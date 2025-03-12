'''
https://platform.stratascratch.com/coding/2006-users-activity-per-month-day/official-solution?code_type=2
Return a distribution of users activity per day of the month. By distribution we mean the number of posts per day of the month.
'''

import pandas as pd
# Start writing code
facebook_posts.head()
result = facebook_posts.groupby(facebook_posts.post_date.dt.day)['post_id'].count().reset_index()
