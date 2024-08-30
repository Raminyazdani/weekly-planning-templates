import pandas as pd
from datetime import datetime as dt
from workalendar.europe import Germany

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def to_pandas(data):
    from io import StringIO
    return pd.read_csv(StringIO(data))

def resolve_columns_type(df):
    for col in df.columns:
        if col in ["date start", "date end"]:
            df[col] = pd.to_datetime(df[col], format='%d/%m/%Y')
        if col in ["time start", "time end"]:
            df[col] = pd.to_datetime(df[col], format='%H:%M').dt.time
        if col in ["Status","To-Fill","Weekly","bi-weekly","one-time"]:
            df[col] = df[col].astype('bool')
        if col in ["Day"]:
            df[col] = pd.to_datetime(df[col], format='%A').dt.day_name()
    return df

def create_master_calendar_with_holidays(df):
    cal = Germany()
    start_date = df['date start'].min() - pd.DateOffset(days=1)
    end_date = df['date end'].max()+ pd.DateOffset(days=1)
    date_range = pd.date_range(start=start_date, end=end_date)
    
    master_calendar = pd.DataFrame(date_range, columns=['date'])
    master_calendar['day'] = master_calendar['date'].dt.day_name()
    master_calendar['Holiday'] = master_calendar['date'].apply(
        lambda x: cal.get_holiday_label(x.date()) if cal.is_holiday(x.date()) else None
    )
    master_calendar['IsWeekend'] = master_calendar['day'].isin(['Saturday', 'Sunday'])
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
        elif row.get('one-time') == True:
            date_range = pd.date_range(start=start_date, end=end_date)
            for date in date_range:
                new_row = row.copy()
                new_row['date start'] = date
                new_row['date end'] = date
                extended_rows.append(new_row)
                
    res = pd.DataFrame(extended_rows)
    res = res.reset_index(drop=True)
    res.rename(columns={'date start':'date'}, inplace=True)
    res.drop(columns=['date end'], inplace=True)
    return res

def aggregate_mc_df(df,mc):
    for index, row in mc.iterrows():
        chidls = []
        for _, row2 in df.iterrows():
            if row['date'] == row2['date']:
                chidls.append(_)
        childs =  '-'.join(map(str, chidls))
        mc.at[index, 'childs'] = childs
    return mc

if __name__ == '__main__':
    file_path = 'temp.csv'
    data = load_data(file_path)
    df_org = to_pandas(data)
    df_org = resolve_columns_type(df_org)
    mc = create_master_calendar_with_holidays(df_org)
    extended_df = extend_original_df(df_org)
    mc = aggregate_mc_df(extended_df, mc)
    mc.to_csv('master_calendar.csv', index=False)
    extended_df.to_csv('extended_data.csv', index=False)
    print("Master calendar and extended data created!")
