#2480
#20241102

a,b,c=map(int,input().split())

def same1(a,b):
    if a==b:
        return a
    else:
        return 0

def same2(b,c):
    if b==c:
        return b
    else:
        return 0

def same3(a,c):
    if a==c:
        return c
    else:
        return 0

def bigger(a,b,c):
    if a>b:
        if b>c:
            return a
        else:
            if a>c:
                return a
            else:
                return c
    else: #a<b
        if a>c:
            return b
        else:
            if b>c:
                return b
            else:
                return c
sum=0
#count를 사용하는 방법을 찾아야할듯...
if same1(a,b)==a and same2(b,c)==b:
    sum=10000+a*1000
    print(sum)
elif same1(a,b)==a and same2(b,c)==0 or same2(b,c)==b and same1(a,b)==0 or same3(a,c)==c and same2(b,c)==0:
    if same1(a,b)==a and same2(b,c)==0:
        sum=1000+a*100
        print(sum)
    elif same2(b,c)==b and same1(a,b)==0:
        sum=1000+b*100
        print(sum)
    else:
        sum=1000+c*100
        print(sum)

else:
    sum=bigger(a,b,c)*100
    print(sum)