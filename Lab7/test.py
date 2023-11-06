import pandas as pd
import requests as r
import io

# Load the CSV file
url = "http://drd.ba.ttu.edu/isqs3358/Labs/Lab7/"
file = 'team_missing_data.csv'
res = r.get(url + file)
df = pd.read_csv(io.StringIO(res.text))

task_names = [
    "DropNA Method",
    "FillNA with 0 Method",
    "FillNA with Column Average",
    "Fill with Team based Column Average Method"
]

rounds = [
    # Task 1: Drop all NA Records
    df.dropna(),

    # Task 2: Fill missing values with 0 or "-default-"
    df.fillna({'points_scored': 0, 'points_allowed': 0, 'opposing_team': '-default-'}),

    # Task 3: Fill missing numeric values with column average
    # and textual values with "-default-"
    df.fillna({'points_scored': df['points_scored'].mean(), 'points_allowed': df['points_allowed'].mean(), 'opposing_team': '-default-'}),

    # Task 4: Fill missing numeric values with team_id-based average
    # and textual values with distribution sampling
    df.assign(
        points_scored=df.groupby('team_id')['points_scored'].transform(lambda x: x.fillna(x.mean())),
        opposing_team=df['opposing_team'].fillna(df['opposing_team'].dropna().sample(frac=1).reset_index(drop=True))
    )
]

# Report the column metrics for each task
for i, round_data in enumerate(rounds):
    print()
    print(f"---------- Task #{i + 1} {task_names[i]} ----------")
    numeric_columns = ['points_scored', 'points_allowed']
    print("Mean:")
    print(round_data[numeric_columns].mean())
    print("\nMedian:")
    print(round_data[numeric_columns].median())
    print("\nVariance:")
    print(round_data[numeric_columns].var())

    # Calculate and print mean by opposing team with columns switched
    mean_by_team = round_data.groupby('opposing_team')[numeric_columns[::-1]].mean()
    print("\nMean by Opposing Team:")
    print(mean_by_team)

