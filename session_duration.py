'''
https://platform.stratascratch.com/coding/2013-customer-average-orders?code_type=2
How many customers placed an order and what is the average order amount?
'''

# Import your libraries
import pandas as pd

# Start writing code
postmates_orders.head()
postmates_orders.agg({'customer_id' : 'nunique','amount' : 'mean'  }).reset_index()
