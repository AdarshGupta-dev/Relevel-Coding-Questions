"""
Question Name: Not Equal pairs

You are given Array A consists of N positive integers.

Return maximum number of pairs that can be formed from Array such that:
1. both elements are not equal, i.e. for every (a, b) : a != b
2. Any element can be in at most one pair.

Input Format

First line contains a single integer denoting N.
Next line contains N space separated integers denoting the elements of array A.
Output Format

Constrains: 
1<=N<=10^5
1<=Ai<=10^9

Sample Input 1
5
2 1 3 2 1

Sample Output 1
2

Explanation of Sample 1

pairs that can be formed or [[2,1], [3,2]] or [[2,1], [3,1]] or [[2,3],[1,2]]
In maximum number of pairs are 2.
"""

# Solution with explanation.


def findPair(arr):
    global pairs
    temp = arr[0]
    for i in range(1, len(arr)):
        if arr[i] != temp:
            pairs += 1
            arr.pop(0)
            arr.pop(i - 1)
            return
    return True

n = int(input())
arr = [int(x) for x in input().split(" ")]
n = len(arr)

pairs = 0

while len(arr) > 1:
    if findPair(arr):
        break
if len(arr) > 1:

    if arr.count(arr[0]) <= n - len(arr):
        pairs += arr.count(arr[0]) // 2


print(pairs)
