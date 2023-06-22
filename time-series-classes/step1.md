# Defining classes for reading and preparing our time series data:

Let's start by importing the necessary packages:

```
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.seasonal import seasonal_decompose
```

We can then define a class called `TransactionDataReader` that allows us to read in our data. Here we define a static method using the `@` character to define our `TransactionDataReader` method `read_data`. Static methods are nice because they can be used without having access to a class instance or its attributes: 

```
class TransactionDataReader:
    @staticmethod
    def read_data(file_path):
        df = pd.read_csv(file_path)
        df["transaction_date"] = pd.to_datetime(df["transaction_date"])
        df = df[df["transaction_date"] < '2023-06-01']
        return df
```

Next we can define a class, called `TransactionDataPrep` that allows us to perform some simple data preparation. The class will have an `init` method that defines a class attribute that stores our dataframe. 
```
class TransactionDataAnalyzer:
    #... code truncated for clarity 
    def __init__(self, df):
        self.df = df
```

We then define a `group_by_date` method that performs a groupby sum on `transaction_amount` by `transaction_date`:
```
class TransactionDataPrep:
    #... code truncated for clarity 
    def group_by_date(self):
        df_grouped = self.df.groupby(self.df['transaction_date'].dt.date)['transaction_amount'].sum().reset_index()
        return df_grouped
```

Next,  we define a `group_by_month_year` method that performs a groupby sum on `transaction_amount` by `month_year`:
```
class TransactionDataAnalyzer:
    #... code truncated for clarity 
    def group_by_month_year(self, merchant_name):
        subgroup = self.df[self.df['merchant_name'] == merchant_name].copy()
        subgroup['month'] = subgroup['transaction_date'].dt.month
        subgroup = subgroup[(subgroup['month'] <= 12) & (subgroup['month'] >= 1)]
        subgroup['month'] = subgroup['month'].astype(str)
        subgroup['year'] = subgroup['transaction_date'].dt.year.astype(str)
        subgroup['month_year'] = pd.to_datetime(subgroup['year'] + "-" + subgroup['month'])
        df_grouped = subgroup.groupby('month_year')['transaction_amount'].sum().reset_index()
        df_grouped = df_grouped.set_index('month_year').sort_index()
        return df_grouped
```

We read in our data:

`data_reader = TransactionDataReader()`

`df = data_reader.read_data("synthetic_transaction_data_Dining.csv")`

Define our merchant:

`merchant_name = "Domino's Pizza"`

Store and instance of `TransactionDataAnalyzer` in a variable called `TransactionDataAnalyzer`:

`preparer = TransactionDataAnalyzer(df)`

And call our `group_by_month_year` on our `preparer` object:

`df_grouped = preparer.group_by_month_year(merchant_name)`

The full code block is:

```
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.seasonal import seasonal_decompose


class TransactionDataReader:
    @staticmethod
    def read_data(file_path):
        df = pd.read_csv(file_path)
        df["transaction_date"] = pd.to_datetime(df["transaction_date"])
        df = df[df["transaction_date"] < '2023-06-01']
        df['transaction_date'] = pd.to_datetime(df['transaction_date'])
        return df


class TransactionDataAnalyzer:
    def __init__(self, df):
        self.df = df

    def group_by_date(self):
        df_grouped = self.df.groupby(self.df['transaction_date'].dt.date)['transaction_amount'].sum().reset_index()
        return df_grouped

    def group_by_month_year(self, merchant_name):
        subgroup = self.df[self.df['merchant_name'] == merchant_name].copy()
        subgroup['month'] = subgroup['transaction_date'].dt.month
        subgroup = subgroup[(subgroup['month'] <= 12) & (subgroup['month'] >= 1)]
        subgroup['month'] = subgroup['month'].astype(str)
        subgroup['year'] = subgroup['transaction_date'].dt.year.astype(str)
        subgroup['month_year'] = pd.to_datetime(subgroup['year'] + "-" + subgroup['month'])
        df_grouped = subgroup.groupby('month_year')['transaction_amount'].sum().reset_index()
        df_grouped = df_grouped.set_index('month_year').sort_index()
        return df_grouped

data_reader = TransactionDataReader()
df = data_reader.read_data("synthetic_transaction_data_Dining.csv")
merchant_name = "Domino's Pizza"

preparer = TransactionDataAnalyzer(df)
df_grouped = preparer.group_by_month_year(merchant_name)

```{{execute}}

