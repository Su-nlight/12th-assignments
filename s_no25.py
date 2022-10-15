import sys

def create():
    global lst
    global limit
    limit=int(input("enter the size of the stack to be created: "))
    for i in range(limit):
        lst.append(int(input("enter the element to be entered in stack: ")))
def push():
    global lst
    if len(lst)<limit:
        lst.append(int(input("enter the element to be entered in stack: ")))
    else: print("stack overflow")

def pop():
    global lst
    lst=lst[0:len(lst)-1]

def display():
    global lst
    print(lst)
    
def main():
    while True:
        print("what do you want to do?\n	1--> create new stack\n 2--> push to stack\n    3--> pop from stack \n	4--> display the stack \n 5-->  exit")
        choice = int(input("	:: "))
        func={1:create,2:push,3:pop,4:display,5:sys.exit}
        if choice in func.keys():
            func[choice]()
        else: print("wrong choice")

if __name__=="__main__":
    limit = 0
    lst = []
    main()
