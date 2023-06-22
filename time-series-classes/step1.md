```
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.seasonal import seasonal_decompose
```


```
class TransactionDataReader:
    @staticmethod
    def read_data(file_path):
        df = pd.read_csv(file_path)
        df["transaction_date"] = pd.to_datetime(df["transaction_date"])
        df = df[df["transaction_date"] < '2023-06-01']
        df['transaction_date'] = pd.to_datetime(df['transaction_date'])
        return df
```

```
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
```


`data_reader = TransactionDataReader()`

`df = data_reader.read_data("synthetic_transaction_data_Dining.csv")`

`analyzer = TransactionDataAnalyzer(df)`
df_grouped = analyzer.group_by_date()
