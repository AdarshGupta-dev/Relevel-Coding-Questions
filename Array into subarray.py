"""
Question: Array into sub-array

You have been given an array A of N integers. 
Divided it into 3 non-empty sub-arrays, such that sum of each sub-array can be represented in form of 2^k. K is a whole number.

Eg. A = [1, 2, 3, 1]

A can be divided into [1], [2], [3, 1]. These have sum of 1 = 2^0, 2 = 2^1, and 4 = 2^2. 

You can add 1 at any index of array. You can do add any number of time. 


You need to find minimum number of times, 1 should be added such that all three sub-array is in 2^k form.

Input: 

T : Number of test cases.
N : length of array
A : array

Constrains

1 <= T <= 5
1 <= N <= 1000
1 <= A[i] <= 100
All input are integers.

Input Format:
First line contain T
Second line contain size of array.
Third line contain array of votes received

Output Format: 
Each separate line for each testcase results.

Sample input:
1
3
2 1 3

Sample output:
1

Explanation: 

1 can be added at position 1, 2, or 3 to make it into [2, 1, 3, 1]. 
This can be divided into [2], [1], and [3, 1]; which does satisfy 2^k form.


"""

# Solution with explanation.

# we need to compare sum to nearest exponent. It is better to just have a list to compute every time.
exponents_of_2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]

# this function return difference of x from next larger 2^k.
def diff(x):
    for i in exponents_of_2:
        if x == i:
            return 0
        elif x < i:
            return i - x


# This function finds the minimum number of required ones
def solve(Nums, length):
    if length < 3:
        return 0

    # this is just a random number.
    ans = 131072
    sumA = 0

    for i in range(1, length - 1):
        # sumA and ansA is calculated in upper iteration to prevent re-doing in lower iteration.
        sumA += Nums[i - 1]
        ansA = diff(sumA)
        sumB = 0
        sumC = sum(Nums[i:])

        for j in range(i + 1, length):
            sumC -= Nums[j - 1]
            sumB += Nums[j - 1]
            ones_needed = ansA + diff(sumB) + diff(sumC)

            if ans > ones_needed:
                ans = ones_needed

    return ans


# number of test cases
T = int(input())


for i in range(T):
    N = int(input())  # length of array
    A = input().split(" ")  # array
    A = [int(x) for x in A]
    print(solve(A, length=N))
