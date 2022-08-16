"""
Question: Odd Subset

You are given an array A of integers. 

For array A, print the maximum possible length of the subset of this array such that the sum of all elements of this subset is an odd number. 
If there is no such subset print “-1”(without quotes) instead.

A subset of the array A as a tuple that can be obtained from A by removing some (possibly all) elements of it.

Input Format
First line contains a single integer denoting N.
Next line contains N space separated integers denoting the elements of array A.

Output Format
Print the maximum possible length of the subset of the given array such that the sum of all elements of this subset is an odd number

Constraints
1<=N<=105
1<=Ai<=109

Sample Input 1
4
4 2 3 1

Sample Output 1
3

Explanation of Sample 1
One can select the subset as [4 2 3 1]. 
The sum of all elements of this subset = 4+2+1 = 7 which is odd.
"""


def solve(arr, length):
    odd = 0
    even = 0
    for i in arr:
        if int(i) % 2:
            odd += 1
        else:
            even += 1

    if odd == 0:
        return -1

    if odd % 2:
        return even + odd
    return even + odd - 1


length = input()
arr = input().split()

print(solve(arr))
