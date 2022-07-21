def remove_lowercase():
	file_name=input("enter name of source file: ").strip()
	file1=open(filename,'r')
	cnt=file1.readlines()
	file_name=input("enter name of target file: ").strip()
	file2=open(filename, 'w')
	
	for i in cnt:
		if i.strip()[0].islower()!=True:
			file2.write(i)
		else: continue

remove_lowercase()
