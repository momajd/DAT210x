import pandas as pd

# Load up the dataset
# Ensuring you set the appropriate header column names
#
names = ['motor', 'screw', 'pgain', 'vgain', 'class']
table = pd.read_csv('Datasets/servo.data', names = names)


# Create a slice that contains all entries
# having a vgain equal to 5. Then print the
# length of (# of samples in) that slice:
#
sliced = table.loc[table['vgain'] == 5]
print(len(sliced))

# Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
sliced = table.loc[(table['motor'] == 'E') & (table['screw'] == 'E')]
print(len(sliced))


# Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
mean = table.loc[table['pgain'] == 4].mean()
print(mean)


# (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
table.dtypes
