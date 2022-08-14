"""
Question: Longest Good Array 1.0

You have been given an array A of N integers. 
P is defined as sum of every previous element in array. 
for: 1<= k <= N
Pk = A1 + A2 + ... Ak

An array is called good array if for each k (1<= k <= N ): Pk + Y*Ak = X.
Find the size of longest sequence of good array within given array.

Constrains
1 <= T <= 1000
1 <= N <= 1000
1 <= A[i] <= 10000
1 <= X, Y <=10^9
All input are integers.

Input: 
T : Number of test cases.
N : length of array
A : array
X, Y : for good array calculation.

Input Format:
First line contain T
Second line contain size of array.
Third line contain array.
Fourth line contain X and Y.

Output Format: 
Each separate line for each testcase results.

Sample input:
1
2 1
4 1

Sample output:
2

Explanation: 
A = [2, 1]
P = [2, 3]
good array: 
P1 + Y*A1 == Y -> 2 + 1*2 == 4 -> True
P2 + Y*A2 == Y -> 3 + 1*1 == 4 -> True
[True, True]
The longest sub-array of good array is 2

"""

# Solution with explanation.

T = int(input())  # no of test cases
output = []

for i in range(T):
    A = list(map(int, input().split()))
    X, Y = input().split(" ")
    X, Y = int(X), int(Y)

    p_arr_element = 0
    ans = count = 0

    for arr_element in A:
        p_arr_element += arr_element

        good_array_element = p_arr_element + Y * arr_element == X

        if good_array_element:
            count += 1
            ans = max(ans, count)
        else:
            count = 0
    output.append(ans)

print(*output, sep="\n")
