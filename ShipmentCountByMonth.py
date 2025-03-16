'''
https://platform.stratascratch.com/coding/2056-number-of-shipments-per-month?code_type=2
Write a query that will calculate the number of shipments per month.
The unique key for one shipment is a combination of shipment_id and sub_id. 
Output the year_month in format YYYY-MM and the number of shipments in that month.

'''
# number of shipments per month 
# shipment_id + sub_id
# Import your libraries
import pandas as pd

# Start writing code
# Create a new column to extract year_month 
amazon_shipment['year_month']= amazon_shipment['shipment_date'].dt.to_period('M')
# Create a new column to create a unique key 
# shipment_id
# sub_id
amazon_shipment['unique_key'] = amazon_shipment['shipment_id'].astype(str) + '_' + amazon_shipment['sub_id'].astype(str)
amazon_shipment


result = amazon_shipment.groupby('year_month')['unique_key'].nunique().reset_index(name='count')

result
