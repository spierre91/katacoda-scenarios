# Reading Microsoft (MSFT) Stock Price Data and Google Trends Data with Pandas
The first thing we need to do is clone the GitHub repo containing the necessary data we will be using. In the terminal on the righthand side copy and paste the following and press enter:
`git clone https://github.com/spierre91/katacoda-scenarios`

Next we need to go into the folder corresponding to the merge/join scenario. Copy and paste the folloing and press enter:
`cd katacoda-scenarios/pandas-merge-join`

Now let's open up the python interactive shell by typing `python` and pressing enter in the terminal window on the right.

Next let's import the pandas library and rename it as 'pd':

`import pandas as pd`{{execute}}

In this example we will be combining MSFT stock price and google trends data using pandas. Combining data is often neccessary when you have data stored in multiple files, worksheets or data tables. In my expeerience, combining data has been an important part of sourcing useful signals for buidling predictive models.

Let's read the MSFT stock prices into a pandas data frame:
`df_stock = pd.read_csv("msft_stock_price.csv")`{{execute}}

Let's print the first five rows:
`print(df_stock.head())`{{execute}}

Let's also read the google trends data into a pandas data frame

`df_trends = pd.read_csv("msft_google_trends.csv")`{{execute}}

Let's print the first five rows:
`print(df_trends.head())`{{execute}}
