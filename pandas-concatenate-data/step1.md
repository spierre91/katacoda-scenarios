# Reading Several Files with Pandas
The first thing we need to do is clone the GitHub repo containing the necessary data we will be using. In the terminal on the righthand side copy and paste the following and press enter:
`git clone https://github.com/spierre91/katacoda-scenarios`

Next we need to go into the folder corresponding to the concatenate data scenario. Copy and paste the following and press enter:
`cd katacoda-scenarios/pandas-concatenate-data/`

Now let's open up the python interactive shell by typing `python` and pressing enter in the terminal window on the right.

Next let's import the Pandas library and rename it as 'pd':

`import pandas as pd`{{execute}}

For our demonstration we will be using the four data files. These files correspond to Google search trends for Tesla (2015-2018). The data was pulled using the Google Trends API. 

Let's read in each file into their own Pandas data frames and print the first five rows. For 2015:

`df_2015 = pd.read_csv('tesla_2015.csv')`{{execute}}

`print(df_2015.head())`{{execute}}

We see that we have an unnamed column. We can remove that with the following:

`del df_2015['Unnamed: 0']`{{execute}}

`print(df_2015.head())`{{execute}}

Let's repeat this for 2016, 2017, 2018, and 2019:

For 2016:

`df_2016 = pd.read_csv('tesla_2016.csv')`{{execute}}

`print(df_2016.head())`{{execute}}

`del df_2016['Unnamed: 0']`{{execute}}

`print(df_2016.head())`{{execute}}


For 2017:

`df_2017 = pd.read_csv('tesla_2017.csv')`{{execute}}

`print(df_2017.head())`{{execute}}

`del df_2017['Unnamed: 0']`{{execute}}

`print(df_2017.head())`{{execute}}


And finally, for 2018:

`df_2018 = pd.read_csv('tesla_2018.csv')`{{execute}}

`print(df_2018.head())`{{execute}}

`del df_2018['Unnamed: 0']`{{execute}}

`print(df_2018.head())`{{execute}}


