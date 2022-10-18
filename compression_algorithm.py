def comprize(name:str)-> str:
    count=1
    a=[]
    result="-"
    for i in range(0,len(name)):
        if i==len(name)-1:
            if name[i]==name[i-1]:
                # count=count+1
                a.append([name[i],str(count)])
            else:
                a.append([name[i],str(1)])
        elif name[i]==name[i+1]:
            count=count+1
        # elif i==len(name)-1:
        #     a.append([name[i], 1])
        else:
            a.append([name[i],str(count)])
            count=1




    for i in a:
        if i[1]=="1":
            if i[0]==" ":
                result=result+"."
            else:
               result=result+i[0]
        elif i[0]==" ":
            result=result+"."+i[1]
        else:
            result=result+i[0]+i[1]

    result=result+"-"
    return result


def verify_answer(ans:str)->bool:
    crt_ans=input("The correct answer\n")
    if ans==crt_ans:
        return True
    else:
        return False














name=input("Enter a text that to be comprised\n")
answer=comprize(name)

if verify_answer(answer):
    print(f"TESTCASE IS PASSED\n{answer}")
else:
    print(f"TESTCASE IS FAILED\n{answer}")












"""
Implement a compression algorithm that accepts a string and compresses it. 
It compresses it by representing repeating characters as numbers.
A compressed string starts and ends with the minus symbol. 
A space character is compressed to a dot symbol. 



Test Cases:

a)

Input
 
sizzlers winning assassins
 
Output
 
-siz2lers.win2ing.as2as2ins-


b)

Input

2122232425    hello       space!

Output

-212332425.4hel2o.7space!-

"""
