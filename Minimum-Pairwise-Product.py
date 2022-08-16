"""
Question: Minimum Pairwise Product

You are given an array of N size, and another array of M size.

`Compatibility` of two arrays A and B is measured as:

1. Two arrays are compatible if and only if they have an equal number of elements.
2. `Compatibility` value of arrays A and B each having length L = A1*B1 + A2*B2 + … + AL*BL.

You can remove any number of element from both of these arrays to get an `compatibility`.

Print the maximum possible `compatibility`.

Input Format
First line contains two space separated integers denoting N and M.
Next line contains N space separated integers denoting the elements of array A.
Next line contains M space separated integers denoting the elements of array B.

Output Format
Print the maximum compatibility value it's possible to achieve by removing some elements from both the arrays

Constraints
1<=N,M<=1000
-105<=Ai, Bi<=105

Sample Input 1
3 4
-1 2 1
-100 3 10 -9

Sample Output 1
120

Explanation of Sample 1
Erase the 3rd element of array A. Array A becomes = [-1, 2]
Erase the 2nd and 4th element of array A. Array A becomes = [-100, 10]
Compatibility values of these arrays = [(-1)*(-100) + 2*10] = 120
"""