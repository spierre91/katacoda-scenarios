# Concatenating Files with Pandas

First let's define a list of data frames:

`li = [df_2015, df_2016, df_2017, df_2018]`{{execute}}

Next we use the `concat()` method provided by pandas:

`combined_df = pd.concat(li, axis=0, ignore_index=True)`{{execute}}

Let's print the first five rows:

`print(combined_df.head())`{{execute}}

For a sanity check, let's convert the 'Week' column into a Pandas datetime object, create a year column and print the unique set of years:


`combined_df['datetime'] = pd.to_datetime(combined_df['Week'])`{{execute}}

`combined_df['year'] = combined_df['datetime'].dt.year`{{execute}}


`print(set(combined_df['year'].values))`{{execute}}

