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
```


`visualizer = TransactionDataVisualizer()`

`visualizer.plot_total_amount_by_day(df_grouped)`

