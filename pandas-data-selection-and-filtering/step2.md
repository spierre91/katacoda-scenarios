#Selecting Columns Using Pandas

Next let's select a few columns. Let's select `animal_type`, `color`, and `breed`:
`df_select = df[['animal_type', 'color', 'breed']]`{{execute}}

Now let's print the first five rows:
`print(df_select.head())`{{execute}}

We can also print more than five rows. We can print the first 20 rows:

`print(df_select.head(20))`{{execute}}

Or even the last 20 rows using `tail`:
`printdf_select.tail(20))`{{execute}}
