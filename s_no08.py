f=open("diary.txt", 'r')
flag=True
while flag==True:
  temp = f.readline()
  if temp.lower().startswith('p') == True:
    print(temp)
  elif temp.strip() == "":
    flag = False
  else:
    continue
