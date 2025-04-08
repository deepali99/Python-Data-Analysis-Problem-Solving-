'''
https://platform.stratascratch.com/coding/2067-low-fat-and-recyclable?code_type=2
What percentage of all products are both low fat and recyclable?
'''

import pandas as pd
df = facebook_products[
(facebook_products['is_low_fat'] == 'Y') & 
(facebook_products['is_recyclable'] == 'Y')
]
result = len(df)/len(facebook_products) *100.0
