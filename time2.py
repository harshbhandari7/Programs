import time

secs=time.time()
print('time : ',secs)

print('-------------------------------------')

time_tuple=time.localtime()
print("time tuple :",time_tuple)    #time tuple Indian standard time

print('-------------------------------------')

mytime=time.asctime()               #standard time format
print("my time is : ",mytime)

print("-------------------------------------")

mygmtime=time.gmtime()              #global time
print("gm time tuple : ",mygmtime)

print('-------------------------------------')

newtime=time.asctime(mygmtime)      #global standard time
print("new time is : ",newtime)

print('-------------------------------------')

print("the next will print with a delay of 2 seconds")
time.sleep(2)
print("printed after a delay of 2 seconds")
