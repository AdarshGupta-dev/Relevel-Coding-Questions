"""
Question: Powerful Triplet

You are given an array of integers.

For a triplet (X, Y, Z) (1<=X<Y<Z<=N),  defines its power as: | AX - AY | * AZ.
X, Y, and Z are indices. And AX, AY, and AZ are elements.

Find the maximum possible power that a triplet can have.

You are given T independent test cases.

Constraints
1 <= T <= 10
3 <= N <= 105
1 <= Ai <= 109
All input values are integers.

Input Format
First-line contains T.
First line of each test case consists of a single integer N.
Second line of each test case consists of N space separated integers denoting the array A.

Output Format
Print in a newline for each test case a single integer denoting maximum possible power that a triplet can have.

Sample Input 1
1
4
1 2 4 3

Sample Output 1
9

Explanation of Sample 1
If she choses the triplet (1, 3, 4), then power = | A1 - A3 | * A4 = | 1 - 4 | * 3 = 9
"""