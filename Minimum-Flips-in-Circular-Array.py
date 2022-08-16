"""
Question: Minimum Flips in Circular Array

You are given a circular binary array Arr of size N (A circular array is an array where we consider the first and last element to be adjacent).
In one operation you can choose an index i(1<=i<=N) and flip the number at index i, i.e.if Arr[i]=1 you can make it 0 and vice versa

You are given two integers O and Z.Your aim is to make a subarray of size O+Z such that the first O digits of the subarray are 1s and the last Z digits of the subarray are 0s
What is the minimum number of operations required to do so?

Note: A subarray is a slice from a contiguous array (i.e., occupy consecutive positions) and inherently maintains the order of elements.

Input Format
The first line of the input contains 3 space-separated integers denoting N O and Z respectively
The next line contains N space separated integers denoting Arr[i](1<=i<=N)

Output Format
Print an integer denoting the minimum number of operations required to make a subarray of size O+Z such that the first O digits of the subarray are 1s and the last Z digits of the subarray are 0s

Constraints
1<=N<=10^5
0<=O,Z<=N
1<=O+Z<=N
0<=Arr[i](1<=i<=N)<=1

Sample Input
4 1 1
1 1 1 1
1

Sample Output
1

Sample Explanation
One of the solutions is to flip the digit at index 2 resulting in our array as 1 0 1 1 and 1 0(index 1 and 2) will be our required subarray
"""

# Solution with explanation:


def solve(arr, length, ones, zeros):
    ansO = ones - sum(arr[0:ones])
    ansZ = sum(arr[ones : ones + zeros])
    ans = ansO + ansZ
    j = ones
    k = ones + zeros
    for i in range(1, length):
        j +=1
        k +=1

        if arr[j - 1] and not arr[i - 1]:
            ansO = max(0, ansO - 1)
        if not arr[j - 1] and arr[i - 1]:
            ansO += 1

        if arr[k - 1] and not arr[j - 1]:
            ansZ += 1
        if not arr[k - 1] and arr[j - 1]:
            ansZ = max(0, ansZ - 1)
        ans = min(ans, ansO + ansZ)
    return ans


N, O, Z = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A += A[: O + Z - 2]
print(solve(A, N, O, Z))
