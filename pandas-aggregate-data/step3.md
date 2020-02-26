# Calculating Pairwise Covariance, Cumulative Sum, and Rolling Mean

Finally, we can calculate the pairwise covariance for the series in the Pandas data frame. This will return a covariance matrix corresponding to the columns in the data frame. Covariance calculations help us analyze the direction of the linear relationship between two variables. To calculate pairwise covariance, we do the following:

`print(df.cov().head())`{{execute}}

Another statistical metric we can look at is correlation. Correlation helps us measure both the direction and strength of the linear relationship between two variables. We calculate correlation by executing the following:

`print(df.corr().head())`{{execute}}

We can also look at the cumulative sum. This allows us to analyze the total contribution of a given variable, usually against time. Let's calculate the cumulative sum for the `Open` column:
`print(df['Open'].cumsum().head())`{{execute}}

Finally, we can calculate the rolling mean. Rolling mean is typically used to smooth out noise in time series data and reveal long-term trends in the data. Let's calculate the rolling mean, for the `Open` column, with a window size of 5:
`print(df['Open'].rolling(window = 5).mean().head(20))`{{execute}}

We can play around with the window size. Let's try a window size of 10:
`print(df['Open'].rolling(window = 10).mean().head(20))`{{execute}}
