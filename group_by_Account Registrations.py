'''
https://platform.stratascratch.com/coding/2126-account-registrations?code_type=2
Find the number of account registrations according to the signup date. Output the year months (YYYY-MM) and their corresponding number of registrations.
'''

# Import your libraries
import pandas as pd

# Start writing code
noom_signups['started_at_month'] = noom_signups['started_at'].dt.to_period('M')

result = noom_signups.groupby('started_at_month').size().rename('n_registrations').reset_index()
result
