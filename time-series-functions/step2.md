# Training ARIMA model 

Next we will define a function, called `data_prep` that prepares our time series data model training:
```
def data_prep(df, merchant_name):
    df_merchant = df[df['merchant_name'] == merchant_name]
    df_merchant['month'] = df_merchant['transaction_date'].dt.month.astype(str)
    df_merchant['year'] = df_merchant['transaction_date'].dt.year.astype(str)
    df_merchant['month_year'] = df_merchant['year'] + "-" + df_merchant['month']
    df_merchant['month_year'] = pd.to_datetime(df_merchant['month_year'])
    df_grouped = df_merchant.groupby('month_year')['transaction_amount'].sum().reset_index()
    df_grouped = df_grouped.set_index('month_year').sort_index()
    return df_grouped
```

We then define a function, called `split_train_test_data` that splits our data for training and testing:

```
def split_train_test_data(df_grouped):
    cutoff_point1 = pd.to_datetime("2023-03-01")
    cutoff_point2 = pd.to_datetime("2023-06-01")
    train_data = df_grouped[df_grouped.index < cutoff_point1]
    test_data = df_grouped[(df_grouped.index >= cutoff_point1) & (df_grouped.index <= cutoff_point2)]
    return train_data, test_data
```

We define a function, called `train_auto_arima_model` that trains our ARIMA model on our training data:

```
def train_auto_arima_model(train_data):
    model = auto_arima(train_data['transaction_amount'])
    return model
```

Next, we define `predict` function that uses our ARIMA model object to generate predictions oon our test data:

```
def predict(model, test_data):
    predictions = model.predict(n_periods=len(test_data))
    return predictions
```

We can then define a function that calculates the root mean square error (RMSE), of our predictions:

```
def calculate_rmse(actual, predicted):
    mse = mean_squared_error(actual, predicted)
    rmse = mse ** 0.5
    return rmse
```


we can then define a merchant we'd like too perform time series analysis on:

`merchant_name = "Domino's Pizza"`

Prepare our data for modeling:

`df_grouped = time_series_analysis(df, merchant_name)`

Split oour data for training and testing:

`train_data, test_data = split_train_test_data(df_grouped)`

Train our ARIMA moodel:

`model = train_auto_arima_model(train_data)` 

Generate predictions:

`predictions = predict(model, test_data)`


Calculate and print RMSE:

`rmse = calculate_rmse(test_data['transaction_amount'], predictions)`

`print('RMSE:', rmse)`

The full codee block is:

```
def time_series_analysis(df, merchant_name):
    df_merchant = df[df['merchant_name'] == merchant_name]
    df_merchant['month'] = df_merchant['transaction_date'].dt.month.astype(str)
    df_merchant['year'] = df_merchant['transaction_date'].dt.year.astype(str)
    df_merchant['month_year'] = df_merchant['year'] + "-" + df_merchant['month']
    df_merchant['month_year'] = pd.to_datetime(df_merchant['month_year'])
    df_grouped = df_merchant.groupby('month_year')['transaction_amount'].sum().reset_index()
    df_grouped = df_grouped.set_index('month_year').sort_index()
    return df_grouped

def split_train_test_data(df_grouped):
    cutoff_point1 = pd.to_datetime("2023-03-01")
    cutoff_point2 = pd.to_datetime("2023-06-01")
    train_data = df_grouped[df_grouped.index < cutoff_point1]
    test_data = df_grouped[(df_grouped.index >= cutoff_point1) & (df_grouped.index <= cutoff_point2)]
    return train_data, test_data

def train_auto_arima_model(train_data):
    model = auto_arima(train_data['transaction_amount'])
    return model

def predict(model, test_data):
    predictions = model.predict(n_periods=len(test_data))
    return predictions

def calculate_rmse(actual, predicted):
    mse = mean_squared_error(actual, predicted)
    rmse = mse ** 0.5
    return rmse

merchant_name = "Domino's Pizza"
df_grouped = time_series_analysis(df, merchant_name)

train_data, test_data = split_train_test_data(df_grouped)

model = train_auto_arima_model(train_data)
predictions = predict(model, test_data)

rmse = calculate_rmse(test_data['transaction_amount'], predictions)
print('RMSE:', rmse)


```{{execute}}
