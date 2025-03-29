'''
https://platform.stratascratch.com/coding/2080-mobile-and-web-logins?code_type=2
Count the number of unique users per day who logged in from both a mobile device and web. Output the date and the corresponding number of users.
'''

# Import your libraries
import pandas as pd

# Start writing code
mobile_logs.head()
all_logs = mobile_logs.merge(web_logs,on = ['user_id','log_date'])
all_logs = all_logs.drop_duplicates()
result = all_logs.groupby('log_date').size().reset_index(name="count")
