import pickle
import sys

def make_file():
    x=input("Enter name of file without Extension : ").strip()
    l=[]
    f1 = open(x + ".dat", 'wb')
    flag=True
    while flag==True:
        l.append(input("Enter content of file : "))
    pickle.dump(f1,l)

def read_file():
    x=input("Enter filename without extension").strip()
    f1=open(x+".dat",'rb')
    content=pickle.load(f1)
    print(content)

def main():
    print("1 --> Create a Binary file\n2 --> Read a Binary file\n3 --> Exit the program")
    try:
        ch=int(input("Enter Choice: "))
        if ch==1:
            make_file()
        elif ch==2:
            read_file()
        elif ch==3:
            sys.exit(0)
        else:
            print("Invalid choice")
    except ValueError:
        print("Choice is not an integer")
    except:
        sys.exit(1)
    
if "__name__"=="__main__":
    main()
