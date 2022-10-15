import sys

def create():
	lst=[]
	limit=int(input("enter the size of the stack to be created: "))
	for i in range(limit):
		lst.append(int(input("enter the element to be intered in stack: ")))
	return lst

if __name__=="__main__":
	while True:
		print("what do you want to do?\n	1--> create the stack\n	2--> pop from stack\n	3--> display the stack\n	4--> exit")
		choice=int(input("	:: "))
		if choice==1:
			lst=create()
		elif choice==2:
			if len(lst)
			lst.pop()
		elif choice==3:
			print(lst)
		elif choice==4:
			sys.exit(0)
		else:print("wrong choice")
