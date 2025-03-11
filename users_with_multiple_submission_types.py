'''
https://platform.stratascratch.com/coding/2002-submission-types?code_type=2
Write a query that returns the user ID of all users that have created at least one ‘Refinance’ submission and at least one ‘InSchool’ submission.
'''

import pandas as pd 
result_1 = loans[loans['type'] == 'Refinance']
result_2 = loans[loans['type'] == 'InSchool']

result = pd.DataFrame(set(result_1['user_id']).intersection 
(set(result_2['user_id'])))
