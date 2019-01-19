fp=open('data.txt','w')

'''first it checks for file,if file is not present, it will create a file and
perform the operatrion only in write and append mode'''

#In read mode ,if file is not present,it will result in error

#file reference
print("file refernce :",fp)

#file refernce type
print("refernce type :",type(fp))

fp.close()
print("File closed :",fp.closed)  #it will return true if file is closed
