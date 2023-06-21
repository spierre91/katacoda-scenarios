# Reading Credit Card Transaction data  Pandas
The first thing we need to do is clone the GitHub repo containing the necessary data we will be using:

`git clone https://github.com/spierre91/katacoda-scenarios`{{execute}}

Next we need to go into the folder corresponding to the monolithic time serie analysis lab:
`cd katacoda-scenarios/time-series-monolithic`{{execute}}

We start by importing necessary packages:

`from statsmodels.tsa.api import SimpleExpSmoothing`{{execute}}

`import pandas as pd`{{execute}}

`import plotly.express as px`{{execute}}

`from datetime import timedelta`{{execute}}

`from pmdarima.arima import auto_arima`{{execute}}

`from sklearn.metrics import mean_squared_error`{{execute}}

`import numpy as np`{{execute}}

`import plotly.graph_objects as go`{{execute}}

`from statsmodels.tsa.seasonal import seasonal_decompose`{{execute}}

Next we read our data into a pandas dataframe, and display the first five rows of data:

`df = pd.read_csv("synthetic_transaction_data_Dining.csv")`{{execute}}

`df.head()`{{execute}}

We then can convert the `transaction_date` column to a pandas datetime object and filter out the rows after June 1, 2023

`df["transaction_date"] = pd.to_datetime(df["transaction_date"])`{{execute}}

`df = df[df["transaction_date"] < '2023-06-01']`{{execute}}

Next we can look at a specific merchant. Let's filter for  "McDonald's" and store the result in a data frame called `fast_food`:

`fast_food = df[df['merchant_name'] == "McDonald's"]`{{execute}}

`fast_food.head()`{{execute}}

# Remove outliers from the DataFrame

As a data processing step, we can filter outlier using the Z-score method:
`z_scores = np.abs((fast_food['transaction_amount'] - fast_food['transaction_amount'].mean()) / fast_food['transaction_amount'].std())`{{execute}}


`threshold = 3`{{execute}}


`fast_food = fast_food[z_scores < threshold]`{{execute}}

We can then perform a groupby sum on the `transaction_amount` column by for every `transaction_date`:

`df_grouped = fast_food.groupby(fast_food['transaction_date'].dt.date)['transaction_amount'].sum().reset_index()`{{execute}}

We can then plot the grouped data using Plotly:

`fig = px.line(df_grouped, x='transaction_date', y='transaction_amount', title='Total Transaction Amount by Day')`{{execute}}

`fig.show()`{{execute}}

We can perform these operations in a for-loop and visualize the grouped time series for the first five merchants. 

Let' start by generating Z-scores for each merchant and filteering out ooutliers:
```
for group in list(set(df['merchant_name']))[:5]:
    subgroup = df[df['merchant_name'] == group].copy()
    merchant_category = list(set(subgroup['merchant_category']))[0]
    z_scores = np.abs((subgroup['transaction_amount'] - subgroup['transaction_amount'].mean()) / subgroup['transaction_amount'].std())

    # Define a threshold (e.g., Z-score > 3) to identify outliers
    threshold = 3

    # Remove outliers from the DataFrame
    subgroup = subgroup[z_scores < threshold]
```
We can then create a month-year column which we will use to peerform our groupby operation. It will also specify the granularity oof oour forecasts:

```
for group in list(set(df['merchant_name']))[:5]:
    .... #preceeding code truncated for clarity
    # create week-year column
    subgroup['month'] = subgroup['transaction_date'].dt.month
    subgroup = subgroup[subgroup['month'] <= 12]
    subgroup = subgroup[subgroup['month'] >= 1]
    subgroup['month'] = subgroup['month'].astype(str)

    subgroup['year'] = subgroup['transaction_date'].dt.year
    subgroup['year'] = subgroup['year'].astype(str)

    subgroup['month_year'] =  subgroup['year'] + "-"+  subgroup['month'] 
    subgroup['month_year'] = pd.to_datetime(subgroup['month_year'])
    print(subgroup['month_year'].max())

```
We can then perform our groupby and generate line plots for each merchant:
```
for group in list(set(df['merchant_name']))[:5]:
    .... #preceeding code truncated for clarity
    df_grouped = subgroup.groupby('month_year')['transaction_amount'].sum().reset_index()

    df_grouped = df_grouped.set_index('month_year').sort_index()
    
    trace = go.Scatter(
    x=df_grouped.index,
    y=df_grouped['transaction_amount'],
    mode='lines',
    connectgaps=True)
    layout = go.Layout(
        title=f'{merchant_category}: {group} Total Transaction Amount by month-year',
    )
    # Create the figure and add the trace
    fig = go.Figure(layout=layout)
    fig.add_trace(trace)
    fig.show()

```

The full code block is:
```
for group in list(set(df['merchant_name']))[:5]:
    subgroup = df[df['merchant_name'] == group].copy()
    merchant_category = list(set(subgroup['merchant_category']))[0]
    z_scores = np.abs((subgroup['transaction_amount'] - subgroup['transaction_amount'].mean()) / subgroup['transaction_amount'].std())

    # Define a threshold (e.g., Z-score > 3) to identify outliers
    threshold = 3

    # Remove outliers from the DataFrame
    subgroup = subgroup[z_scores < threshold]
    
    # create week-year column
    subgroup['month'] = subgroup['transaction_date'].dt.month
    subgroup = subgroup[subgroup['month'] <= 12]
    subgroup = subgroup[subgroup['month'] >= 1]
    subgroup['month'] = subgroup['month'].astype(str)

    subgroup['year'] = subgroup['transaction_date'].dt.year
    subgroup['year'] = subgroup['year'].astype(str)

    subgroup['month_year'] =  subgroup['year'] + "-"+  subgroup['month'] 
    subgroup['month_year'] = pd.to_datetime(subgroup['month_year'])
    print(subgroup['month_year'].max())

    df_grouped = subgroup.groupby('month_year')['transaction_amount'].sum().reset_index()

    df_grouped = df_grouped.set_index('month_year').sort_index()
    
    trace = go.Scatter(
    x=df_grouped.index,
    y=df_grouped['transaction_amount'],
    mode='lines',
    connectgaps=True)
    layout = go.Layout(
        title=f'{merchant_category}: {group} Total Transaction Amount by month-year',
    )
    # Create the figure and add the trace
    fig = go.Figure(layout=layout)
    fig.add_trace(trace)
    fig.show()
 ```{{execute}}   
    


