
def push(diction):
    global stack
    for i in diction.keys():
        if diction[i]>=70:
            stack[i]=diction[i]
        else: continue

def pop_display():
    global stack
    try:
        stack.pop(list(stack.keys())[-1])
        print(stack)
    except IndexError:
        print("stack is empty.")

def values():
    flag = 0
    diction={}
    while flag < 5:
        name = input("Enter name of student: ")
        marks = int(input(f"Enter marks of {name}: "))
        diction[name] = marks
        flag += 1
    return diction

def main():
    diction=values()
    flag=True
    while flag==True:
        print("What do you want to do?\n 1--> push into stack\n 2--> pop and display the stack\n 3--> Re-enter values\n 4-->exit")
        ch=int(input("   :: "))
        if ch==1:
            push(diction=diction)
        elif ch==2:
            pop_display()
        elif ch==3:
            diction.clear()
            diction=values()
        elif ch==4:
            flag=False
        else:
            print("Wrong choice.\nRepeating process.")


if __name__=="__main__":
    stack={}
    main()
