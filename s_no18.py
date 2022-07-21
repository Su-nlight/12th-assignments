vowel=['a','e','i','o','u']

f=open("idksomething.txt","r")
t=f.read().lower()
count=0
for i in t:
	if i in vowel:
		print(i,count)
		count+=1
	else: continue
	
print("Number of vowels in file are",count)
