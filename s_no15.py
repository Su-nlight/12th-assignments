f=open("poem.txt",'r')
temp=f.readlines()
counting= [0,0]

for i in temp:
	counting[0]+=i.strip().lower().count("to")
	counting[1]+=i.strip().lower().count("the")
print("Number of occurences of 'to' is{}\noccurences of 'the' is {}".format(counting[0],counting[1]))
