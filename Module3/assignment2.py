import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
matplotlib.style.use('ggplot')


# Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'

df = pd.read_csv('Datasets/wheat.data')


# Create a 2d scatter plot that graphs the
# area and perimeter features

df.plot.scatter(x = 'area', y = 'perimeter')


# Create a 2d scatter plot that graphs the
# groove and asymmetry features

df.plot.scatter(x = 'groove', y = 'asymmetry')


# Create a 2d scatter plot that graphs the
# compactness and width features

df.plot.scatter(x = 'compactness', y = 'width')


# BONUS:
# After completing the above, go ahead and run your program
# Check out the results, and see what happens when you add
# in the optional display parameter marker with values of
# either '^', '.', or 'o'.

df.plot.scatter(x = 'compactness', y = 'width', marker='^')

plt.show()
