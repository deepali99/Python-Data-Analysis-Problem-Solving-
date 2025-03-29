/*
https://platform.stratascratch.com/coding/2109-products-with-no-sales?code_type=2
Write a query to get a list of products that have not had any sales. Output the ID and market name of these products.
*/

# Import your libraries
import pandas as pd

# Start writing code
fct_customer_sales.head()
sales_and_products = dim_product.merge(fct_customer_sales, on ='prod_sku_id' , how = 'left')

result = sales_and_products[sales_and_products['order_id'].isna()][['prod_sku_id', 'market_name']]
