'''
https://platform.stratascratch.com/coding/2062-questions-in-second-quarter?code_type=2
How many searches were there in the second quarter of 2021?
'''

# Import your libraries
import pandas as pd

# Start writing code
fb_searches.head()
fb_searches_q2 = fb_searches[(fb_searches['date'].dt.quarter == 2) & (fb_searches['date'].dt.year == 2021)]
result = len(fb_searches_q2) 
