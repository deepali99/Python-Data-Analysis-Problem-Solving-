'''
https://platform.stratascratch.com/coding/2057-weight-for-first-shipment?code_type=2
Write a query to find the weight for each shipment's earliest shipment date. Output the shipment id along with the weight.
'''
# Import your libraries
import pandas as pd

# Start writing code
amazon_shipment.head()
min_date = amazon_shipment.groupby('shipment_id')['shipment_date'].min().to_frame('shipment_date').reset_index()
result = amazon_shipment.merge(min_date,on=['shipment_id', 'shipment_date'])[['shipment_id', 'weight']]
