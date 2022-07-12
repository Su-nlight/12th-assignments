f=open("date.txt",'r')
temp=f.readlines()

print(" Last line of file is:\n {}\n Number of lines are {}".format(temp[-1],len(temp)))
