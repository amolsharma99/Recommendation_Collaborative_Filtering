import pandas as pd
from scipy.spatial.distance import cosine
from tqdm import *

data = pd.read_csv('data.csv')

#user is not needed for item based collaborative filtering
data = data.drop('user', 1)

# Create a placeholder dataframe listing item vs. item
data_ibs = pd.DataFrame(index=data.columns, columns=data.columns)

#using scipy's cosine to fit similarities between items.

# Lets fill in those empty spaces with cosine similarities
# Loop through the columns
for i in tqdm(range(0,len(data_ibs.columns))) :
    # Loop through the columns for each column
    for j in range(0,len(data_ibs.columns)) :
      # Fill in placeholder with cosine similarities
      data_ibs.ix[i,j] = 1-cosine(data.ix[:,i], data.ix[:,j])


# Create a placeholder items for closes neighbours to an item
data_neighbours = pd.DataFrame(index=data_ibs.columns, columns=range(1,11))

# Loop through our similarity dataframe and fill in neighbouring item names
for i in tqdm(range(0,len(data_ibs.columns))):
    data_neighbours.ix[i,:10] = data_ibs.ix[0:,i].order(ascending=False)[:10].index

print data_neighbours.head(6).ix[:6,2:4]

