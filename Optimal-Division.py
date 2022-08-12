"""
Question Name: Optimal division

You are given Array A consisting of N positive integers.

Value of an array is defined as number of unique elements it have. 
Like value of array [1,2,1,2,2,3] = 3 as it has 3 unique elements(1,2 and 3), value of array [1,2,3,4] = 4 and so on.

Split the array into 2 parts, such that sum of values of 2 sub-arrays are maximum. 

Note : It may be possible that one of them does not receive any element of the bought array.

Input Format
First line contains a single integer denoting N.
Next line contains N space separated integers denoting the elements of the bought array.

Output Format
Print the maximum possible total value of the final arrays that can be achieved if elements of the array are dived optimally.

Constraints
1<=N<=10^5
1<= element of the array<=10^9

Sample Input 1
6
1 2 1 2 2 3

Sample Output 1
5

Explanation of Sample 1
You can divide the array elements as :
A1 = [1,2,2], value of array = 2
A2 = [2,1,3], value of array = 3
Hence total value = 2+3 = 5. 

It can be proved that this is the maximum possible value.
"""


def solve(arr, length):
    count = 0
    temp = -1
    for i in range(length):
        if arr[i] == temp:
            continue
        temp = arr[i]
        if i == length - 1 or arr[i] != arr[i + 1]:
            count += 1
        else:
            count += 2

    return count


N = int(input())
A = input().split(" ")
A.sort()

print(solve(A, N))
