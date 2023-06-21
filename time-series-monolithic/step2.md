`df_dominos = df[df['merchant_name'] == "Domino's Pizza"]`{{execute}}


`z_scores = np.abs((df_dominos['transaction_amount'] - df_dominos['transaction_amount'].mean()) / df_dominos['transaction_amount'].std())`{{execute}}

# Define a threshold (e.g., Z-score > 3) to identify outliers
`threshold = 3`{{execute}}

# Remove outliers from the DataFrame
`df_dominos = df_dominos[z_scores < threshold]`{{execute}}

# create week-year column
`df_dominos['month'] = df_dominos['transaction_date'].dt.month`{{execute}}

`df_dominos = df_dominos[df_dominos['month'] <= 12]`{{execute}}

`df_dominos = df_dominos[df_dominos['month'] >= 1]`{{execute}}

`df_dominos['month'] = df_dominos['month'].astype(str)`{{execute}}

`df_dominos['year'] = df_dominos['transaction_date'].dt.year`{{execute}}

`df_dominos['year'] = df_dominos['year'].astype(str)`{{execute}}

`df_dominos['month_year'] =  df_dominos['year'] + "-"+  df_dominos['month']`{{execute}}

`df_dominos['month_year'] = pd.to_datetime(df_dominos['month_year'])`{{execute}}

`print(df_dominos['month_year'].max())`{{execute}}

`df_grouped = df_dominos.groupby('month_year')['transaction_amount'].sum().reset_index()`{{execute}}

`df_grouped = df_grouped.set_index('month_year').sort_index()`{{execute}}

`df_grouped.index = pd.to_datetime(df_grouped.index)`{{execute}}


# Split the data into training and testing sets
`cutoff_point1 = pd.to_datetime("2023-03-01")`{{execute}}

`cutoff_point2 = pd.to_datetime("2023-06-01")`{{execute}}

`train_data = df_grouped[df_grouped.index < cutoff_point1]`{{execute}}

`test_data = df_grouped[(df_grouped.index >= cutoff_point1) & (df_grouped.index <= cutoff_point2)]`{{execute}}



