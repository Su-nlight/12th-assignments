class freq:
    def freqoele(self, lst, element):
        frequency = 0
        for x in lst:
            if x == element:
                frequency += 1
            else:
                continue
        return frequency

    def freqoall(self, lst):
        frequency = {}
        for x in lst:
            if x in frequency:
                frequency[x] += 1
            else:
                frequency[x] = 1
        return frequency

    def __init__(self):
        trial=input("Enter your list elements seperated by only comma(,) : ")
        list1=list(int(x) for x in trial.split(","))
        ch=int(input("""Enter your choice as given by the following\n
                    \t1 if you want frequency of particular element\n
                    \t2 if you want frequency of all element\n
                    \t : """))
        if ch==1:
            element=int(input("Enter the element that you want to find frequency of : "))
            print("{} occurs {} times in list provided".format(str(element),str(self.freqoele(lst=list1,element=element))))
        elif ch==2:
            print(self.freqoall(lst=list1))
        else:
            print("Such choice does not exist.")

freq()