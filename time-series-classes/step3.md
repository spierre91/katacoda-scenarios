# Defining a class for training our ARIMA model and visualizing predictions 

Let's define a new class call `TransactionModelTrainer` and a `@staticmethod` called `split_train_test_data` that allows us to split our  data for training and testing:

```
class TransactionModelTrainer:
    @staticmethod
    def split_train_test_data(df_grouped):
        cutoff_point1 = pd.to_datetime("2023-03-01")
        cutoff_point2 = pd.to_datetime("2023-06-01")
        train_data = df_grouped[df_grouped.index < cutoff_point1]
        test_data = df_grouped[(df_grouped.index >= cutoff_point1) & (df_grouped.index <= cutoff_point2)]
        return train_data, test_data
```

Next let's define another `@staticmethod` called `train_auto_arima_model` that trains our ARIMA model on our training data:

```
class TransactionModelTrainer:
    #... code truncated for clarity
    @staticmethod
    def train_auto_arima_model(train_data):
        model = auto_arima(train_data['transaction_amount'])
        return model
```

We can then define a `@staticmethod` called `predict` that allow us to generate predictions on our test data:

```
class TransactionModelTrainer:
    #... code truncated for clarity
    @staticmethod
    def predict(model, test_data):
        predictions = model.predict(n_periods=len(test_data))
        return predictions
```

Finally, we can define a `@staticmethod` called `calculate_rmse` that allows us to calculate the RMSE of our predictions:

```
class TransactionModelTrainer:
    #... code truncated for clarity
    @staticmethod
    def calculate_rmse(actual, predicted):
        mse = mean_squared_error(actual, predicted)
        rmse = mse ** 0.5
        return rmse
```


We can define an intance of our `TransactionModelTrainer` class:

`trainer = TransactionModelTrainer()`

We'll also specify the merchant we plan to model:

`merchant_name = "Domino's Pizza"`

Split our data for traiining and testing:

`train_data, test_data = trainer.split_train_test_data(analyzer.group_by_month_year(merchant_name))`

Train our ARIMA model:

`model = trainer.train_auto_arima_model(train_data)`

Generate predictions on our test set:

`predictions = trainer.predict(model, test_data)`

Calculate and print RMSE:

`rmse = trainer.calculate_rmse(test_data['transaction_amount'], predictions)`


`print('RMSE:', rmse)`


`visualizer.plot_training_testing_predictions(train_data, test_data, predictions)`

`visualizer.perform_seasonal_decomposition(analyzer.group_by_month_year(merchant_name))`

