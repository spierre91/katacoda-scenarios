# Filtering Data with Pandas

Finally, we will walk through how to filter data with pandas. Let's continue working with the `df_select` data frame we created. 
First, let's consider filtering our data by `year`. To get a good idea of the values of `year` in the data we can print the unique set of `year` values by executing the following:

`print(set(df_select['year'].values))`{{execute}}

If we want to filter the data frame to only include data before `2010` we do the following

`df_select = df_select[df_select['year'] < 2010]`{{execute}}

To ensure that our filtering worked we can print the unique set of `year` values once again:

`print(set(df_select['year'].values))`{{execute}}

We can also filter by categorical values. In our current data frame, we have the `sex_upon_outcome` column which contains categorical values. Let's print the unique set of values for `sex_upon_outcome`.

`print(set(df_select['sex_upon_outcome'].values))`{{execute}}

Let's define a new data frame called `df_select_new`. This will be defined as the `df_select` data frame filtered to only inclue `sex_upon_outcome == 'intact Male'`

`df_select_new = df_select[df_select['sex_upon_outcome'] == 'Intact Male']`{{execute}}

If we print the unique set of `sex_upon_outcome` values we have:
`print(set(df_select_new['sex_upon_outcome'].values))`{{execute}}

We can also filter based on a list of categorical values. If we only want `sex_upon_outcome =='Intact Male'` or `sex_upon_outcome =='Spayed Female'`:

`df_select_new = df_select[df_select['sex_upon_outcome'].isin(['Spayed Female', 'Intact Male'])]`{{execute}}

And printing the unique set:
`print(set(df_select_new['sex_upon_outcome'].values))`{{execute}}

verifies the result.



