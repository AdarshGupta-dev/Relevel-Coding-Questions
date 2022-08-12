"""
Question: Perfectly filled buckets. 

You have been given an array A of N prime numbers. You need to fill K buckets with integers of array.

Initially, all buckets are empty. And they are numbered from 1 to N. 
Each element can be put in at most one bucket. Also, each bucket must contain at least one integer.

A bucket is considered "perfectly-filled", if after removing at most one integer from the bucket,
the product of resultant integers in the bucket becomes a perfect square, or bucket will become empty.

Bi denotes the number of integers in the bucket numbered i. 

Find the maximum possible value of M, for M = min( B1, B2, ... BK), if buckets are filled optimally.

Constrains
1 <= T <= 10
1 <= K <= N <= 100,000
2 <= A[i] <= 120
Ai is prime number
All input are integers.

Input Format:
First line contain T

First line of each test cases contain K and N, separated by a space.
Second line of each test cases contain N space separated ints.

Output format:
Print in a new line for each test case, a single integer denoting the maximum possible value.

Sample input:
1
5 2
3 2 5 3 2

Sample output:
2

Explanation: 
We need to perfectly fill 2 buckets with maximum number of elements from Array A. 

B1 = 3: Bucket would contain [3, 5, 3]. 
B2 = 2: Bucket would contain [2, 2]
so min(B1, B2) = 2

Note: 
We have maximize size smaller of both B1, B2; to have bigger min of both. 
We can't add move 2 from b2 to b1 because: then b1 would not be perfectly filled and b2 size would become 1, reducing min value.
For same, reason we can't move 3 from b2 to b1.
We can move 5, but there won't be any chance to result.
"""

# Solution with explanation.

# Since does ask, what buckets will contain; it is idiotic to calculate all combinations.
# we will calculate possible length of sub-arrays. i.e max of min of bucket lengths.
def solve(Arr, length, buckets):
    if buckets > length // 2:
        return 1
    if buckets == 1:
        return length

    Arr.sort()
    singles, pairs, ans = 0, 0, 0

    i = 0
    while i < length:
        if i == length - 1 or Arr[i] != Arr[i + 1]:
            singles += 1
            i += 1
        else:
            pairs += 1
            i += 2

    while pairs:
        if pairs >= buckets:
            ans += 2
            pairs -= buckets

    if singles >= buckets:
        ans += 1
        singles -= 1

    return ans


Testcases = int(input())

for i in range(Testcases):
    N, B = [int(x) for x in input().split(" ")]
    A = [int(x) for x in input().split(" ")]

    print(solve(A, N, B))
