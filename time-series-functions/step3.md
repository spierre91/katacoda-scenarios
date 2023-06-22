# Ploting predictions and visualizing seasonality 

Next we will define a function that visualizes the training, testing and predicition data:

```
def plot_training_testing_predictions(train_data, test_data, predictions):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=train_data.index, y=train_data['transaction_amount'], name='Training'))
    fig.add_trace(go.Scatter(x=test_data.index, y=test_data['transaction_amount'], name='Testing'))
    fig.add_trace(go.Scatter(x=test_data.index, y=predictions, name='Predictions'))
    fig.show()
```

We will also define a function that allows us to visualize seasonality:

```
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

We call our `plot_training_testing_predictions` with our taining data, test data and predictions:

`plot_training_testing_predictions(train_data, test_data, predictions)`{{execute}}

And call the `perform_seasonal_decomposition` with our aggregated data:

`perform_seasonal_decomposition(df_grouped)`{{execute}}
