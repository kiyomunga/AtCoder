N=int(input())
A=[x-1 for x in map(int,input().split())]
Answer=[None]*N

for s in range(N):
    if Answer[s]!=None:
        continue
    x=s
    R=[]
    while True:
        if x==A[x]:
            Answer[x]=x+1
            break
        elif Answer[x]!=None:
            break
        else:
            R.append(x)
            x=A[x]
    for i in R:
        Answer[i]=x+1
print(*Answer)


