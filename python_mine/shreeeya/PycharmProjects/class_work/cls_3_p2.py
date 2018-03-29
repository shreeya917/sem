with open('some_file.txt','w') as fp:
    fp.write('hello world!')



l=["hello","there"]
with open('list.txt',"w") as fp:
    for each in l:
        fp.write(each)