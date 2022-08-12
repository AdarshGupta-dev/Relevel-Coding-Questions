"""
Question: Sorting Machine

You have been given an array A of N element composed only of 1s and 0s.
There is a machine that swaps every A[i] = 1 with A[i+1] = 0; in on second.
Find the minimum time required to solve using this machine.

Eg. A = [0, 1, 0, 0, 1, 0, 1, 0]

After 1 sec: A = [0, 0, 1, 0, 0, 1, 0, 1]
After 2 sec: A = [0, 0, 0, 1, 0, 0, 1, 1]
After 3 sec: A = [0, 0, 0, 0, 1, 0, 1, 1]
After 4 sec: A = [0, 0, 0, 0, 0, 1, 1, 1]

So, Ans = 4. After 4 seconds, entire array is sorted.

Input: 
T : Number of test cases.
N : length of array
A : array

Constrains
1 <= T <= 10
1 <= N <= 100,000
0 <= A[i] <= 1
All input are integers.

Input Format:
First line contain T
Second line contain length of test case array
Third line contain value of test case array

Sample input:
2
3
1 0 0
2
0 1

Sample output:
2
0

Explanation: 
In case of A = [1, 0, 0]
After 1 sec: A = [0, 1, 0]
After 2 sec: A = [0, 0, 1]
thus ans is 2.

In case of A = [0, 1]
Array is already sorted; thus ans = 0

"""


def countSeconds(array):
    zero, one, ans = 0, 0, 0
    for i in array[::-1]:
        if i == 1:
            ans = max(ans, one + zero)
            one = min(one + 1, one + zero)
        else:
            one = max(0, one - 1)
            zero += 1
    return ans


TestCases = int(input())
solutions = []
for i in range(TestCases):
    length = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]

    solutions.append(countSeconds(array))

for i in range(TestCases):
    print(solutions[i])
