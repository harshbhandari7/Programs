def add(p):
    print("a inside function is ",a)
a=10
print("a outside the function is ",a)
add(a)

def add():
    a=20
    print("a inside function",a)
a=10
print("a outside function",a)
add()
