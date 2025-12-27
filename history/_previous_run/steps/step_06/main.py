import os
import threading
from itertools import count
import time as tt
import pandas as pd
from datetime import datetime as dt

from click import wrap_text
from matplotlib.transforms import Bbox
from workalendar.europe import Germany

from concurrent.futures import ThreadPoolExecutor

import matplotlib.pyplot as plt
from datetime import datetime, timedelta,time

from matplotlib.colors import to_rgb
import colorsys



def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def to_pandas(data):
    # Assuming the data is in CSV format
    from io import StringIO
    return pd.read_csv(StringIO(data))

def resolve_columns_type(df):
    for col in df.columns:
        # if the col name is in ["date start", "date end"]
        if col in ["date start", "date end"]:
            df[col] = pd.to_datetime(df[col], format='%d/%m/%Y')
        if col in ["time start", "time end"]:
            df[col] = pd.to_datetime(df[col], format='%H:%M').dt.time
        if col in ["Status","To-Fill","Weekly","bi-weekly","one-time"]:
            df[col] = df[col].astype('bool')
        # its weekday
        if col in ["Day"]:
            df[col] = pd.to_datetime(df[col], format='%A').dt.day_name()

    return df

def format_hour(hour):
    h = int(hour)
    m = int((hour - h) * 60)
    s = int(((hour - h) * 60 - m) * 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def create_master_calendar_with_holidays(df):
    # Create date range
    cal = Germany()  # or use GermanySaxony(), GermanyBavaria(), etc.

    start_date = df['date start'].min() - pd.DateOffset(days=1)  # Include the start date
    # start_date = datetime.today()  # Include the start date
    end_date = df['date end'].max()+ pd.DateOffset(days=1)  # Include the end date
    date_range = pd.date_range(start=start_date, end=end_date)

    # Create master calendar
    master_calendar = pd.DataFrame(date_range, columns=['date'])
    master_calendar['day'] = master_calendar['date'].dt.day_name()

    # German holidays (national)
    master_calendar['Holiday'] = master_calendar['date'].apply(
        lambda x: cal.get_holiday_label(x.date()) if cal.is_holiday(x.date()) else None
    )

    # Mark weekends
    master_calendar['IsWeekend'] = master_calendar['day'].isin(['Saturday', 'Sunday'])
    # Combine into "IsOffDay"
    master_calendar['IsOffDay'] = master_calendar.apply(
        lambda row: bool(row['Holiday']) or row['IsWeekend'], axis=1
    )
    master_calendar["childs"] = ""

    master_calendar = master_calendar.reset_index(drop=True)

    return master_calendar

def extend_original_df(org_df):
    extended_rows = []

    for _, row in org_df.iterrows():
        if row['Status'] == False:
            continue
        start_date = row['date start']
        end_date = row['date end']
        weekday = row['day']

        if row.get('weekly') == True:
            date_range = pd.date_range(start=start_date, end=end_date)
            for date in date_range:
                if date.strftime('%A') == weekday:
                    new_row = row.copy()
                    new_row['date start'] = date
                    new_row['date end'] = date
                    extended_rows.append(new_row)

        elif row.get('bi-weekly') == True:
            # Start from the first occurrence of the correct weekday
            current_date = start_date
            while current_date <= end_date:
                if current_date.strftime('%A') == weekday:
                    break
                current_date += pd.Timedelta(days=1)
            # Now build a bi-weekly series from that day
            date_range = pd.date_range(start=current_date, end=end_date, freq='2W')
            for date in date_range:
                new_row = row.copy()
                new_row['date start'] = date
                new_row['date end'] = date
                extended_rows.append(new_row)

        elif row.get('one-time') == True:
            date_range = pd.date_range(start=start_date, end=end_date)
            for date in date_range:
                new_row = row.copy()
                new_row['date start'] = date
                new_row['date end'] = date
                extended_rows.append(new_row)
        elif row.get("daily") == True:
            date_range = pd.date_range(start=start_date, end=end_date)
            for date in date_range:
                new_row = row.copy()
                new_row['date start'] = date
                new_row['date end'] = date
                extended_rows.append(new_row)

    # Return as DataFrame
    res = pd.DataFrame(extended_rows)
    # make indexs of res unique
    res = res.reset_index(drop=True)
    res.rename(columns={'date start':'date'}, inplace=True)
    res.drop(columns=['date end'], inplace=True)
    res = res.reset_index(drop=True)


    return res

def aggregate_mc_df(df,mc):
    for index, row in mc.iterrows():
        chidls = []
        for _, row2 in df.iterrows():
            if row['date'] == row2['date']:
                # append the index of row2
                chidls.append(_)
        childs =  '-'.join(map(str, chidls))
        # add the index of row to the list
        mc.at[index, 'childs'] = childs
    return mc

def adjust_lightness(hex_color, lightness):
    """Adjust lightness of a base color using HLS."""
    rgb = to_rgb(hex_color)
    h, _, s = colorsys.rgb_to_hls(*rgb)
    r, g, b = colorsys.hls_to_rgb(h, lightness, s)
    return '#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255))

class colors_memory:
    data = {}  # format: {'group': {'color': '#hex', 'child_colors': {'child1': '#hex', ...}}}

def assign_unique_colors(groups_dict):
    cmap = plt.get_cmap("Accent")

    for i, group in enumerate(groups_dict.keys()):
        # === GROUP COLOR ===
        if group in colors_memory.data and "color" in colors_memory.data[group]:
            hex_base = colors_memory.data[group]["color"]
        else:
            base_color = cmap(i % cmap.N)
            hex_base = '#%02x%02x%02x' % tuple(int(c * 255) for c in base_color[:3])
            colors_memory.data[group] = {"color": hex_base}

        groups_dict[group]["color"] = hex_base

        # === CHILD COLORS ===
        children = groups_dict[group].get("childs", [])
        n = len(children)

        min_lightness = 0.3
        max_lightness = 0.85
        if n > 1:
            steps = [min_lightness + i * (max_lightness - min_lightness) / (n - 1) for i in range(n)]
        else:
            steps = [(min_lightness + max_lightness) / 2]

        child_colors = {}
        for child, lightness in zip(children, steps):
            # Check memory for child color
            if group in colors_memory.data and "child_colors" in colors_memory.data[group] and child in colors_memory.data[group]["child_colors"]:
                color = colors_memory.data[group]["child_colors"][child]
            else:
                color = adjust_lightness(hex_base, lightness)
                # Save to memory
                colors_memory.data[group].setdefault("child_colors", {})[child] = color

            child_colors[child] = color

        groups_dict[group]["child_colors"] = child_colors

    return groups_dict

def calculate_time(start_time, end_time, target):
    fmt = "%H:%M"

    start_dt = datetime.strptime(start_time, fmt)
    if end_time == "24:00":
        end_time = "00:00"
    end_dt = datetime.strptime(end_time, fmt)
    target_dt = datetime.strptime(target.strftime(fmt), fmt)
    # Total range in hours
    total_hours = (end_dt - start_dt).total_seconds() / 3600
    # Time from start to target in hours
    target_hours = (target_dt - start_dt).total_seconds() / 3600

    return target_hours  # This is the scaled float value
def group_rectangles(rects):
    def get_range(item):
        start = item['rectangle_x']
        end = start + item['rectangle_width']
        return start, end

    groups = []

    for rect in rects:
        r_start, r_end = get_range(rect)
        placed = False

        for group in groups:
            if any(
                r_start < other['rectangle_x'] + other['rectangle_width'] and
                r_end > other['rectangle_x']
                for other in group
            ):
                group.append(rect)
                placed = True
                break

        if not placed:
            groups.append([rect])

    return groups

class font_vals:
    data = []

def auto_fit_fontsize(text, width, height, fig=None, ax=None, min_fontsize=1, margin=0.95):
    fig = fig
    ax = ax

    # Look for existing fit in cache
    for cached in font_vals.data:
        if (
            cached["text"] == text.get_text() and
            cached["width"] == width and
            cached["height"] == height
        ):
            text.set_fontsize(cached["fontsize"])
            return cached["fontsize"]

    renderer = fig.canvas.get_renderer()

    # Convert box size (data units) to pixel size
    top_right_px = ax.transData.transform((text._x + width / 2, text._y + height / 2))
    bottom_left_px = ax.transData.transform((text._x - width / 2, text._y - height / 2))
    box_width_px = abs(top_right_px[0] - bottom_left_px[0])
    box_height_px = abs(top_right_px[1] - bottom_left_px[1])

    # Try decreasing font sizes until it fits
    for fontsize in reversed(range(min_fontsize, int(text.get_fontsize()) + 1)):
        text.set_fontsize(fontsize)
        fig.canvas.draw()
        bb = text.get_window_extent(renderer=renderer)
        if bb.width <= box_width_px * margin and bb.height <= box_height_px * margin:
            font_vals.data.append({
                "text": text.get_text(),
                "width": width,
                "height": height,
                "fontsize": fontsize
            })
            return fontsize

    # Fall back to min fontsize
    text.set_fontsize(min_fontsize)
    font_vals.data.append({
        "text": text.get_text(),
        "width": width,
        "height": height,
        "fontsize": min_fontsize
    })
    return min_fontsize

def draw_calendar(mc_inside, df_inside, start_hour=8, end_hour=20, box_width=2, box_height=0.8, name_file="calendar.png",no_output=False):
    start_date = mc_inside['date'].min()
    end_date = mc_inside['date'].max()

    # Generate dates and hours
    dates = pd.date_range(start=start_date, end=end_date)
    hours = range(start_hour, end_hour + 1)
    start_hour = f"{start_hour}:00"
    end_hour = f"{end_hour}:00"

    fig, ax = plt.subplots(figsize=(len(hours) * box_width, len(dates) * box_height))
    max_width = 0
    for j, date in enumerate(dates):
        day_name = date.strftime('%A')
        label = f"{date.date()}{day_name}"
        max_width = max(max_width, len(label))

    today = datetime.today().date()

    # Draw horizontal grid lines (for each day)
    for j, date in enumerate(dates):
        y = j * box_height

        # Highlight today's row with light yellow background
        if no_output == False:
            print(date.date() == today , today, date.date())
        if date.date() == today:
            patch = plt.Rectangle(
                (0, 0),
                -box_width,
                y,
                color="red",
                alpha=0.6
            )
            ax.add_patch(patch)



        # Draw grid line
        ax.axhline(y=y, color='lightgray', linewidth=0.5)

        # Format label
        day_name = date.strftime('%A')
        label = f"{date.date()} {day_name}"
        cur_length = len(label)
        spaces = ' ' * (max_width - cur_length + 5)
        label = f"{date.date()}{spaces}{day_name}"

        # Draw day label
        ax.text(-0.1, y + box_height / 2, label, ha='right', va='center', fontsize=8, transform=ax.transData,color='black')
    # Set axis limits based on box size
    ax.set_xlim(0, len(hours) * box_width)
    ax.set_ylim(0, len(dates) * box_height)
    ax.invert_yaxis()
    ax.axis('off')
    items = {}
    dates = dates.tolist()
    # 1 - 6
    colors = {}
    new_hours = []
    for _,d in mc_inside.iterrows():
        for c in d["childs"].strip().split("-"):
            try:
                item = df_inside.iloc[int(c)]
                date = d["date"]

                start_t = calculate_time(start_hour, end_hour, item["time start"])
                end_t = calculate_time(start_hour, end_hour,  item["time end"])
                start_t = start_t * box_width
                end_t = end_t * box_width
                y = dates.index(date) * box_height

                temp = {

                    "rectangle_x": start_t,
                    "rectangle_y": y,
                    "rectangle_width": end_t - start_t,
                    "rectangle_height": box_height,
                    "color": "skyblue",

                    "name" : f"{item["group"]+"\n"+item["name"]}",
                    "group": item["group"],
                }
                if item["time start"] not in new_hours:
                    new_hours.append(item["time start"])
                if item["time end"] not in new_hours:
                    new_hours.append(item["time end"])
                if item["group"] not in colors:
                    colors[item["group"]] = {"color":"","childs":[]}
                if temp["name"] not in colors[item["group"]]["childs"]:
                    colors[item["group"]]["childs"].append(temp["name"])
                if d["date"] not in items:
                    items[d["date"]] = []
                items[d["date"]].append(temp)
            except:
                pass
    colors = assign_unique_colors(colors)
    final_items = {}

    already_hours = []
    # Draw vertical grid lines (for each hour)
    for i, hour in enumerate(hours):
        x = i * box_width

        ax.axvline(x=x, color='lightgray', linewidth=0.5)
        ax.text(x, -0.75, format_hour(hour), ha='left', va='top', fontsize=8, rotation=90)
        already_hours.append(hour)
    for hour in new_hours:

        if hour in already_hours:
            continue
        ax.axvline(x=calculate_time(start_hour,end_hour,hour), color='lightgray', linewidth=0.5)
        ax.text(calculate_time(start_hour,end_hour,hour), -0.75, hour, ha='left', va='top', fontsize=8, rotation=90)

    for date, t in items.items():
        final_items[date] = []
        groups = group_rectangles(t)

        for g in groups:
            total_height = g[0]["rectangle_height"]  # assume all share the same height
            base_y = g[0]["rectangle_y"]  # shared starting y

            slice_height = total_height / len(g)

            for ind, item in enumerate(g):
                item["color"] = colors[item["group"]]["child_colors"][item["name"]]
                item["rectangle_height"] = slice_height
                item["rectangle_y"] = base_y + slice_height * ind
                final_items[date].append(item)

    draw_objects = []

    c = sum(len(t) for t in final_items.values())
    cc = 0

    for date, t in final_items.items():
        for item in t:
            if no_output == False:

                print(cc, "/", c)
            patch = plt.Rectangle(
                (item["rectangle_x"], item["rectangle_y"]),
                item["rectangle_width"],
                item["rectangle_height"],
                color=item["color"],
                alpha=0.6
            )
            ax.add_patch(patch)

            text = ax.text(
                item["rectangle_x"] + (item["rectangle_width"] / 2),
                item["rectangle_y"] + (item["rectangle_height"] / 2),
                item["name"],
                ha='center',
                va='center',
                fontsize=20  # Start with medium
            )
            auto_fit_fontsize(
                text,
                width=item["rectangle_width"],
                height=item["rectangle_height"],
                fig=fig,
                ax=ax,
                min_fontsize=2  # prevent invisible text
            )
            cc += 1

    plt.tight_layout()
    if no_output == False:
        plt.show()
    fig.savefig(name_file, bbox_inches='tight', dpi=300)


if __name__ == '__main__':


    file_path = 'temp.csv'

    # read - convert to pd - and resolve columns type
    data = load_data(file_path)
    df_org = to_pandas(data)
    df_org = resolve_columns_type(df_org)

    mc = create_master_calendar_with_holidays(df_org)
    extended_df = extend_original_df(df_org)
    mc = aggregate_mc_df(extended_df, mc)


    mc.to_csv('master_calendar.csv', index=False)
    extended_df.to_csv('extended_data.csv', index=False)

    today = datetime.today().date()

    # Filter: only rows where the date is today or in the future


    draw_calendar(
        mc,
        extended_df,
        start_hour=6,
        end_hour=24,
        name_file="calendar.png",
    )

    fmt = "%Y-%m-%d"


    # 7 days mc
    min_date_mc_7_days = mc['date'].min()
    max_date_mc_7_days = mc['date'].max()
    range_dates_7_days = {}
    c_date_7_days = min_date_mc_7_days

    while c_date_7_days <= max_date_mc_7_days:
        range_dates_7_days[c_date_7_days.strftime(fmt)+" _ "+(c_date_7_days + timedelta(days=7)).strftime(fmt)]= {"start_date": c_date_7_days,"end_date": c_date_7_days + timedelta(days=7)}
        c_date_7_days += timedelta(days=1)
    num_workers = max(1, os.cpu_count() - 1)

    all_c = len(range_dates_7_days)
    print("Number of tasks:", all_c)
    c_c = 0
# Function to wrap calendar drawing safely
def draw_calendar_task(args):
    global c_c
    key, value = args
    file_name = f"./frames/calendar_{key}.png"
    start_date = value["start_date"]
    end_date = value["end_date"]

    new_filtered_mc = mc[(mc['date'] >= start_date) & (mc['date'] <= end_date)]

    try:
        draw_calendar(
            new_filtered_mc,
            extended_df,
            start_hour=6,
            end_hour=24,
            name_file=file_name,
            no_output=True,
            box_height=1.2
        )
    except Exception as e:
        print(f"❌ Error in drawing calendar for {start_date} → {end_date}: {e}")
    c_c+=1
    print(c_c, "/", all_c)
# Prepare task list
tasks = list(range_dates_7_days.items())

# Execute in parallel
with ThreadPoolExecutor(max_workers=num_workers) as executor:
    executor.map(draw_calendar_task, tasks)
