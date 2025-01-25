#241104

sum1=int(input())
a=int(input())

e=[]

for i in range (1,a+1):
    b,c=map(int,input().split())
    e.append(b)
    e.append(c)

def cal(e):
    sum2=0
    for v in range(0,a*2,2):
        sum2+=e[v]*e[v+1]
    if sum1==sum2:
        print("Yes")
    else:
        print("No")

cal(e)