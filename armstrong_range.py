for i in range(100,1000):
    h=i//100
    t1=i%100
    t=t1//10
    o=i%10
    num1=h**3+t**3+o**3
    if i==num1:
        print(i,"Number is an armstrong")
        
    
print("Number is not an armstrong ")
