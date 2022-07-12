f=open("poem.txt", 'r')
t=f.readlines()

for i in t:
    x=i.split(" ")
    for j in x:
        if len(j)<=4:
            print(j)
