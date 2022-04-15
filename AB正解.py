import time
import random

num=time.time()
second=int(num)
answer=int(10000*(num-second)) 
th=answer//1000
h=(answer-(th*1000))//100
ten=(answer-(th*1000)-h*100)//10
one=answer-(th*1000)-h*100-ten*10

a=0
while(a!=1):
    if(th==h or th==ten or th==one):
        answer=answer+2597
        if answer>=10000:
            answer=answer%10000
    if h==ten or h==one:
        answer=answer+2597
        if answer>=10000:
            answer=answer%10000
    if ten==one:
        answer=answer+2597
        if answer>10000:
            answer=answer%10000              
    th=answer//1000
    h=(answer-(th*1000))//100
    ten=(answer-(th*1000)-h*100)//10
    one=answer-(th*1000)-h*100-ten*10  
    if th!=h and th!=ten and th!=one and h!=ten and h!=one and ten!=one:
        break

guess=int(0)
A=int(0)
B=int(0)
while(guess!=answer):
    print("請輸入四個數字")
    w=int(input())
    x=int(input())
    y=int(input())
    z=int(input())
    r=[]
    if w==th:
        A+=1
        r.append("1")
    elif w==h or w==ten or w==one:
        B+=1
    if x==h:
        A+=1
        r.append("2")
    elif x==th or x==ten or x==one:
        B+=1
    if y==ten:
        A+=1
        r.append("3")
    elif y==th or y==h or y==ten:
        B+=1
    if z==one:
        A+=1
        r.append("4")
    elif z==th or z==h or z==one:
        B+=1
    print("\n")
    print(A,"A",B,"B")
    print("猜對的位子有",r)
    print(answer)
    print(w,x,y,z)
