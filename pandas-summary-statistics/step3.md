# Generating Statistics from Categorical Columns

For categorical columns, we can look at the mode. The mode is simply the value that appears most often.  We can calculate this statistic for columns like `Nationality` and `Position`. 


Let's print the mode of the `Nationality` column:
`print("Mode of Nationality: ", df['Nationality'].mode())`{{execute}}


Let's do the same for the `Position` column:
`print("Mode of Position: ", df['Position'].mode())`{{execute}}

And the `Preferred Foot` column:
`print("Mode of Preferred Foot: ", df['Preferred Foot'].mode())`{{execute}}


The last thing we can look at is the distribution in categorical values using the `Counter` method from the `collections` module. Let's import the `Counter` method:

`from collections import Counter`{{execute}}

Let's print the `Counter` output for `Nationality`:

`print(Counter(df['Nationality']))`{{execute}}

We can limit the output to the most common `n` values. Let's print the most common `n=5` values:
`print(Counter(df['Nationality']).most_common(5))`{{execute}}

And we can do the same for `Position`:
`print(Counter(df['Position']).most_common(5))`{{execute}}

And `Preferred Foot`:
`print(Counter(df['Preferred Foot']).most_common(5))`{{execute}}


