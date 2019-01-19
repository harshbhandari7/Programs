#Methods of list
#REVERSE()
l1=['sd','ds','dd','ad','fd','hg']
l2=[1,2,3,4,5,6,7]
print("the lists are")
print(l1)
print(l2)
print("the reverse of list is",l1.reverse())
print("the reverse of list is",l2.reverse())
print(l1)
print(l2)

#SORT()
l3=[53,35,22,5,554,35]
l3.reverse()
l4=l3
print(l4)
print(l3)
print(id(l3))
print(id(l4))

#POP()
l5=[30,20,54,51,4,95,78,47]
print("before pop",l5)
l5.pop()
print("after pop",l5)

#INSERT(INDEX,VALUE)
l6=[1,2,3]
print(l6)
print("list after insertion")
l6.insert(1,4)
print(l6)

#APPEND()       appends value at last index
l7=[1,2,3,4]
print(l7)
print("after append")
l7.append(5)
print(l7)







