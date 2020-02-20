# Selecting Data with Pandas

Next let's select a few columns. Let's select `animal_type`, `color`, and `breed`:


`df_select = df[['animal_type', 'color', 'breed']]`{{execute}}

Now let's print the first five rows:

`print(df_select.head())`{{execute}}

We can also print more than five rows. We can print the first 20 rows:

`print(df_select.head(20))`{{execute}}

Or even the last 20 rows using `tail`:
`print(df_select.tail(20))`{{execute}}

We can also select anothher set of columns. Let's select `age_upon_outcome`, `animal_id`,`name`, `date_of_birth`, and `sex_upon_outcome`:


`df_select = df[['age_upon_outcome','animal_id','name', 'date_of_birth', 'sex_upon_outcome']]`{{execute}}

Let's now print the first five rows:

`print(df_select.head())`{{execute}}


Another thing we can do is engineer a few features from the `date_of_birth` column. First, Let's convert `date_of_birth` into a pandas datetime object:

`df_select.loc[:, 'date_of_birth'] = pd.to_datetime(df_select['date_of_birth'])`{{execute}}

Let's create a `week` column:

`df_select.loc[:,'week'] = df_select['date_of_birth'].dt.week`{{execute}}

Let's print the first five rows to analyze the result:

`print(df_select.head())`{{execute}}

We can also create `month` and `year` columns:

`df_select.loc[:,'month'] = df_select['date_of_birth'].dt.month`{{execute}}

`df_select.loc[:,'year'] = df_select['date_of_birth'].dt.year`{{execute}}

`print(df_select.head())`{{execute}}

Finally, we can select our engineered columns and let's select one original column, say `sex_upon_outcome`:

`df_select = df_select[['year', 'month', 'week', 'sex_upon_outcome']]`{{execute}}

`print(df_select.head())`{{execute}}







