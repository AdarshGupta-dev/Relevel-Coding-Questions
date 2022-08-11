"""
Question: Number of Arrays

You have been given an array A of N integers. 
Find the the number of different array B than can be generated with following conditions.

1. len(B) == len(A)
2. 1<= B[i] <= A[i] for i : 1<= i <= N
3. B[i] != B[j] for i,j :  i : 1<= i<j <= N

since ans can be very large, print the ans % 10^9 + 7


Constrains

1 <= N <= 10000
1 <= A[i] <= 10^9
All input are integers.

Input Format:
First line contains size of array.
Second line contain array.

Output Format: 
Number of array % 10^9+7

Sample input:
2
2 3  

Sample output:
4

Explanation: 

1 can be added at position 1, 2, or 3 to make it into [2, 1, 3, 1]. 
This can be divided into [2], [1], and [3, 1]; which does satisfy 2^k form.


"""

# Solution with explanation.
