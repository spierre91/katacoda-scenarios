# Writing Concatenated Files to CSV with Pandas

For this lasst step will will write the `combined_df` to a new CSV file. To do this we use the `to_csv()` method in pandas:

`combined_df.to_csv("combined_tesla_files.csv")`{{execute}}


We can now read in the combined file into a data frame:

`df = pd.read_csv("combined_tesla_files.csv")`{{execute}}


and let's print the first five rows:

`print(df.head())`{{execute}}


