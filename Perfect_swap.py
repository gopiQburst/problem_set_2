



def chck_swaps(a:list)->str:
    first=""
    index_f,index_l=0,0
    second=""
    for i in range(len(a[-1])):
        if a[-1][i] in a[0][index_f:]:
            first=first+a[-1][i]
            index_f=len(first)

        elif a[-1][i] in a[1][index_l:]:
            second=second+a[-1][i]
            index_l=len(second)
        else:
            pass
    if first==a[0] and second==a[1]:
        return "TESTCASE IS PASSED"
    else:
        return "TESTCASE IS FAILED"


a=[]
for i in range(3):
   a.append(input().lower().strip())


print(chck_swaps(a))




"""

Given 3 strings: first,  second, and third,  write a program to check whether the third string is a shuffle of first and second strings. 
The string is considered a shuffle only if the characters of the first and second string come in the third string in a way that maintains the left to the right ordering of the characters from each string.
Constraints to qualify as a valid shuffle:
– All characters in the first and the second strings should be present in the third string.
– Third string should contain all characters in the first string in the same order as they appear in the first string. Similarly, the third string should also contain all characters in the second string in the same order as they appear in the second string.

Example 1

Input: 
"abc" 
"def", 
"Adbefc"

Output: 1
 
Example 2

Input: 
"nyc"
"pak"
"npcayk"
Output: 0

Test Cases:

a)

Input
 
one
two
Twoone
 
Output
1
 
b)
 
Input
 
oneoneone
twotwotwo
Twoone
 
Output
0

"""
