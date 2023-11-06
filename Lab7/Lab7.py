
'''
Brandon Ornelas, Connor Case, Kai Clough, Leo Ramirez
Lab 7 
'''

import io
import pandas as pd
import requests as r

# Define the URL and file name
url = 'http://drd.ba.ttu.edu/isqs3358/Labs/Lab7/'
file_1 = 'team_missing_data.csv'

# Load the data from the URL
response = r.get(url + file_1)
data = pd.read_csv(io.StringIO(response.text))

# Define the columns to handle missing values
columns_to_handle = ['points_scored', 'points_allowed', 'opposing_team']

def handle_missing_values(data, method):
    if method == 1:
        # Round 1: Drop all NA Records
        cleaned_data = data.dropna(subset=columns_to_handle)
    elif method == 2:
        # Round 2: Fill Numerics with 0, Textual with "-default-"
        cleaned_data = data.fillna({'points_scored': 0, 'points_allowed': 0, 'opposing_team': '-default-'})
    elif method == 3:
        # Round 3: Fill Numerics with Column average, Textual with "-default-"
        cleaned_data = data.fillna({'points_scored': data['points_scored'].mean(),
                                    'points_allowed': data['points_allowed'].mean(),
                                    'opposing_team': '-default-'})
    elif method == 4:
        # Round 4: Fill Numerics with team_id based average, Textual with distribution sampling
        cleaned_data = data.copy()
        team_id_avg = cleaned_data.groupby('team_id')[['points_scored', 'points_allowed']].transform('mean')
        cleaned_data[['points_scored', 'points_allowed']] = cleaned_data[['points_scored', 'points_allowed']].fillna(team_id_avg)
        cleaned_data['opposing_team'] = cleaned_data.groupby('team_id')['opposing_team'].transform(lambda x: x.fillna(x.sample(frac=1, random_state=42).iloc[0]))

    
    return cleaned_data

# Define column metrics to report
column_metrics = ['Mean', 'Median', 'Variance']

# Define column names for better display
column_names = {'points_scored': 'Points Scored',
                'points_allowed': 'Points Allowed',
                'opposing_team': 'Opposing Team'}

# Loop through each handling method
for round_num in range(1, 5):
    print(f'Round {round_num}:')
    cleaned_data = handle_missing_values(data, round_num)
    
    # Calculate and print column metrics
    for column in columns_to_handle:
        if column == 'opposing_team':
            continue
        print(f'{column_names[column]}:')
        print(f'  Mean: {cleaned_data[column].mean()}')
        print(f'  Median: {cleaned_data[column].median()}')
        print(f'  Variance: {cleaned_data[column].var()}')
    
    print('\n')

# Optionally, you can display the cleaned_data after each round
# Example: print(cleaned_data)
