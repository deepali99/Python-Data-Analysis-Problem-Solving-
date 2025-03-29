'''https://platform.stratascratch.com/coding/2072-active-users-per-platform?code_type=2
For each platform (e.g. Windows, iPhone, iPad etc.), calculate the number of users. 
Consider unique users and not individual sessions. 
Output the name of the platform with the corresponding number of users.'''

# Import your libraries
import pandas as pd

# Start writing code
grouped_df = user_sessions.groupby('platform')['user_id'].nunique()
result = grouped_df.reset_index()
