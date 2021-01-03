import pandas as pd
from datetime import datetime, timedelta

out_df = pd.DataFrame(columns=['Date', 'Holiday'])

df = pd.read_csv("res/holidays_2019_2020.csv")
df = df[['Date', 'Holiday']]
df.to_csv('holidays.csv', index=False)

# print(df)
for date_t,holiday_name in zip(df['Date'], df['Holiday']):
    holiday = datetime.strptime(date_t, '%Y-%m-%d')
    for delta in range(-10,11):
        next_day = holiday+timedelta(days=delta)
        if next_day <datetime(year=2019,month=1,day=1) \
                or next_day> datetime(year=2020,month=12,day=31):
            continue
        if not out_df.empty:
            if out_df['Date'].iloc[-1] >= next_day:

        # if out_df['Date'].tail() > next_day:
                print(next_day)
                continue
        new_item = {"Date": next_day, "Holiday": holiday_name}
        out_df = out_df.append(new_item, ignore_index=True)
out_df.to_csv('holiday_period.csv', index=False)

