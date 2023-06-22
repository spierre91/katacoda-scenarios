# Train the AutoARIMA model on the train data

Next let's define an ARIMA model object:

`model = auto_arima(train_data['transaction_amount'])`{{execute}}

Predict on the test data using the trained model:

`predictions = model.predict(n_periods=len(test_data))`{{execute}}

Calculate the RMSE for the predictions:

`mse = mean_squared_error(test_data['transaction_amount'], predictions)`{{execute}}

`rmse = mse ** 0.5`{{execute}}

`print('RMSE:', rmse)`{{execute}}


Plot the training, testing, and predicted values:

`fig = go.Figure()`{{execute}}

`fig.add_trace(go.Scatter(x=train_data.index, y=train_data['transaction_amount'], name='Training'))`{{execute}}

`fig.add_trace(go.Scatter(x=test_data.index, y=test_data['transaction_amount'], name='Testing'))`{{execute}}

`fig.add_trace(go.Scatter(x=test_data.index, y=predictions, name='Predictions'))`{{execute}}

`fig.show()`{{execute}}
    
# Perform Seasonal decomposition

Next let's perform seasonal decomposition to see if we have any seasonal trends in our data:

`from statsmodels.tsa.seasonal import seasonal_decompose`{{execute}}

`result = seasonal_decompose(df_grouped['transaction_amount'], model='additive')`{{execute}}

Next, we can create Plotly traces for each component:

`observed_trace = go.Scatter(x=df_grouped.index, y=result.observed, name='Observed')`{{execute}}

`trend_trace = go.Scatter(x=df_grouped.index, y=result.trend, name='Trend')`{{execute}}

`seasonal_trace = go.Scatter(x=df_grouped.index, y=result.seasonal, name='Seasonal')`{{execute}}

`residual_trace = go.Scatter(x=df_grouped.index, y=result.resid, name='Residual')`{{execute}}

Create a Plotly figure, add the traces and show plot:

`fig = go.Figure(data=[observed_trace, trend_trace, seasonal_trace, residual_trace])`{{execute}}

`fig.update_layout(title='Seasonal Decomposition',
                  xaxis_title='Month Year', yaxis_title='Amount')`{{execute}}

`fig.show()`{{execute}}


