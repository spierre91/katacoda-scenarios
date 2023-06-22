# Refactoring time series exploratory data analysis coode

We can start by defining a function that reads in our data, converts `transaction_date` into a pandas datetime, and filter out row before June 1, 2023:

```
def read_data(file_path):
    df = pd.read_csv(file_path)
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])
    df = df[df["transaction_date"] < '2023-06-01']
    return df
```


Next we will define a function that plots the daily transaction amounts. We first perform a groupby sum on `transaction_amount` by `transaction_date` and use the Plotly express line method to plot the time series:

```
def plot_total_amount_by_day(df):
    df_grouped = df.groupby(df['transaction_date'].dt.date)['transaction_amount'].sum().reset_index()
    fig = px.line(df_grouped, x='transaction_date', y='transaction_amount', title='Total Transaction Amount by Day')
    fig.show()
```

Next we will define a function that alloows us to plot our time series at a monthly granularity. The function will take a dataframe and a list of merchants and display line plots of our time series data for each merchant:

```
def plot_amount_by_month_year(df, merchant_names):
    for merchant_name in merchant_names:
        subgroup = df[df['merchant_name'] == merchant_name].copy()
        subgroup['month'] = subgroup['transaction_date'].dt.month
        subgroup = subgroup[(subgroup['month'] <= 12) & (subgroup['month'] >= 1)]
        subgroup['month'] = subgroup['month'].astype(str)
        subgroup['year'] = subgroup['transaction_date'].dt.year.astype(str)
        subgroup['month_year'] = pd.to_datetime(subgroup['year'] + "-" + subgroup['month'])
        
        df_grouped = subgroup.groupby('month_year')['transaction_amount'].sum().reset_index()
        df_grouped = df_grouped.set_index('month_year').sort_index()
        
        trace = go.Scatter(x=df_grouped.index, y=df_grouped['transaction_amount'], mode='lines', connectgaps=True)
        layout = go.Layout(title=f'{merchant_name}: Total Transaction Amount by Month-Year')
        fig = go.Figure(layout=layout)
        fig.add_trace(trace)
        fig.show()
  ```

We can now call our `read_data` function with the name of our file and store the results in a variable called `df`:

`df = read_data("synthetic_transaction_data_Dining.csv")`

Plot the `transaction_amounts` at daily granularity:

`plot_total_amount_by_day(df)`


Also plot the time `transaction_amounts` at monthly granularity:

`merchant_names = list(set(df['merchant_name']))[:5]`

`plot_amount_by_month_year(df, merchant_names)`

The full code block is:

```
def read_data(file_path):
    df = pd.read_csv(file_path)
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])
    df = df[df["transaction_date"] < '2023-06-01']
    return df

def plot_total_amount_by_day(df):
    df_grouped = df.groupby(df['transaction_date'].dt.date)['transaction_amount'].sum().reset_index()
    fig = px.line(df_grouped, x='transaction_date', y='transaction_amount', title='Total Transaction Amount by Day')
    fig.show()

def plot_amount_by_month_year(df, merchant_names):
    for merchant_name in merchant_names:
        subgroup = df[df['merchant_name'] == merchant_name].copy()
        subgroup['month'] = subgroup['transaction_date'].dt.month
        subgroup = subgroup[(subgroup['month'] <= 12) & (subgroup['month'] >= 1)]
        subgroup['month'] = subgroup['month'].astype(str)
        subgroup['year'] = subgroup['transaction_date'].dt.year.astype(str)
        subgroup['month_year'] = pd.to_datetime(subgroup['year'] + "-" + subgroup['month'])
        
        df_grouped = subgroup.groupby('month_year')['transaction_amount'].sum().reset_index()
        df_grouped = df_grouped.set_index('month_year').sort_index()
        
        trace = go.Scatter(x=df_grouped.index, y=df_grouped['transaction_amount'], mode='lines', connectgaps=True)
        layout = go.Layout(title=f'{merchant_name}: Total Transaction Amount by Month-Year')
        fig = go.Figure(layout=layout)
        fig.add_trace(trace)
        fig.show()

df = read_data("synthetic_transaction_data_Dining.csv")

plot_total_amount_by_day(df)

merchant_names = list(set(df['merchant_name']))[:5]

plot_amount_by_month_year(df, merchant_names

```{{execute}}
