def demo(a,*tup):
    print("a referes to the first reference ",a)
    print("tup referes to rest of the references",tup)
demo(10)
demo(10,20,30)
demo(20,20,50,9,0,520)


def add(a,*tup):
    print("The sum of numbers")
    for element in tup:
        a+=element
    print("result is",a)
add(10)
add(10,20)
add(10,20,30,40)
