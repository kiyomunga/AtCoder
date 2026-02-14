#20260214
#B問題
N=int(input())
S=[None]*N
for i in range(N):
    S[i]=input().rstrip()

S_list=[None]*N
for i in range(N):
    S_list[i]=list(S[i])

L=[None]*N
for i in range(N):
    L[i]=len(S_list[i])

m=max(L)

for i in range(N):
    print("."*((m-L[i])//2)+S[i]+"."*((m-L[i])//2))
