import pandas as pd
rides = pd.read_csv('capital-onebike.csv')
print(rides.head(3))

rides['Start date']  # Specifies a column
rides.iloc[2] # particular row 

rides = pd.read_csv('capital-onebike.csv'), parse_dates = ['Start date','End date'])          # pandas will treat this columns as datetimes
rides['Start date'] = pd.to_datetime(rides['Start date'], format = "%Y-%m-%d %H:%M:%S")

rides['Start date'].iloc[2]
# Created a duration column
rides['Duration'] = rides['End date'] - rides['Start date']
print(rides['Duration'].head(5))

rides['Duration'\
.dt.total_seconds()\
.head(5)]