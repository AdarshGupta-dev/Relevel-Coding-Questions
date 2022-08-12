"""
Question Name: Not Equal pairs

You are given Array A consists of N positive integers.

Return maximum number of pairs that can be formed from Array such that:
1. both elements are not equal, i.e. for every (a, b) : a != b
2. Any element can be in at most one pair.

Input Format
First line contains a single integer denoting N.
Next line contains N space separated integers denoting the elements of array A.
Output Format

Constrains: 
1<=N<=10^5
1<=Ai<=10^9

Sample Input 1
5
2 1 3 2 1

Sample Output 1
2

Explanation of Sample 1
pairs that can be formed or [[2,1], [3,2]] or [[2,1], [3,1]] or [[2,3],[1,2]]
In maximum number of pairs are 2.
"""

# Solution with explanation.

"""
This question seems tricky; but is not.

So, there are N elements. They must form N // 2 pairs. 

What can prevent them from doing so? 
If some random element occur more than n/2 times. If not, ans would always will be n//2.

Now, say if some random element does occur more than n/2 times.
Then, every other element will have a pair. 
so ans is n - frequency of majority element.
"""


def findPair(arr, n):
    majority_found = False
    majority_element, majority_frequency = 0, 0
    mapping = {}
    for i in arr:
        if majority_found:
            if i == majority_element:
                majority_frequency += 1
        else:
            if i in mapping:
                mapping[i] += 1
            else:
                mapping[i] = 1
            if mapping[i] > n // 2:
                majority_found = True
                majority_element = i
                majority_frequency = mapping[i]
    if majority_found:
        return n - majority_frequency
    return n // 2


n = int(input())
arr = [int(x) for x in input().split(" ")]

print(findPair(arr, n))
