# Data preparation for time series forecasting

Let's proceed by filtering our data frame to only include rows for  "Domino's Pizza":

`df_dominos = df[df['merchant_name'] == "Domino's Pizza"]`{{execute}}

We can then calculate Z-scores for this filtered data:

`z_scores = np.abs((df_dominos['transaction_amount'] - df_dominos['transaction_amount'].mean()) / df_dominos['transaction_amount'].std())`{{execute}}

Define a threshold (e.g., Z-score > 3) to identify outliers:

`threshold = 3`{{execute}}

Remove outliers from the DataFrame:

`df_dominos = df_dominos[z_scores < threshold]`{{execute}}

create mooth column:

`df_dominos['month'] = df_dominos['transaction_date'].dt.month`{{execute}}

Filter out invalid month values:

`df_dominos = df_dominos[df_dominos['month'] <= 12]`{{execute}}

`df_dominos = df_dominos[df_dominos['month'] >= 1]`{{execute}}

Convert month into a string for concatenation:

`df_dominos['month'] = df_dominos['month'].astype(str)`{{execute}}


Create a year column:

`df_dominos['year'] = df_dominos['transaction_date'].dt.year`{{execute}}

Coonvert month into a string for concatenation:

`df_dominos['year'] = df_dominos['year'].astype(str)`{{execute}}

Create month-year column:

`df_dominos['month_year'] =  df_dominos['year'] + "-"+  df_dominos['month']`{{execute}}

Coonvert to a pandas datetime:

`df_dominos['month_year'] = pd.to_datetime(df_dominos['month_year'])`{{execute}}


Perform a groupby sum on the `transaction_amount` by the `month_year` column:

`df_grouped = df_dominos.groupby('month_year')['transaction_amount'].sum().reset_index()`{{execute}}

Set `month_year` as the index:

`df_grouped = df_grouped.set_index('month_year').sort_index()`{{execute}}

Convert index to a datetime object:

`df_grouped.index = pd.to_datetime(df_grouped.index)`{{execute}}


Define cut offs for train/test split: 

`cutoff_point1 = pd.to_datetime("2023-03-01")`{{execute}}

`cutoff_point2 = pd.to_datetime("2023-06-01")`{{execute}}

Split the data into training and testing sets:

`train_data = df_grouped[df_grouped.index < cutoff_point1]`{{execute}}

`test_data = df_grouped[(df_grouped.index >= cutoff_point1) & (df_grouped.index <= cutoff_point2)]`{{execute}}



