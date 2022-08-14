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

# Solution with explanation:

# Step1: Take modulus of every int. For k = 5, Ai 1, 6, 11, 16... all these are same. They would need equal effort. So make them one.
# You don't even need to iterate over entire list. Just till you have found all possible remainders.

# now move a pointer from 1, to k-1. Push everything on left to 0 and everything on right to k. Count cost. 
# repeat and return smallest of them.

def solve(arr, length, K):
    # this is to check appearance of every possible remainders. Last True is just buffer.
    remainders = [False] * K + [True]
    for i in arr:
        remainders[i % K] = True
        if all(remainders):
            break
    
    # k is maximum possible iteration.
    iterations = K
    for i in range(1, K):
        # we are moving a divider from 1 to k.
        # pushing every left to zero, and right to k.
        remainders_left = remainders[:i]
        remainders_right = remainders[i:]

        temp = 0
        if True in remainders_left:
            temp = len(remainders_left) - 1 - remainders_left[::-1].index(True)
        if True in remainders_right:
            temp += K - i - remainders_right.index(True)
        iterations = min(iterations, temp)

    return iterations


test_cases = int(input())
output = []

for i in range(test_cases):
    length, K = input().split()
    K = int(K)

    arr = list(map(int, input().split()))

    output.append(solve(arr, length, K))

print(*output, sep="\n")
