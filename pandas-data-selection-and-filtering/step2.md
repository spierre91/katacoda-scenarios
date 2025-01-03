# Selecting Data with Pandas

Next let's select a few columns. Let's select `animal_type`, `color`, and `breed`:


`df_select = df[['animal_type', 'color', 'breed']]`{{execute}}

Now let's print the first five rows:

`print(df_select.head())`{{execute}}

We can also print more than five rows. We can print the first 20 rows:

`print(df_select.head(20))`{{execute}}

Or even the last 20 rows using `tail`:
`print(df_select.tail(20))`{{execute}}

Another thing we can do is engineer a few features from the `date_of_birth` column. First, let's convert `date_of_birth` into a Pandas datetime object:

`df['date_of_birth'] = pd.to_datetime(df['date_of_birth'])`{{execute}}

Let's create a `week` column:

`df['week'] = df['date_of_birth'].dt.isocalendar().week`{{execute}}

Let's print the first five rows to analyze the result:

`print(df.head())`{{execute}}

We can also create `month` and `year` columns:

`df['month'] = df['date_of_birth'].dt.month`{{execute}}

`df['year'] = df['date_of_birth'].dt.year`{{execute}}

`print(df.head())`{{execute}}

Finally, we can select our engineered columns along with an original column, say `sex_upon_outcome`:

`df_select = df[['year', 'month', 'week', 'sex_upon_outcome']]`{{execute}}

`print(df_select.head())`{{execute}}







