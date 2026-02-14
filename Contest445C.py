N=int(input())
A=list(map(int,input().split()))
Answer=[None]*N
for s in range(N):
    if Answer[s]!=None:
        continue
    x=A[s]-1
    X=A[x]
    R=[]
    while True:
        if Answer[x]!=None:
            Answer[s]=Answer[x]
            for i in R:
                Answer[i]=Answer[x]
            break
        elif x+1==X:
            Answer[s]=x+1
            for i in R:
                Answer[i]=x+1
            Answer[x]=x+1
            break
        else:
            R.append(x)
            x=A[x]-1
            X=A[x]

print(*Answer)