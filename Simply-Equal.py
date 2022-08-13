"""
Question: Simply Equal

You are given an array A of N integers. 
In one operation you can select a non-empty sub-sequence of A, and decrease each element of the subsequence by 1.

Find the minimum number of operations required to make all the elements of the array A equal.

You are given T independent test cases.

Constraints
1 <= T <= 10
1 <= N <= 105
1 <= Ai <= 109
All input values are integers.

Input Format
First-line contains T.
First line of each test case consists of a single integer N.
Second line of each test case consists of N space separated integers denoting the array A.
Output Format

Print in a newline for each test case a single integer denoting the minimum number of operations required to make all the elements of the array A equal.

Sample Input 1
1
3
2 1 2

Sample Output 1
1

Explanation of Sample 1

She can select the subsequence S = {A1, A3} and decrease each by 1. So array becomes: A = [1, 1, 1]
"""

test_case = int(input())
ans = []

for i in range(test_case):
    length = input()
    arr = input()
    y = list(map(int, arr.split()))
    ans.append(max(y) - min(y))

for i in ans:
    print(i)
