# Reading AAPL Stock Price Data with Pandas
The first thing we need to do is clone the GitHub repo containing the necessary data we will be using:

`git clone https://github.com/spierre91/katacoda-scenarios`{{execute}}

Next we need to go into the folder corresponding to the data aggregation scenario:
`cd katacoda-scenarios/pandas-aggregate-data`{{execute}}

Now let's open up the python interactive shell: `python`{{execute}}

Next let's import the Pandas library and rename it as 'pd':

`import pandas as pd`{{execute}}

For this demonstration we will be using 'AAPL' stock price data. Let's import the data into a Pandas data frame:

`df = pd.read_csv("AAPL.csv")`{{execute}}

Let's print the first five rows:

`print(df.head())`{{execute}}
