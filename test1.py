s1=int(input("Enter s1 "))
s2=int(input("Enter s2 "))
s3=int(input("Enter s3 "))
s4=int(input("Enter s4 "))
s5=int(input("Enter s5 "))
count=0
list=[s1,s2,s3,s4,s5]
for i in range(0,len(list)):
   if list[i]<33:
       count=count+1
if count==0:
    print("pass")
elif count==1:
    print("grace pass")
elif count==2:
    print("Supplementry")
elif count==3:
    print("Fail")
