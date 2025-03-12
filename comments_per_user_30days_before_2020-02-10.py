'''
https://platform.stratascratch.com/coding/2004-number-of-comments-per-user-in-past-30-days?code_type=2
Return the total number of comments received for each user in the 30 or less days before 2020-02-10. 
Don't output users who haven't received any comment in the defined time period.

'''

# Import your libraries
import pandas as pd
from datetime import timedelta  

# Start writing code
fb_comments_count.head()
start_date = pd.to_datetime('2020-02-10') - timedelta(days=30)
end_date = pd.to_datetime('2020-02-10')

result = fb_comments_count[
(fb_comments_count['created_at'] >= start_date) 
& 
(fb_comments_count['created_at'] <= end_date)].groupby('user_id')['number_of_comments'].sum().reset_index()
