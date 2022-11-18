def isempty(tocheck):
    if tocheck.strip() == "": return True
    else: return False

class students:
    name = []
    def __init__(self):
        try:
            self.n = int(input("Enter value of n: "))
            self.add_name()
            self.name = tuple(self.name)
            print(self.name)
        except ValueError:
            print("Provided value of n is not valid, retry again...")
            students()
    def does_exists(self, name1):
        if name1 in self.name: return True
        else: return False
    def add_name(self):
        i=0
        while i<self.n:
            newname = input("Enter name of student {}: ".format(i + 1))
            if isempty(newname) == True:
                print("The name entered is blank so it is not acceptable")
            elif self.does_exists(name1=newname) == True:
                print("Student already does exist in the tuple")
            else:
                self.name.append(newname)
                print(newname, "is added to the tuple")
                i+=1

students()
