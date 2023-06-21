# Train the AutoARIMA model on the train data
model = auto_arima(train_data['transaction_amount'])

# Predict on the test data using the trained model
predictions = model.predict(n_periods=len(test_data))

# Calculate the RMSE for the predictions
mse = mean_squared_error(test_data['transaction_amount'], predictions)
rmse = mse ** 0.5
print('RMSE:', rmse)

# Plot the training, testing, and predicted values
fig = go.Figure()
fig.add_trace(go.Scatter(x=train_data.index, y=train_data['transaction_amount'], name='Training'))
fig.add_trace(go.Scatter(x=test_data.index, y=test_data['transaction_amount'], name='Testing'))
fig.add_trace(go.Scatter(x=test_data.index, y=predictions, name='Predictions'))
fig.show()
    
    
from statsmodels.tsa.seasonal import seasonal_decompose

result = seasonal_decompose(df_grouped['transaction_amount'], model='additive')

# Create Plotly traces for each component
observed_trace = go.Scatter(x=df_grouped.index, y=result.observed, name='Observed')
trend_trace = go.Scatter(x=df_grouped.index, y=result.trend, name='Trend')
seasonal_trace = go.Scatter(x=df_grouped.index, y=result.seasonal, name='Seasonal')
residual_trace = go.Scatter(x=df_grouped.index, y=result.resid, name='Residual')

# Create a Plotly figure and add the traces
fig = go.Figure(data=[observed_trace, trend_trace, seasonal_trace, residual_trace])
fig.update_layout(title='Seasonal Decomposition',
                  xaxis_title='Month Year', yaxis_title='Amount')

# Show the Plotly figure
fig.show()  


