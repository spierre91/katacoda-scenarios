# Generating Statistics from Numerical Columns

We can calculate statistical values like mean, maximum, minimum and standard deviation for any of the numerical columns. 


Most readers will be familiar with the statistical mean but as a reminder it is the sum of all the numerical values divided by the number of values. In short, it represents the central value of a discrete set of numbers. Let's print the mean `height` of all soccer players:

`print("Mean Height (cm): ", df['Height'].mean())`{{execute}}

Let's print the mean `Weight`:


`print("Mean Weight (kg): ", df['Weight'].mean())`{{execute}}

We can also look at the standard deviation. The standard deviation measures the amount of dispersion in the values of a numerical column in a data set.  Let's print the standard deviation in `Height`:


`print("Standard Deviation Height (cm): ", df['Height'].std())`{{execute}}

And `Weight`:

`print("Standard Deviation Weight (kg): ", df['Weight'].std())`{{execute}}


Next, let's print the minimum and maximum values of `Height`:


`print("Minimum Height (cm): ", df['Height'].min())`{{execute}}


`print("Maximum Height (cm): ", df['Height'].max())`{{execute}}


And `Weight`:

`print("Minimum Weight (kg): ", df['Weight'].min())`{{execute}}


`print("Maximum Weight (kg): ", df['Weight'].max())`{{execute}}



