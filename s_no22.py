import pickle
import os
import sys

class binary_handle:
	d={}
	filename=""
	def creating(self):
		f=open(self.filename,'ab')
		x=input("Enter number of records you want to enter: ")
		for i in range(x):
			key=input("Enter key: ")
			value=input("Enter value: ")
			self.d[key]=value
		pickle.dump(self.d,f)
	
	def reading(self):
		f=open(self.filename,'rb')
		return pickle.load(f)
	
	def deletion(self,key_value):
		try:
			f=open(self.filename,'rb')
			t=pickle.load(f).copy()
			for i in t:
				try:
					if i == key_value:
						t.pop(i)
					else:
						continue
				except EOFError:
					break
		except:
			print("some unexpected error has occurred")
		finally:
			os.remove(self.filename)
			f=open(self.filename,'wb')
			pickle.dump(t,f)
	
	def __init__(self):
		while True:
			try:
				print("1--> Creating a file\n2--> Reading a file\n3--> Deletion of an element of file\n4--> Exit")
				ch=int(input("Enter choice: "))
				if ch==1:
					self.filename=input("Enter filename: ").strip()
					self.creating()
				elif ch==2:
					self.filename=input("Enter filename: ").strip()
					x=self.reading()
					print("Content of file are:\n{}".format(x))
				elif ch==3:
					self.filename=input("Enter filename: ").strip()
					key=input("Enter key value you want to remove from file: ").strip()
					self.deletion(key_value=key)
				elif ch==4:
					sys.exit(0)
				else:
					print("No such choice")
			except ValueError:
				print("Provided choice is not integer")
			
binary_handle()		
