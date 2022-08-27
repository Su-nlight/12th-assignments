# this program is exam oriented.
import csv

def csvfile():
    f=open('abc.csv','w')
    fields=["Emp. no.","Emp. name","Designation","Basic Salary"]
    w_obj=csv.writer(f)
    w_obj.writerow(fields)
    n=int(input("Enter number of records you want to enter: "))
    for i in range(n):
        d={}
        for j in fields:
            d[j]=input("{}: ".format(j))
            
        w_obj.writerow(d.values())
        d.clear()
        
def readcsvfile():
    f=open("abc.csv",'r')
    r_obj=csv.reader()
    for i in r_obj:
        print(i)
