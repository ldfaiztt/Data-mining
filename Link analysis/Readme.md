1) Consider three Web pages with the following links:

![pagerank1.jpeg](https://github.com/shngli/Data-mining/blob/master/Link%20analysis/pagerank1.jpeg)

Suppose we compute PageRank with a β of 0.7, and we introduce the additional constraint that the sum of the PageRanks of the three pages must be 3, to handle the problem that otherwise any multiple of a solution will also be a solution. Compute the PageRanks a, b, and c of the three pages A, B, and C, respectively. Then, identify from the list below, the true statement.
**Output**: pagerank1.py

2) Consider three Web pages with the following links:

![pagerank2.jpeg](https://github.com/shngli/Data-mining/blob/master/Link%20analysis/pagerank2.jpeg)

Suppose we compute PageRank with β=0.85. Write the equations for the PageRanks a, b, and c of the three pages A, B, and C, respectively. Then, identify in the list below, one of the equations.
**Output**: pagerank2.py

3) Consider three Web pages with the following links:

![pagerank2.jpeg](https://github.com/shngli/Data-mining/blob/master/Link%20analysis/pagerank2.jpeg)

Assuming no "taxation," compute the PageRanks a, b, and c of the three pages A, B, and C, using iteration, starting with the "0th" iteration where all three pages have rank a = b = c = 1. Compute as far as the 5th iteration, and also determine what the PageRanks are in the limit. Then, identify the true statement from the list below.
**Output**: pagerank3.py

**pagerank.r** implements the solutions for Q1-Q3 in R.

4) Consider the link graph below. Construct the link matrix L based on the HITS algorithm. Then, begin by assuming the hubbiness of each node is 1; that is, the vector h is (the transpose of) [1,1,1,1]. Compute an estimate of the authority vector a = LTh, and normalize a by dividing all values so the largest value is 1. Compute an estimate of the hubbiness vector h = La, and normalize h by dividing all values so the largest value is 1. Repeat the steps. Identify the final estimates. **Output**: pagerank4.py

![pagerank4.jpg](https://github.com/shngli/Data-mining/blob/master/Link%20analysis/pagerank4.jpg)
