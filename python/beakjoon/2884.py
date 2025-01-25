#241028

h,m=map(int,input().split())

h1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

def minute(h,m):
    if m>=45:
        m=m-45
        h=h1[h]
        return(f"{h} {m}")
    else:
        h=h1[h-1]
        m=m-45
        m=60-(-1*m)
        return(f"{h} {m}")

print(minute(h,m))