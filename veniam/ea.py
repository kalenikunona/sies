import pandas as pd

# Create a sample dataframe
data = {'col1': [1, 1, 1, 1], 'col2': [2, 2, 2, 2], 'col3': [3, 3, 3, 3]}
df = pd.DataFrame(data)

# Drop columns with only one unique value
for col in df.columns:
    if df[col].nunique() == 1:
        df.drop(col, axis=1, inplace=True)

print(df)
