import pandas as pd
import html5lib


# Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading

url = "http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2"
df = pd.read_html(url)[0]


# Rename the columns so that they match the
# column definitions provided to you on the website
columns = ["RK", "PLAYER", "TEAM", "GP", "G", "A", "PTS", "+/-", "PIM", "PTS/G",
            "SOG", "PCT", "GWG", "PP_G", "PP_A", "SH_G", "SH_A"]

df.columns = columns


# Get rid of any row that has at least 4 NANs in it
df = df.dropna(axis=0, thresh=4)


# At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
df = df.drop_duplicates(subset='PLAYER', keep=False)


# Get rid of the 'RK' column
df = df.drop(labels=['RK'], axis=1)


# Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
df = df.reset_index(drop=True)



# Check the data type of all columns, and ensure those
# that should be numeric are numeric
for i in range(3, len(columns) - 1):
    df[columns[i]] = pd.to_numeric(df[columns[i]], errors='coerce')



# Your dataframe is now ready! Use the appropriate
# commands to answer the questions on the course lab page.
print(df)
print(len(df.PCT.unique()))
print(df.loc[15,"GP"] + df.loc[16,"GP"])
