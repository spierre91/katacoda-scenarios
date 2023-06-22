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
