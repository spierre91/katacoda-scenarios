# Reading AAPL Stock Price Data with Pandas
The first thing we need to do is clone the GitHub repo containing the necessary data we will be using. In the terminal on the right-hand side copy and paste the following and press enter:
`git clone https://github.com/spierre91/katacoda-scenarios`

`python clonee_repo.py`{{execute}}

Next we need to go into the folder corresponding to the data aggregation scenario. Copy and paste the following and press enter:
`cd katacoda-scenarios/pandas-aggregate-data`

Now let's open up the python interactive shell by typing `python` and pressing enter in the terminal window on the right.

Next let's import the Pandas library and rename it as 'pd':

`import pandas as pd`{{execute}}

For this demonstration we will be using 'AAPL' stock price data. Let's import the data into a Pandas data frame:

`df = pd.read_csv("AAPL.csv")`{{execute}}

Let's print the first five rows:

`print(df.head())`{{execute}}
