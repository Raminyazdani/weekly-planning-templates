import pandas as pd
from datetime import datetime as dt

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

def create_master_calendar(df):
    start_date = df['date start'].min() - pd.DateOffset(days=1)
    end_date = df['date end'].max()+ pd.DateOffset(days=1)
    date_range = pd.date_range(start=start_date, end=end_date)
    
    master_calendar = pd.DataFrame(date_range, columns=['date'])
    master_calendar['day'] = master_calendar['date'].dt.day_name()
    master_calendar['IsWeekend'] = master_calendar['day'].isin(['Saturday', 'Sunday'])
    master_calendar["childs"] = ""
    master_calendar = master_calendar.reset_index(drop=True)
    return master_calendar

if __name__ == '__main__':
    file_path = 'temp.csv'
    data = load_data(file_path)
    df_org = to_pandas(data)
    df_org = resolve_columns_type(df_org)
    mc = create_master_calendar(df_org)
    mc.to_csv('master_calendar.csv', index=False)
    print("Master calendar created!")
