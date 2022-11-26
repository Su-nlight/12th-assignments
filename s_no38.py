import pickle

def modify():
    f=open("SMarks.dat", 'rb')
    temp=pickle.load(f)
    f.close()
    mod=int(input("What do you want to modify??\n"
                  "1.Roll number of the student\n"
                  "2.Name of the student 3. Total Marks\n"
                  "4.Number of subjects\n"))
    if mod==1:
        rold=int(input("Enter existing/wrong roll number"))
        rnew=int(input("Enter correct roll number"))
        temp[rnew]=temp[rold]
        del temp[rold]
        f=open("SMarks.dat",'wb')
        print("Record has been updated", temp)
        pickle.dump(temp,f)
        f.close()
    elif mod ==2:
        r=int(input("Enter roll number of the student"))
        nnew=input("Enter new name of the student")
        for i in temp.keys():
            if i == r:
                temp[i][0] = nnew
        f = open("SMarks.dat", 'wb')
        print("Record has been updated", temp)
        pickle.dump(temp, f)
        f.close()
    elif mod == 3:
        r = int(input("Enter roll number of the student"))
        mnew = int(input("Enter total marks of the student"))
        for i in temp.keys():
            if i == r:
                temp[i][1] = mnew
        f = open("SMarks.dat", 'wb')
        print("Record has been updated", temp)
        pickle.dump(temp, f)
        f.close()
    elif mod == 4:
        r = int(input("Enter roll number of the student"))
        snew = input("Enter number of subjects of the student")
        for i in temp.keys(): 
            if i == r:
                temp[i][2] = snew
        f = open("SMarks.dat", 'wb')
        print("Record has been updated", temp)
        pickle.dump(temp, f)
        f.close()

modify()
