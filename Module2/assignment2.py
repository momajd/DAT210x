import pandas as pd

# Load up the 'tutorial.csv' dataset
data = pd.read_csv('Datasets/tutorial.csv')

# Print the results of the .describe() method
print(data.describe())

# Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
print(data.loc[ 2:4, ['col3']])
