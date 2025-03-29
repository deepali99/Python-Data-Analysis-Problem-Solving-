'''
https://platform.stratascratch.com/coding/2083-pending-claims?code_type=2
Count how many claims submitted in December 2021 are still pending. A claim is pending when it has neither an acceptance nor rejection date
'''

import pandas as pd

# Filter for claims submitted in December 2021 that have no acceptance or rejection date
filtered_claims = cvs_claims[(pd.to_datetime(cvs_claims['date_submitted']).dt.to_period('M') == '2021-12') & 
                            (cvs_claims['date_accepted'].isna()) & 
                            (cvs_claims['date_rejected'].isna())]
# Count the number of pending claims
result = filtered_claims.shape[0]
