def verify(highest_amount):
    crt_answer=int(input("Correct output\n"))
    if crt_answer==highest_amount:
        print(f"TESTCASE IS PASSED\n{highest_amount}")
    else:
        print(f"TESTCASE IS FAILED\n{highest_amount}")


def product(ar):
    p=1
    for i in ar:
        p=p*i
    return p


def highest_sum(a,n):
    re=[]
    start,last=0,0
    for i in range (1,n):
        k=n%i

        for j in range(0,n-k,i):
            start=j
            last=start+i+1
            re.append(product(a[start:last]))
    # print(re)
    return max(re)




a=[]
n=int(input("Number of rolls\n"))
for i in range(n):
    a.append(int(input().strip()))

verify(highest_sum(a,n))








"""


There’s a game in Squid Games where all the participants are given a roll of coins.
Each coin will have a value (positive, negative, or zero).
The participants can select any number of adjacent coins from the roll.
Those who get the highest product value get to the next level. 
If you are participating in the game, can you pick the set of adjacent coins so that the product 
is the highest value?
Examples:
Roll contains coins: 6, -3, -10, 0, 2
Highest product: 180  (The coins are 6, -3, and -10)
Roll contains coins: -1, -3, -10, 0, 60
Highest product: 60  (The coin is 60)
Roll contains coins: -2, -40, 0, -2, -3
Highest product: 80 (The coins are -2 and -40)

Test Cases:

a)
Input
 
5
-2
-3
-5
0
-4
 
Output
15

b)
Input
 
5
-1
-3
-10
60
0
 
Output
1800










"""
