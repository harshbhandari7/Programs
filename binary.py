T=int(input())
for t in range(0,T):
    N=int(input())
    s=""
    while(N>=1):
        if(N%2==0):
            s=s+"0"
        else:
            s=s+"1"
        N=N//2
    #print(s)
    r=s[::-1]
    #print(r)
    one,zero=0,0
    for i in range(0,len(r)):
        if(r[i]=="1"):
            one+=1
        else:
            zero+=1
    print(one)
