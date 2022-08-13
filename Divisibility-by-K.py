"""
Question: Divisibility By k

You are given an array A of N integers.
In one operation, you select a non-empty subsequence of array A and increase or decrease each element of the array by 1.
Find the minimum number of operations you need to make each element of the array A, divisible by K.

You are given T independent test cases.

Constraints
1 <= T <= 10
1 <= N <= 105
2 <= K <= 105
0 <= Ai <= 109
All input values are integers.

Input Format
First-line contains T.
First line of each test case consists of two space separated integers N and K.
Second line of each test case has N space separated integers denoting the array A.

Output Format
Print in a newline for each test case a single integer denoting the minimum number of operations she needs to make each element of the array divisible by K.

Sample Input 1
1
4 3
4 3 6 2

Sample Output 1
2

Explanation of Sample 1
Iteration 1: Select {A0}, and decrement them. A = [3,3,6,2]
Iteration 2: Select {A3}, and increment them. A = [3,3,6,3]

Now each element of the array is divisible by 3.
"""
