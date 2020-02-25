# Reading Data with Pandas

The first thing we need to do is clone the GitHub repo containing the necessary data we will be using. In the terminal on the righthand side copy and paste the following and press enter:
`git clone https://github.com/spierre91/katacoda-scenarios`

Next we need to go into the folder corresponding to the data selection and filtering scenario. Copy and paste the folloing and press enter:
`cd katacoda-scenarios/pandas-data-selection-and-filtering/`

Next let's open up a python interactive shell. 

Copy and paste `python` in the terminal on the righthand side and press enter. 

Next let's import the pandas library and rename it as 'pd'. You can either copy and paste and press enter or simply click the code below:

`import pandas as pd`{{execute}}

For our demonstration we will be using the Austin Animal Shelter data set. Let's import the data into a data frame:

`df = pd.read_csv('aac_shelter_outcomes.csv')`{{execute}}

`print(df.head())`{{execute}}

We will notice that a few of the columns are hidden. We can show all columns by executing the following:

`pd.set_option('display.max_columns', None)`{{execute}}

`pd.set_option('display.max_rows', None)`{{execute}}

This set's the column and row limits to `None`. Now let's print the first five rows:

`print(df.head())`{{execute}}


