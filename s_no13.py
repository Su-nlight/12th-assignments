f=open('abc.txt','r')
counting=0
flag=True
while flag==True:
    temp=f.readline().lower()
    temp1=temp.split(" ")
    for i in temp1:
        if i.strip()=='my':
            counting+=1
        else: continue

print("number of occurrence is : ",counting)
