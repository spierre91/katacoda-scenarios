# Generating statistics from Numerical Variables

We can calcualte statical values like mean, maximum, minimum and standard deviation for any of the numerical columns. An issue here is that some of the numerical columns that may be of interest to us are string which we can't perform useful calculations on. 
Let's transform the height values into centimeters and the weight into kilograms:

To convert the height we execute the following block of code:

```
Height_cm = []
for i in list(df['Height'].values):
    try:
        Height_cm.append((float(str(i)[0])*12.0 + float(str(i)[2:]))*2.54)
    except(ValueError):
        Height_cm.append(np.nan)
        
df['Height_cm'] = Height_cm
```{{execute}}


To conver the weight we execute the following:
`df['Weight_kg'] = df['Weight'].str[:3].astype(float)/2.20462`{{execute}}


Let's calculate the mean `Height` of all the soccer players:

`print("Mean Height: ", df['Height'].mean())`{{execute}}
