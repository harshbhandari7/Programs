T=int(input())
for t in range(0,T):
    N=int(input())
    s=""
    while(N>=1):
        a=N%16
        #print(a)
        s=s+str(a)
        N=N//16
    #print(s)
    r=s[::-1]
    print(r)
print(end=" ")
