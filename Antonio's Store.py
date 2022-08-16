"""
Question: Antonio’s Store


Antonio is a very successful businessman. Recently he bought a basketball Store. In the basketball Store, there are N containers, where each container can store at most K basketballs.
Initially ith. container contains A[i] balls. Now he bought M more basketballs from somewhere and wants to store them in these containers. He can store the jth ball (1<=j<=M) in any container. He cannot remove initial balls from the container.

Your task is to determine the minimum capacity K such he can store all the additional M balls into the containers.

Input Format
The first line contains two space-separated integers N and M.
The second line contains N space-separated integers, the array A.

Output Format
Print the minimum capacity K for that Antonio can store all the additional M balls into the containers

Constraints
1<=N<=105
1<=A[i],M<=109.

Sample Input 1
3 4
1 2 3

Sample Output 1
4

Explanation of Sample 1
For the given test case, we can set K=4 and then
Add 2 more basketballs in the first.
Add 2 more basketballs in the second
"""


def solve(arr, length, extras):
    empty = max(arr) * length - sum(arr)

    if empty > extras:
        return max(arr)
    return max(arr) + ((extras - empty) // length) + 1


n, m = [int(x) for x in input().split()]

a = list(map(int, input().split()))

print(solve(a, n, m))
