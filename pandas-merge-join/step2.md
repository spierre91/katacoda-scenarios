# Creating Merge Columns 

To be able to merge our data, let's create year and week columns. First, we need to convert the date columns into pandas datetime objects:

Let's start with the MSFT stock price data. Let's convert the `Date` column into a datetime object:

`df_stock['Date'] = pd.to_datetime(df_stock['Date'])`{{execute}}

`df_stock['Year'] = df_stock['Date'].dt.year`{{execute}}

`df_stock['Week Number'] = df_stock['Date'].dt.week`{{execute}}

Let's print the first five rows:
`print(df_stock.head())`{{execute}}

Next, let's do the same for the `Week` column:
`df_trends['Week'] = pd.to_datetime(df_trends['Week'])`{{execute}}

`df_trends['Year'] = df_trends['Week'].dt.year`{{execute}}

`df_trends['Week Number'] = df_trends['Week'].dt.week`{{execute}}

And we can print the first five rows:
`print(df_trends.head())`{{execute}}
