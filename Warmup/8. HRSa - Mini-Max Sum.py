l=list(map(int, input().split()))
sum1=0
sum2=0

for i in l:
    sum1=sum1+i
    sum2=sum2+i

s1=sum1-max(l)
s2=sum2-min(l)
print(s1,end=" ")
print(s2)