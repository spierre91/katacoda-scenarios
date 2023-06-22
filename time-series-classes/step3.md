```
class TransactionModelTrainer:
    @staticmethod
    def split_train_test_data(df_grouped):
        cutoff_point1 = pd.to_datetime("2023-03-01")
        cutoff_point2 = pd.to_datetime("2023-06-01")
        train_data = df_grouped[df_grouped.index < cutoff_point1]
        test_data = df_grouped[(df_grouped.index >= cutoff_point1) & (df_grouped.index <= cutoff_point2)]
        return train_data, test_data

    @staticmethod
    def train_auto_arima_model(train_data):
        model = auto_arima(train_data['transaction_amount'])
        return model

    @staticmethod
    def predict(model, test_data):
        predictions = model.predict(n_periods=len(test_data))
        return predictions

    @staticmethod
    def calculate_rmse(actual, predicted):
        mse = mean_squared_error(actual, predicted)
        rmse = mse ** 0.5
        return rmse
```

merchant_names = list(set(df['merchant_name']))[:5]
for merchant_name in merchant_names:
    df_grouped = analyzer.group_by_month_year(merchant_name)
    visualizer.plot_amount_by_month_year(df_grouped, merchant_name)

`trainer = TransactionModelTrainer()`

`merchant_name = "Domino's Pizza"`

`train_data, test_data = trainer.split_train_test_data(analyzer.group_by_month_year(merchant_name))`

`model = trainer.train_auto_arima_model(train_data)`

`predictions = trainer.predict(model, test_data)`

`rmse = trainer.calculate_rmse(test_data['transaction_amount'], predictions)`

`print('RMSE:', rmse)`


`visualizer.plot_training_testing_predictions(train_data, test_data, predictions)`

`visualizer.perform_seasonal_decomposition(analyzer.group_by_month_year(merchant_name))`

