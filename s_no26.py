import sys


def sel_sort(lst:list):
    num = len(lst)
    for i in range(num):
        x = lst[i:]
        minim = x[0]
        for n in x:
            if n < minim:
                minim = n
            else:
                pass

        print("\nstep {}".format(i+1))
        print("before", lst)
        lst.remove(minim)
        lst.insert(i, minim)
        print("after", lst)
    print(lst)

def main():
    while True:
        lst=list(eval(input("Enter integer list elements separated by commas : ")))
        sel_sort(lst=lst)
        ch=input("Rerun program? (y/n) :: ").strip()
        if ch=="n":
            sys.exit(0)
        else: continue

if __name__=="__main__":
    main()
