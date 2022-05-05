def freqoele(lst, element):
        frequency = 0
        for x in lst:
            if x == element:
                frequency += 1
            else:
                continue
        return frequency

lst=[]                     # your list of integers goes here in the bracket
n=int(input("Enter the element you want to find occurence of : "))
print("frequency of {} in list is {}".format(n,freqoele(lst,n)))
