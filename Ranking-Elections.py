"""
Question: Ranking elections

Political party 1 has `(N+1)` members for an election. `N` members have already received their votes.
Array A contain votes received by N members in order. i.e. A[i] is received by ith member.

Party decides rank based on their number of votes. Member with higher votes, receive better rank. 
In case of tie, member with lower i receive better rank.

eg. 3 members received [2, 3, 2] votes respectively. Their ranks would be [2, 1, 3] respectively. 
2nd member received highest votes, thus rank 1. Member 1, and 3 received equal votes, and 1 < 3; thus 1 is given better rank.

(N+1)th member have yet to receive votes. Find out total number of different ranks he could possibly get. 

Input: 
T : Number of test cases.
N, Q : number of members and number of queries.
A : array of votes received
L, Q : Query

Constrains
1 <= T <= 1000
1 <= N,Q <= 100000
1 <= A[i] <= 10^9
1 <= L <= N
1 <= R <= 10^9
All input are integers.

Input Format:
First line contain T
Second line contain number of members and number of queries.
Third line contain array of votes received
Fourth line onwards contain query or modification.

Output Format: 
Each separate line for each testcase results.

Sample input:
1
4 1
2 1 1 5
2 3

Sample output:
5

Explanations: 
No of test cases 1.
No of members that have received votes : 4. This makes total member : 5. Number of queries: 1
member and their votes, member 1: 2, member 2:1, member 3:1, member 4:5. Ranks = [2, 3, 4, 1]
Query: 2, 3. Member 2 has received 3 votes. New votes = [2, 3, 1, 5] Ranks = [3, 2, 4, 1]

if n+1 receives 0 votes: he would receive 5th rank. Ranks = [3, 2, 4, 1, 5]
if n+1 receives 1 votes: he would receive 5th rank. Ranks = [3, 2, 4, 1, 5]
if n+1 receives 2 votes: he would receive 4th rank. Ranks = [3, 2, 5, 1, 4]
if n+1 receives 3 votes: he would receive 3rd rank. Ranks = [4, 2, 5, 1, 3]
if n+1 receives 4 votes: he would receive 2nd rank. Ranks = [4, 3, 5, 1, 2]
if n+1 receives 5 votes: he would receive 2nd rank. Ranks = [4, 3, 5, 1, 2]
if n+1 receives >5 votes: he would receive 1st rank. Ranks = [4, 3, 5, 2, 1]

so number of different ranks he could receive is 5. 
"""

# Solution with explanation

# this function ranks members based on their number of votes
def RankedMembers(votes):
    # sorting to have a reference of all votes in descending order. 
    # In new array because, if same number of votes occur; index can be given priority. 
    sorted_votes = sorted(votes)
    
    # Giving negative ranks to prevent conflict with vote count.
    rank = -1
    for i in sorted_votes:
        while i in votes:
            votes[votes.index(i)] = rank
            rank -= 1
    # now array contains only rank not votes. Removing negative and returning it back.
    return [-x for x in votes]


# This function makes list of all possible ranks and returns count.
def unique_ranks(votes):
    ranks = []

    # Feeding all possibility of votes that can be received by n+1 th member. i.e. 0 to max + 1
    for i in range(0, max(votes) + 1):
        # Adding only unique to count.
        if RankedMembers(votes + [i]) not in ranks:
            ranks.append(RankedMembers(votes + [i]))

    return len(ranks)


# number of test cases
T = int(input())


for i in range(T):
    N, Q = input().split(" ")
    N, Q = int(N), int(Q) # length of array and queries

    A = input().split(" ")
    A = [int(x) for x in A] # votes

    for j in range(Q):
        L, R = input().split(" ")
        L, R = int(N), int(Q) # query

        A[L - 1] = R # changes to votes based on query

    unique_ranks(A) 
