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

Sample input 2:
3
0 0 1

Sample input 3:
3
1 1 1 

Sample output 1:
3
3 4 6

Sample output 2:
3
1 0 0

Sample output 3:
1
1


"""

# Solution with explanation.

def ans(odd, evens):
    len_evens = len(evens)
    len_odds = len(odds)
    
    if len_odds == 0:
        print(0)
        return
    else:
        print(len_evens + 1)
        print(f"{odd[0]}", end=" ")
        print(*evens, end=" ")
        print(*odds[1:])
        return


n = input()
a = [int(x) for x in input().split(" ")]
a.sort()


odds = []
evens = []

for i in a:
    if i % 2:
        odds.append(i)
    else:
        evens.append(i)

ans(odds, evens)
