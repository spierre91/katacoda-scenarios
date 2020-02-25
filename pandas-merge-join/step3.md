#Merging and Joining Data

First we will merge both data sets on the `Year` and `Week Number` columns we created:


`df = pd.merge(df_stock, df_trends, on = ['Year', 'Week Number'])`{{execute}}

Let's print the first five rows of the merged data set:

`print(df.head())`{{execute}}

