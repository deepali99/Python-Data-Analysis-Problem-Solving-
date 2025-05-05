'''
https://platform.stratascratch.com/coding/2043-employees-without-annual-review?code_type=2
Return all employees who have never had an annual review. Your output should include the employee's first name, last name, hiring date, and termination date. List the most recently hired employees first.

'''
import pandas as pd
review_ids = uber_annual_review['emp_id'].unique()
result = uber_employees[~uber_employees['id'].isin(review_ids)][['first_name', 'last_name', 'hire_date', 'termination_date']].sort_values('hire_date', ascending=False)
