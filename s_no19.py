f=open("abc.txt",'r')
temp=f.read()
counting=[0,0,0]

for i in temp:
    if i.islower()==True:
        counting[0]+=1
    elif i.isupper()==True:
        counting[1]+=1
    elif i.isdigit()==True:
        counting[2]+=1
    else: continue
    
print("Number of uppercase letters = {}\nNumber of lowercase letters = {}\nNumber of digits = {]".format(counting[1],counting[0],counting[2]))
