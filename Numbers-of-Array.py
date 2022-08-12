"""
Question: Number of Arrays

You have been given an array A of N integers. 
Find the the number of different array B than can be generated with following conditions.

1. len(B) == len(A)
2. 1<= B[i] <= A[i] for i : 1<= i <= N
3. B[i] != B[j] for i,j :  i : 1<= i<j <= N

since ans can be very large, print the ans % 10^9 + 7

Constrains
1 <= N <= 10000
1 <= A[i] <= 10^9
All input are integers.

Input Format:
First line contains size of array.
Second line contain array.

Output Format: 
Number of array % 10^9+7

Sample input:
2
3 2  

Sample output:
4

Explanation: 

Length of 32 is 2. The number of digits in 32 is 2. So, new numbers should be of 2 digits only.
31 is a valid ans. As 31 ≤ 32; and 3≤3, and 1≤2. New number 31 is less than original. Also, every new digit is less or equal to the original digit.

Similarly, 11, 12, 21, 22, 31, and 32 are valid of condition 2nd. 14, 41, 33, and 15 are not valid.
Now we also have to check for repeating numbers and reject them. So, 11 and 22 from previous step, fails condition 3.

Final ans would be [12, 21, 31, 32] i,e. 4 counts.

For 45: [12, 13, 14, 15, 21, 23, 24, 25, 31, 32, 34, 35, 41, 42, 43, 45]: Ans would be 16

Thank you.
1 can be added at position 1, 2, or 3 to make it into [2, 1, 3, 1]. 
This can be divided into [2], [1], and [3, 1]; which does satisfy 2^k form.

"""

# Solution with explanation.


def solve(arr, length):
    ans = 1
    for i in arr:
        length -= 1
        ans *= i - length
    return ans % (10**9 + 7)


n = int(input())
A = [int(x) for x in input().split(" ")]
A.sort(reverse=True)

print(solve(A, n))
