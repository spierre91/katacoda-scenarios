#Merging Data on Columns

To be able to merge our data, let's create year and week columns. First, we need to convert the date columns into pandas datetime objects:

Let's start with the MSFT stock price data. Let'ss convert the `Date` column into a datetime object:

`df_stock['Date'] = pd.to_datetime(df_stock['Date'])`{{execute}}

`df_stock['Year'] = df_stock['Date'].dt.year`{{execute}}

`df_stock['Week Number'] = df_stock['Date'].dt.week`{{execute}}

Next, let's do the same for the `Week` column:
`df_trends['Week'] = pd.to_datetime(df_trends['Week'])`{{execute}}

`df_trends['Year'] = df_trends['Date'].dt.year`{{execute}}

`df_trends['Week Number'] = df_trends['Date'].dt.week`{{execute}}
