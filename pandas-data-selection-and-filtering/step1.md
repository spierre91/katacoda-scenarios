# Reading Data with Pandas

First let's open up the python interactive shell by ptyping 'python' and pressing enter in the terminal window on the right.

Next let's import the pandas library and rename it as 'pd':

`import pandas as pd`{{execute}}

For our demonstration we will be using the Austin Animal Shelter data set. Let's import the data into a data frame:

`df = pd.read_csv('aac_shelter_outcomes.csv')`{{execute}}

`print(df.head())`{{execute}}



