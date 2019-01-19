#identity operator
#is ,is not
#these operators are used to make a comparison between the identities of operators.
a=10
print("id of a is ",id(a))
b=5
print("id of b is ",id(b))
res=a is b
print("result is",res)

#if data is same,then reference will be same
'''we can prove the above statement by assigning same value(data) to 2 different variables,as values are same their
id will also be same'''
c=10
print("c is",c,"id of c is",id(c))
d=10
print("d is",d,"id of d is",id(d))
