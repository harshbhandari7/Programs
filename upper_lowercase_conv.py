ch=input("enter a character ")
if ord(ch)>=65 and ord(ch)<=90:
    print("entered character is uppercase")
    res=ord(ch)
    res=res+32
    print("lowercase is ",chr(res))
else:    
    print("entered character is lowercase")
    res=ord(ch)
    res=res-32
    print("uppercase is",chr(res))
