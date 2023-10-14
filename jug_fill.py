def jugs(N,L,C):
    C.sort(reverse=True)
    cup=[0]*N 
    j_c=L 

    for i in range(N):
        if j_c==0:
            break
        if C[i]<=j_c:
            t_use=j_c//C[i]
            j_c-=t_use*C[i]
            cup[i]=t_use

    total_use=sum(cup)

    return cup ,t_use

N=int(input())

C=list(map(int,input().split()))
L=int(input())
cup,t_use=jugs(N,L,C)

print(C)
print(cup)

