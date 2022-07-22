import pickle
import sys

def create_f(filename:str,m_admno:list,m_values:list):
	try:
		f1=open(filename, 'wb')
		d={}
		for i in m_admno:
			d[i]=m_values[i.index()]
		pickle.dump(f1,d)
		return {"process":"completed"}
	except:
		return {"process":"error"}

def read_f(filename):
	try:
		f1=open(filename,'rb')
		content=pickle.load(f1)
		return {"contents":content}
	except:
		return{"contents":False}
		
def main():
	while True:
		print("1 --> Create a file of data\n2 --> Read a file of data\n3 --> Exit the program")
		choice=int(input("Enter choice: "))
		f_name=input("Enter Filename: ").strip()
		if choice==1:
			admno=[]
			values=[]
			try:
				x=int(input("enter number of records you want to enter:"))
				for i in range(x):
					value=[]
					admno.append(input("Enter admno of record no.{}: ".format(i).strip()))
					value.append(input("Enter name of {}: ".format(admno[i])))
					value.append(input("Enter class of {}: ".format(admno[i])))
					value.append(input("Enter section of {}: ".format(admno[i])))
					value.append(input("Enter Roll number of {}: ".format(admno[i])))
					values.append(value)
				x=create_f(f_name,admno,values)
				if x["process"]!="error":
					print("process is completed")
				else: raise OSError
			except:
				print("Unexpected Error")
				
			finally:
				print("continuing program")
				continue
		
		if choice==2:
			f_name=input("Enter Filename: ").strip()
			cnt=read_f(f_name)["contents"]
			if cnt!=False:
				print(cnt)
			else: 
				print("Unexpected Error")
			
		if choice==3:
			sys.exit(0)
if '__name__'=='__main__':
	main()				
