'''
https://platform.stratascratch.com/coding/2049-total-order-per-status-per-service?code_type=2
Uber is interested in identifying gaps in their business. 
Calculate the count of orders for each status of each service. 
Your output should include the service name, status of the order, and the number of orders.
'''
# Import your libraries
import pandas as pd

# Start writing code
grouped_data = uber_orders.groupby(['service_name','status_of_order'])['number_of_orders'].sum().reset_index()

grouped_data

