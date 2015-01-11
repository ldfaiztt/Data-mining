1) The edit distance is the minimum number of character insertions and character deletions required to turn one string into another. Compute the edit distance between each pair of the strings he, she, his, and hers. Then, identify the number of pairs at a certain edit distance. **Output**: lcs.py

2) Consider the following matrix:

![minhash.jpeg](https://github.com/shngli/Data-mining/blob/master/LSH/minhash.jpeg)

Perform a minhashing of the data, with the order of rows: R4, R6, R1, R3, R5, R2. Which of the following is the correct minhash value of the stated column? **Output**: minhash.py

3) Consider a matrix representing the signatures of seven columns, C1 through C7:

![candPair.jpeg](https://github.com/shngli/Data-mining/blob/master/LSH/candPair.jpeg)

Suppose we use locality-sensitive hashing with three bands of two rows each. Assume there are enough buckets available that the hash function for each band can be the identity function (i.e., columns hash to the same bucket if and only if they are identical in the band). Find all the candidate pairs. **Output**: candPair.py

4) Find the set of 2-shingles for the "document": ABRACADABRA and also for the "document": BRICABRAC. How many 2-shingles do they have in common? What is the Jaccard similarity between the two documents"? **Output**: shingles.py

5) How many distinct 3-shingles are there in the string "hello world" (excluding the quotes)? **Output**: shingleHello.py

6) We have an LSH family h of (d1,d2,0.6,0.4) hash functions. We can use three functions from h and the AND-construction to form a (d1,d2,w,x) family, and we can use two functions from h and the OR-construction to form a (d1,d2,y,z) family. Calculate w, x, y, and z. **Output**: lshAndOr.py

7) There are 8 strings that represent sets: s1 = abcef; s2 = acdeg; s3 = bcdefg; s4 = adfg; s5 = bcdfgh; s6 = bceg; s7 = cdfg; s8 = abcd. The upper limit on Jaccard distance is 0.2, and we index the strings based on symbols appearing in the prefix. For each of s1, s3, and s6, determine how many other strings that string will be compared with, if it is used as the probe string. **Output**: jaccard.py

