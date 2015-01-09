1) Consider the diagonal matrix M. Compute its Moore-Penrose pseudoinverse, and then identify the elements of the pseudoinverse. **Output**: pseudoInverse.py

![matrix m.jpeg](https://github.com/shngli/Data-mining/blob/master/Clustering/matrix%20m.jpeg)

2) In certain clustering algorithms, such as CURE, we need to pick a representative set of points in a supposed cluster, and these points should be as far away from each other as possible. Begin with the two furthest points, and at each step add the point whose minimum distance to any of the previously selected points is maximum. Suppose these are the following points in two-dimensional Euclidean space: x = (0,0); y = (10,10), a = (1,6); b = (3,7); c = (4,3); d = (7,7), e = (8,2); f = (9,5). x and y are furthest apart, so start with these. You must add six more points, and the distance measure is the normal Euclidean L2-norm. What is the order in which the points are added? **Output**: CURE.py

3)We wish to cluster the set of points in the image into 10 clusters. We initially choose each of the green points (25,125), (44,105), (29,97), (35,63), (55,63), (42,57), (23,40), (64,37), (33,22), and (55,20) as a centroid. Assign each of the gold points to their nearest centroid.Then, recompute the centroids of each of the clusters. Do any of the points then get reassigned to a new cluster on the next round? **Output**:

![cluster.jpeg](https://github.com/shngli/Data-mining/blob/master/Clustering/cluster.jpeg)
