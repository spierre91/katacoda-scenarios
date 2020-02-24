# Generating Statistics from Categorical Columns

For categorical columns, we can look at the mode. The mode is simply the value that appears most often.  We can calculate this statistic for columns like `Nationality` and and `Position`. 


Let's print the mode of the `Nationality` column:
`print("Mode of Nationality: ", df['Nationality'].mode())`{{execute}}


Let's do the same for the `Position` column:
`print("Mode of Position: ", df['Position'].mode())`{{execute}}

And the `Preferred Foot` column:
`print("Mode of Preferred Foot: ", df['Preferred Foot'].mode())`{{execute}}
