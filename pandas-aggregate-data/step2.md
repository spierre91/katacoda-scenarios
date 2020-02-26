# Resampling AAPL Stock Price Data with Pandas

The first thing we can do is calculate the percent change in a column of our choice. Percent change calculations are often used in finance to measure the degree to which the price of an asset increases or decreases.
We can calculate the percent change of the opening price of the AAPL stock by using the `pct_change()` method in pandas. We can print the first five values of the resulting series:

`print(df['Open'].pct_change().head())`{{execute}}

We can do the same for the high column:

`print(df['High'].pct_change().head())`{{execute}}

and the low:

`print(df['Low'].pct_change().head())`{{execute}}

and finally, the close:

`print(df['Close'].pct_change().head())`{{execute}}

We can also apply this transformation to all four columns simultaneously:

`print(df[["Open", "High", "Low", "Close"]].pct_change().head())`{{execute}}

We can also calculate open to close returns:

`df['Returns'] = ((df['Close']-df['Open'])/df['Open'])*100.0`{{execute}}

Print the resulting data frame:

`print(df.head())`{{execute}}

Finally, we can generate percent change in returns:

`print(df['Returns'].pct_change().head())`{{execute}}

