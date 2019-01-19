#function overloading
def pro(a,*tup):
    for element in tup:
        a*=element
    print("the product of Numbers is",a)
pro(5)
pro(5,2)
pro(5,5,5,5)
