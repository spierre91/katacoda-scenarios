# Reading Data with Pandas
The first thing we need to do is clone the GitHub repo containing the necessary data we will be using:

`git clone https://github.com/spierre91/katacoda-scenarios`{{execute}}

Next we need to go into the folder corresponding to the data summary statistics scenario:
`cd katacoda-scenarios/pandas-summary-statistics`{{execute}}

Now let's open up the python interactive shell: `python`{{execute}}

Next let's import the Pandas library and rename it as 'pd':

`import pandas as pd`{{execute}}

In this post, we will demonstrate how we can use pandas to generate statistics like mean, median, mode, and standard deviation. 

To get started, let's import the data into a Pandas data frame:

`df = pd.read_csv("fifa_19.csv")`{{execute}}

Let's print the first five rows:

`print(df.head())`{{execute}}

We can see that some of the rows are hidden. We can modify this by executing the following:

`pd.set_option('display.max_columns', None)`{{execute}}

`pd.set_option('display.max_rows', None)`{{execute}}

Also, Let's filter the data frame to only include the columns we want:

`df = df[['Name', 'Age', 'Nationality', 'Preferred Foot', 'Height', 'Weight', 'Position', 'Overall']]`{{execute}}

`print(df.head())`{{execute}}


