"""
Question Name: Dominant Element


You are given an array A consisting of N positive integers. The ith element of the array is called Dominant if :

1. Let B be an array formed by removing Ai from array A. 
Like if A = [5 1 2 3 2] and i=3, B will be = [5 1 3 2].

2. Now Ai is dominant if it is possible to rearrange elements of array B such that Ai+j > Bj holds for all 1<=j<=length of array B.

Like if Ai = 2 and B = [3 1 2], Ai is dominant.
THis is because if we rearrange elements of array B as [2 1 3], A1+1 > B1, A2+2 > B2 and A3+3 > B3 holds.
Given array A, print the number of Dominant elements in array A.


Input Format

First line contains a single integer denoting N.
Next line contains N space separated integers denoting the elements of array A.


Output Format

Print the number of Dominant elements in array A.


Constraints

1<=N<=10^5
1<=Ai<=N


Sample Input 1

5
5 1 4 3 2

Sample Output 1

2

Explanation of Sample 1

The 1st and 3rd elements of the array are Dominant.
For i=1, B = [1 4 3 2]. Here 5+1>1, 5+2>4, 5+3>3 and 5+4>2 holds.
For i=3, B = [5 1 3 2]. Rearrange array B as [2 3 1 5]. Here 4+1>2, 4+1>3, 4+3>1, 4+4>5 holds.

"""

