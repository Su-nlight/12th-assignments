import sys


class basic_maths:
    attempt = 0
    def inputvari(self):
        try:
            x=int(input("Enter value of x: "))
            y=int(input("Enter value of y: "))
            return x,y
        except ValueError:
            if self.attempt<3:
                print("Value Error has occured, Retry entering values. {} attempts left".format(3-self.attempt))
                self.attempt+=1
                return self.inputvari()
            elif self.attempt==3:
                print("No attemts left, rerun the program")
                sys.exit(0)
    def sumof2(self):
        x,y=self.inputvari()
        return x+y
    def differenceof2(self):
        x, y = self.inputvari()
        return x-y
    def multiplyof2(self):
        x, y = self.inputvari()
        return x*y
    def divideof2(self):
        x, y = self.inputvari()
        if y==0:
            return ("Can not divide by zero") 
        else:
            return x/y

    def __init__(self):

        print("\n--- Initiating basic_maths module ---\n")
        print("Please input what function you want to execute \n"
              "\t1 --> Sum of provided 2 numbers (x+y)\n"
              "\t2 --> Difference of 2 numbers (x-y)\n"
              "\t3 --> Product of 2 numbers (x*y)\n"
              "\t4 --> Quotient of 2 numbers (x/y)\n")
        choice=input("\t\t: ")
        func = {"1": self.sumof2, "2": self.differenceof2, "3": self.multiplyof2, "4": self.divideof2}
        if choice in func.keys():
            print(func[choice]())
        else:
            print("Such function doesn't exist") 

basic_maths()
