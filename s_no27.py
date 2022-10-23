# a list contains following records 
stack=[]
def push_ele(records):
	global stack
	print(records)
	for i in records:
		print(i)
		if i[2] =="Goa":
			stack.append(i)
		else: continue

def pop_ele():
	global stack
	if len(stack)==0:
		print("stack empty")
	else: print(x for x in stack)
	
def display():
	global stack
	print(stack)
	
def make_records():
	rec=[]
	while True:
		name=input("Enter customer name: ")
		number=input("Enter Customer Number: ")
		city=input("Enter city of customer: ")
		rec.append([name,number,city])
		ch=input("you want to continue to add more records?(y/n) : ")
		if ch=="y": continue
		elif ch=="n": break
		else: print("wrong choice, so continuing")
		
		
	return rec
def main():
	records=make_records()
	print(records)
	while True:
		print("what do you want to do?\n1 for push_ele\n2 for pop_ele\n3 for displaying whole stack\n4 to exit")
		ch=int(input(" :: "))
		if ch==1:
			push_ele(records)
		elif ch==2:
			pop_ele()
		elif ch==3:
			display()
		else: break

if __name__=="__main__":
	main()
		
		
