'''
https://platform.stratascratch.com/coding/2017-paid-users-in-april-2020?code_type=2
How many paid users had any calls in Apr 2020?

'''


# Import your libraries
import pandas as pd

# Start writing code
rc_calls.head()
paid_users = rc_users[rc_users['status'] == 'paid']['user_id']
rc_calls = rc_calls[ rc_calls['date'].between('2020-04-01', '2020-04-30')]
