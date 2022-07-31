"""
Question: Array into sub-array

You have been given an array A of N integers. 
Divided it into 3 non-empty sub-arrays, such that sum of each sub-array can be represented in form of 2^k. K is a whole number.

Eg. A = [1, 2, 3, 1]

A can be divided into [1], [2], [3, 1]. These have sum of 1 = 2^0, 2 = 2^1, and 4 = 2^2. 

You can add 1 at any index of array. You can do add any number of time. 


You need to find minimum number of times, 1 should be added such that all three sub-array is in 2^k form.


Constrains

1 <= T <= 5
1 <= N <= 1000
1 <= A[i] <= 100
All input are integers.


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

# this function return difference of x from next larger 2^k. 
def two_power_k(x):
    # k in 2^k is whole number. Thus k starts with 0
    k = 0
    while True:
        # if x is equal to 2^k, difference is zero.
        if x == 2**k:
            return 0
        # if x is greater than 2^k, increment k for next comparison.
        elif x > 2**k:
            k += 1
        # if x is smaller, then we have found the next larger 2^k. We just need to return difference. 
        else:
            return 2**k - x

# this function returns minimum placement of 1s are needed.
def solve(Nums, length):
    # we will make a list of all possible ways to make 2^k.
    ones_needed = []

    # I am using 2 pointer. i will divide, a1 and a2; while j will separates a2 and a3. 
    for i in range(1, length):
        # i and j starts with 1 difference as sub array can't be empty.
        for j in range(i + 1, length):
            ones_needed.append(
                two_power_k(sum(Nums[:i])) # a1
                + two_power_k(sum(Nums[i:j])) # a2
                + two_power_k(sum(Nums[j:])) # a3
            )
    return min(ones_needed)

# number of test cases
T = int(input())


for i in range(T):
    N = int(input()) # length of array 
    A = input().split(" ") # array
    A = [int(x) for x in A]
    print(solve(A), length=N)
