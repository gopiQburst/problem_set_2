def verify(answer:int)->str:
 crt_answer=int(input("Enter the correct answer\n"))
 if crt_answer==answer:
     return "TESTCASE IS PASSED"
 else:
     return "TESTCASE IS FAILED"

def decode(eqn:str,val:list)->int:
    result=0
    l=[i for i in eqn]
    for i in val:
        for k in range(len(l)):
            if l[k]==i[0]:
                l[k]=i[1]
    result=eval("".join(l))
    print(result)
    return result



eqn =input("Enter A eqn\n")
a=[]
for i in range(3):
   k=list(map(str,input().split(" ? ")))
   a.append(k)

ans=decode(eqn,a)
print(verify(ans))








"""
program should read an alphanumeric string say, “a6b5c3” , 
where a, b, c can be either *, +, -, number which should read from input.
 And should output evaluated expression 
Input: a6b5c3
a ? -
b ? +
c ? 5
Output : 547 (evaluated result of -6+553)




"""
