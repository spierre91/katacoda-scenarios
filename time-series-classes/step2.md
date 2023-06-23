# Defining a class for time series data visualization

Let's proceed by defining a class called `TransactionDataVisualizer` and a `@staticmethod` called  `plot_total_amount_by_day` that we will use to plot daily transactions over time:

```
class TransactionDataVisualizer:
    @staticmethod
    def plot_total_amount_by_day(df_grouped):
        fig = px.line(df_grouped, x='transaction_date', y='transaction_amount', title='Total Transaction Amount by Day')
        fig.show()
```

Next let's define a `@staticmethod` called `plot_amount_by_month_year` that performs a groupby sum on `transaction_amount` by `month_year` and plots a time seriees line plot:

```
class TransactionDataVisualizer:
    #... code truncated for clarity
    @staticmethod
    def plot_amount_by_month_year(df_grouped, merchant_name):
        trace = go.Scatter(x=df_grouped.index, y=df_grouped['transaction_amount'], mode='lines', connectgaps=True)
        layout = go.Layout(title=f'{merchant_name}: Total Transaction Amount by Month-Year')
        fig = go.Figure(layout=layout)
        fig.add_trace(trace)
        fig.show()
```

We will also define a `@staticmethod` called `plot_training_testing_predictions` which wiill plot the training, testing and prediction data:

```
class TransactionDataVisualizer:
    #... code truncated for clarity
    @staticmethod
    def plot_training_testing_predictions(train_data, test_data, predictions):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=train_data.index, y=train_data['transaction_amount'], name='Training'))
        fig.add_trace(go.Scatter(x=test_data.index, y=test_data['transaction_amount'], name='Testing'))
        fig.add_trace(go.Scatter(x=test_data.index, y=predictions, name='Predictions'))
        fig.show()
```
 
Finally, let's define a `@staticmethod` called `perform_seasonal_decomposition` that performs seasonal decomposition and allows us to visualize seasonal trends:

```
class TransactionDataVisualizer:
    #... code truncated for clarity
    @staticmethod
    def perform_seasonal_decomposition(df_grouped):
        result = seasonal_decompose(df_grouped['transaction_amount'], model='additive')
        observed_trace = go.Scatter(x=df_grouped.index, y=result.observed, name='Observed')
        trend_trace = go.Scatter(x=df_grouped.index, y=result.trend, name='Trend')
        seasonal_trace = go.Scatter(x=df_grouped.index, y=result.seasonal, name='Seasonal')
        residual_trace = go.Scatter(x=df_grouped.index, y=result.resid, name='Residual')
        fig = go.Figure(data=[observed_trace, trend_trace, seasonal_trace, residual_trace])
        fig.update_layout(title='Seasonal Decomposition', xaxis_title='Month Year', yaxis_title='Amount')
        fig.show()
```

We can define an instance of our class:

`visualizer = TransactionDataVisualizer()`

And plot the daily transactions:

`visualizer.plot_total_amount_by_day(df_grouped)`

Let's define a list of merchants:

`merchant_names = list(set(df['merchant_name']))[:5]`

And a for-loop over the merchant list that performs a monht_year group by on the `transaction_amoount` and plots the aggregated time series:

```
for merchant_name in merchant_names:
    df_grouped = analyzer.group_by_month_year(merchant_name)
    visualizer.plot_amount_by_month_year(df_grouped, merchant_name)
```


The full code block is:

```
class TransactionDataVisualizer:
    @staticmethod
    def plot_total_amount_by_day(df_grouped):
        fig = px.line(df_grouped, x='transaction_date', y='transaction_amount', title='Total Transaction Amount by Day')
        fig.show()

    @staticmethod
    def plot_amount_by_month_year(df_grouped, merchant_name):
        trace = go.Scatter(x=df_grouped.index, y=df_grouped['transaction_amount'], mode='lines', connectgaps=True)
        layout = go.Layout(title=f'{merchant_name}: Total Transaction Amount by Month-Year')
        fig = go.Figure(layout=layout)
        fig.add_trace(trace)
        fig.show()

    @staticmethod
    def plot_training_testing_predictions(train_data, test_data, predictions):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=train_data.index, y=train_data['transaction_amount'], name='Training'))
        fig.add_trace(go.Scatter(x=test_data.index, y=test_data['transaction_amount'], name='Testing'))
        fig.add_trace(go.Scatter(x=test_data.index, y=predictions, name='Predictions'))
        fig.show()

    @staticmethod
    def perform_seasonal_decomposition(df_grouped):
        result = seasonal_decompose(df_grouped['transaction_amount'], model='additive')
        observed_trace = go.Scatter(x=df_grouped.index, y=result.observed, name='Observed')
        trend_trace = go.Scatter(x=df_grouped.index, y=result.trend, name='Trend')
        seasonal_trace = go.Scatter(x=df_grouped.index, y=result.seasonal, name='Seasonal')
        residual_trace = go.Scatter(x=df_grouped.index, y=result.resid, name='Residual')
        fig = go.Figure(data=[observed_trace, trend_trace, seasonal_trace, residual_trace])
        fig.update_layout(title='Seasonal Decomposition', xaxis_title='Month Year', yaxis_title='Amount')
        fig.show()


visualizer = TransactionDataVisualizer()
visualizer.plot_total_amount_by_day(df_grouped)

merchant_names = list(set(df['merchant_name']))[:5]

for merchant_name in merchant_names:
    df_grouped = analyzer.group_by_month_year(merchant_name)
    visualizer.plot_amount_by_month_year(df_grouped, merchant_name)


```{{execute}}

