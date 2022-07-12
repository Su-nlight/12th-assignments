def write1():
  f=open("daynote.txt",'w')
  flag=True
  while flag==True:
    msg=input("Enter line : ")
    if msg=="exit":
      flag=False
    else:
      f.write(msg+'/n')

write1()
