# Reading Several Files with Pandas
The first thing we need to do is clone the GitHub repo containing the necessary data we will be using. In the terminal on the righthand side copy and paste the following and press enter:
`git clone https://github.com/spierre91/katacoda-scenarios`

Next we need to go into the folder corresponding the the data selection and filtering scenario. Copy and paste the folloing and press enter:
`cd katacoda-scenarios/pandas-concatenate-data/`

Now let's open up the python interactive shell by typing `python` and pressing enter in the terminal window on the right.

Next let's import the pandas library and rename it as 'pd':

`import pandas as pd`{{execute}}

For our demonstration we will be using the four data files. These file correspond to Google search trends for Tesla over the course of 5 years. The data was pulled using the Google Trends API. 

Let's read in each file into their own pandas data frames and print the first five rows. For 2015:

`df_2015 = pd.read_csv('tesla_2015.csv')`{{execute}}

`print(df_2015.head())`{{execute}}







