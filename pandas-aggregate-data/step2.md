# Resampling AAPL Stock Price Data with Pandas

The first thing we can do is calculate the percent change in a column of our choice. Percent change calculations are often used in finance in order to measure the degree to which the price of an asset increases or decreases.
We can caluctate the percent change of the opening price of the AAPL stock by using the `pct_change()` method in pandas. We can print the first five values of the resulting transformation:

`print(df['Open'].pct_change().head())`{{execute}}

We can do the same for the  high column:

`print(df['High'].pct_change().head())`{{execute}}

and the low:

`print(df['Low'].pct_change().head())`{{execute}}

and finally, the closee:

`print(df['Close'].pct_change().head())`{{execute}}

We can also apply this transformation to all four columns simulataneously

`print(df[["Open", "High", "Low", "Close"]].pct_change().head())`{{execute}}

We can also calculate open to close returns:

`df['Returns'] = ((df['Close']-df['Open'])/df['Open'])*100.0`{{execute}}

Print the ressult data frame:

`print(df.head())`{{execute}}

Finally we can generate percent change in returns:

`print(df['Returns'].pct_change().head())`{{execute}}

