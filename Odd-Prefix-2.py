"""
Question: Odd Prefix 2

You have been given an array A of N integers. 
An array B is said to be prefix of array A, if it can be formed by deleting several [0<= k < N] from end of array A.

Eg. A = [5, 1, 4, 2]
then B can be [5], [5, 1], [5, 1, 4], and [5, 1, 4, 2]

A prefix is considered good if sum of all elements are odd.
In above example: [5], and [5, 1, 4, 2] are good prefix.

Now, arrange the array in such a way; that there are maximum number of good prefixes. 

Print number of good prefixes, and array. If multiple array are possible, print the lexicographically smallest of them.

Input: 
N : length of array
A : array

Constrains
1 <= N <= 10000
1 <= A[i] <= 10000
All input are integers.

Input Format:
First line contain size of array.
Second line contain array.

Output Format: 
Number of good prefixes.
Re-arranged array.

Sample input 1:
3
4 3 6 

Sample output 1:
3
3 4 6

Sample input 2:
5
1 2 3 1 1

Sample output 2:
3
1 1 1 2 3

Sample input 3:
5
1 1 1 2 2 

Sample output 3:
4
1 1 1 2 2

"""

# Solution with explanation.


def ans(arr):
    count = 0  # we will increment count, every time we add a number that may result in odd sum.
    # Separate the odd and even numbers, and sort the two separate arrays
    even = []
    odd = []
    for nr in arr:
        if nr % 2 == 0:
            even.append(nr)
        else:
            odd.append(nr)

    even.sort(reverse=True)
    odd.sort(reverse=True)

    # Initialize the array
    ans_arr = []

    # Place the lowest odd number
    if odd:
        ans_arr.append(odd.pop())
        count += 1

    # keep going until we have odd AND even numbers
    while odd and even:
        # If the next odd number is lower than the even number, and we still have 2 or more, we place 2
        if odd[-1] < even[-1] and len(odd) >= 2:
            ans_arr.append(odd.pop())
            ans_arr.append(odd.pop())
            count += 1
        # We don't have 2 odd numbers, or the even number is lower, we place the even number
        else:
            ans_arr.append(even.pop())
            count += 1
    count += len(even) + len(odd) // 2

    # NOTE: The order of the next two loops does not matter, as only 1 will run
    # Place the remaining odd numbers
    while odd:
        ans_arr.append(odd.pop())

    # Place the remaining even numbers
    while even:
        ans_arr.append(even.pop())

    print(count)
    print(ans_arr)


n = input()
a = [int(x) for x in input().split(" ")]

ans(a)
