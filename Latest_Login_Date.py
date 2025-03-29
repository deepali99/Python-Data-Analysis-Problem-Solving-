'''
https://platform.stratascratch.com/coding/2091-latest-login-date?code_type=2
For each video game player, find the latest date when they logged in.
'''

# Import your libraries
import pandas as pd

# Start writing code
result = players_logins.groupby('player_id')['login_date'].max().reset_index()
