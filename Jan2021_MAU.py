'''
https://platform.stratascratch.com/coding/2051-monthly-active-users?code_type=2

Find the monthly active users for January 2021 for each account. 
Your output should have account_id and the monthly count for that account.

'''

# Import your libraries
import pandas as pd

# Start writing code
sf_events.head()
dates_jan_2021 = sf_events[sf_events['record_date'].between('2021-01-01','2021-01-31')]
monthly_active_users = dates_jan_2021.groupby('account_id')['user_id'].nunique()
result = monthly_active_users.reset_index()
result
