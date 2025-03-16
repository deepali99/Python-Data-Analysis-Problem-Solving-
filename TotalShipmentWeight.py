'''
https://platform.stratascratch.com/coding/2058-total-shipment-weight?code_type=2
Calculate the total weight for each shipment and add it as a new column. 
Your output needs to have all the existing rows and columns in addition to the  new column that shows the total weight for each shipment. 
One shipment can have multiple rows.
'''

# Import your libraries
import pandas as pd

# Start writing code
amazon_shipment.head()
amazon_shipment['total_weight'] = amazon_shipment.groupby('shipment_id')['weight'].transform('sum')
result = amazon_shipment
