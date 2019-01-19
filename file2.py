fp=open("data.txt",'w')
data="This is a file handling program"
fp.write(data)
fp.close


#fetchin file content
fp=open("data.txt",'r')
data=fp.read()
print("content of file is :",data)
fp.close()
