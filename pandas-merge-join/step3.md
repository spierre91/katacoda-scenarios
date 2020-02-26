# Merging and Joining Data 

First, we will merge both data sets on the `Year` and `Week Number` columns we created:


`df = pd.merge(df_stock, df_trends, on = ['Year', 'Week Number'])`{{execute}}

Let's print the first five rows of the merged data set:

`print(df.head())`{{execute}}

We can expand the columns using the following:

`pd.set_option('display.max_columns', None)`{{execute}}

And print the first five rows:

`print(df.head())`{{execute}}


Next we will take a look at `join()`. Join is used when you want to combine two data frames with different indices. 
For example, let's set the index of the stock price data frame to be the `Date`:

`df_stock.set_index('Year', inplace = True)`{{execute}}

Let's print the first five rows to see the results:
`print(df_stock.head())`{{execute}}


Let's print the first five rows of the google trends data:
`print(df_trends.head())`{{execute}}


We can see that the indices of both data frames are different. 


We can join the data frame by executing the following:
`df = df_stock.join(df_trends, on = 'Year', lsuffix='_left', rsuffix='_right')`{{execute}}

Let's print the first five rows:
`print(df.head())`{{execute}}

In general, using the `merge()` method is more convenient than the `join()` method. This is because there are more restrictions on performing joins. 




