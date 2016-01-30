Building a Recommender System using Collaborative Filtering(CF)

Collaborative Filtering in simple terms -
At first, people rate different items (like videos, images, games). After that, the system is making predictions about user's rating for an item, which the user hasn't rated yet. These predictions are built upon the existing ratings of other users, who have similar ratings with the active user.

Other approaches of building recommender systems -
Content Based Recommenders, Matrix Factorization.

Tips -
- Matrix Factorization doesn't work if data sets are large, CF perfoms better in these scenarios.
- Content based approach require content that can be encoded as meaningful features. At the same time it doesn't face the problem of cold start and popularity bias. there is a risk of overfitting, if for a user data points are less.

Limitations of CF -
- Cold Start: There needs to be enough users already in the system to find a match. New Items need to get enough ratings. clustering might help to solve cold start. 
- Popularity Bias: hard to recommend item to someone with unique tastes. (Tends to recommend popular items, item from the tail do not get so much data) This can be addressed with some advanced approches of handling bias.

1. 
Based on http://www.salemmarafi.com/code/collaborative-filtering-with-python/

Using Last.fm data which have - users, age, gender, artists they have listened to.

