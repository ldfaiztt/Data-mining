1) This is a table of 1-5 star ratings for five movies (M, N, P. Q. R) by three raters (A, B, C):

![movieRating.jpeg](https://github.com/shngli/Data-mining/blob/master/Recommender%20System/movieRating.jpeg)

Normalize the ratings by subtracting the average for each row and then subtracting the average for each column in the resulting table. **Output**: movieRating.py

2) This is a table giving the profile of three items:

![cosineScore.jpeg](https://github.com/shngli/Data-mining/blob/master/Recommender%20System/cosineScore.jpeg)

The first five attributes are Boolean, and the last is an integer "rating." Assume that the scale factor for the rating is α. Compute, as a function of α, the cosine distances between each pair of profiles. For each of α = 0, 0.5, 1, and 2, determine the cosine of the angle between each pair of vectors. **Output**: cosineScore.py

3) Suppose we have three points in a two dimensional space: (1,1), (2,2), and (3,4). We want to perform PCA on these points, so we construct a 2-by-2 matrix whose eigenvectors are the directions that best represent these three points. Construct this matrix. **Output**: pca.py
