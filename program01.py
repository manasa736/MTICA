n1=input().split()
n2=input().split()
ans=[]
for i,j in zip(n1,n2):
    ans.append(int(i)+int(j))
print(*ans)
