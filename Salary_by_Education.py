'''
https://platform.stratascratch.com/coding/2100-salary-by-education?code_type=2
Given the education levels and salaries of a group of individuals, find what is the average salary for each level of education.
'''

# Import your libraries
import pandas as pd

# Start writing code
result = google_salaries.groupby('education')['salary'].mean()
result= result.reset_index()
