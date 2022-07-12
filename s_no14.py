file1=open("source.txt",'r')
file2=open("target.txt",'w')

content=file1.readlines()
for i in content:
    if i.startswith("@")==True:
        file2.write(i.replace("@","")+'\n')
    else: continue
