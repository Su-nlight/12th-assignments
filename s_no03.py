data=dict()

n=int(input("Enter number of employes you want to enter: "))
for x in range(n):
    name=input("Enter name of employee no.{}: ".format(x+1))
    if name.replace(" ","").isalpha()==False:
        raise ValueError
    else:
        salary=int(input("Enter salary of {}: ".format(name)))
        data[name]=salary

print(data)
