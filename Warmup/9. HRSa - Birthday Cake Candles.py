n=int(input())
c=list(map(int, input().split()))
s=0
m=max(c)

for i in c:
    if i==m:
        s+=1
print(s)