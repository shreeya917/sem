#File handling
fp=open("d:\\new_test.txt","w")
print(fp)


fp.write("hello world")
fp.write("..... and again")
fp.close()

fp=open("new_test","r")
print(fp)
fp.close()

fp=open("d:\\test.txt","w")
print(fp)
fp.write("hello")

fp=open("test.txt","a")
print(fp)

fp.write("appending")
fp.close()


fp=open("new.text","w")
fp.write("hello world")
fp.tell()
fp.close()


