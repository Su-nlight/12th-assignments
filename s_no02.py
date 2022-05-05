n=float(input("Enter the number of whose table you want : "))
a=int(input("Enter the natural number till you want to see {}'s table : ".format(n)))

for i in range(1,a+1):
    print("{0} * {1} = {2}".format(n,i,n*i))
