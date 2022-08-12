"""
Question: NP Problem

An array A of N integers is said to be a good if these conditions are met.
1. Elements of array are non-decreasing. i.e A1 < A2 < A3 <... < An.
2. Product of all elements is less than or equal to P.

Find how many distinct good array A, exist for a given value of N and P. 

Constrains
1 <= T <= 5
1 <= N <= 3
1 <= P <= 2 * 10^10
All input are integers.

Input: 
T : Number of test cases.
N : length of array
P : for good array calculation.

Input Format:
First line contain T
Second line contain N and P.

Output Format: 
Each separate line for each testcase results.

Sample input:
1
2 4

Sample output:
5

Explanation: 

All possible good array are [1,1], [1,2], [1,3], [1,4], and [2,2].
"""

# Solution with explanation.

def solve(target):
# this function solves for n ==2
    sum = 0
    i = 0
    while i < P // i:
        sum += P//i - i + 1
        i += 1
    return ans

T = int(input())
for i in range(T):
    N, P = input().split(" ")
    N, P = int(N), int(P)
    
    ans = 0
    if N == 1:
        ans = P
    elif N == 2:
        ans = solve(P)
    elif N == 3:
        sum = 0
        i = 1
        while True:
            temp = solve(P//i)
            if temp > 0:
                sum += temp
                i+=1
            else:
                break
        ans = sum
    print(ans)