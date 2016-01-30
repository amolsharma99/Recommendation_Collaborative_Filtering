import pandas as pd
from scipy.spatial.distance import cosine
from tqdm import *
import collaborative_filtering_item_based
from collaborative_filtering_item_based import data_neighbours, data_germany, data, data_ibs

'''
Approach User based CF
Have an Item Based similarity matrix at your disposal (in collaborative_filtering.py)
Check which items the user has consumed
For each item the user has consumed, get the top X neighbours
Get the consumption record of the user for each neighbour.
Calculate a similarity score using some formula
Recommend the items with the highest score
'''

data = pd.read_csv('data.csv')

# Helper function to get similarity scores
def getScore(history, similarities):
   return sum(history*similarities)/sum(similarities)


# Create a place holder matrix for similarities, and fill in the user name column
data_sims = pd.DataFrame(index=data.index,columns=data.columns)
data_sims.ix[:,:1] = data.ix[:,:1]

#Loop through all rows, skip the user column, and fill with similarity scores
for i in tqdm(range(0,len(data_sims.index))):
    for j in range(1,len(data_sims.columns)):
        user = data_sims.index[i]
        product = data_sims.columns[j]
 
        if data.ix[i][j] == 1:
            data_sims.ix[i][j] = 0
        else:
            product_top_names = data_neighbours.ix[product][1:10]
            product_top_sims = data_ibs.ix[product].order(ascending=False)[1:10]
            user_purchases = data_germany.ix[user,product_top_names]
 
            data_sims.ix[i][j] = getScore(user_purchases,product_top_sims)

# Get the top songs
data_recommend = pd.DataFrame(index=data_sims.index, columns=['user','1','2','3','4','5','6'])
data_recommend.ix[0:,0] = data_sims.ix[:,0]

# Instead of top song scores, we want to see names
for i in range(0,len(data_sims.index)):
    data_recommend.ix[i,1:] = data_sims.ix[i,:].order(ascending=False).ix[1:7,].index.transpose()

print data_recommend.ix[:10,:4]
