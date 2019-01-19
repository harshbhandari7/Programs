#to check given character string is uppercase or lowercase
char=input("enter the character\n")
res=ord(char)
if res>=65 and res<=90:
    print("the entered cahracter is uppercase")
else:
    print("the entered charcter is lowercase")
