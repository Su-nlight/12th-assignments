class stuff:
    def vowels(self):
        vowel=['a','e','i','o','u']
        count=0
        for i in self.string:
            if i in vowel:
                count+=1
        return count

    def loca(self):
        return self.l1.index(self.ele)

    def occur(self):
        freq=0
        for i in self.l1:
            if i==self.ele:
                freq+=1
            else: continue
        return freq

    def __init__(self):
        flag = True
        while flag == True:
            print("""----------------------------------------------------------------------------------------------
                    1 -- Count the numbers of vowels from the given list.
                    2 -- To display sum of all numeric values from the list
                    3 -- To get an element from the user and display it's location from the list.
                    4 -- To get an element from the user and display it's number of occurence in the list.
                    exit -- To exit the program""")
            choice=input("Enter the program index that you wan to run : ")

            if choice=='1':
                self.string=input("Enter the String : ")
                print("occurence of vowel is {}".format(self.vowels()))

            elif choice=='2':
                l1=list(eval(input("Enter your numeric list elements separated by comma(,): ")))
                print("Sum of all elements in provided list is ",sum(l1))

            elif choice=='3':
                self.l1 = list(eval(input("Enter your numeric list elements separated by comma(,): ")))
                self.ele=eval(input("enter the element: "))
                print("{} in list is found at index = {}".format(self.ele,self.loca()))

            elif choice=='4':
                self.l1 = list(eval(input("Enter your numeric list elements separated by comma(,): ")))
                self.ele=eval(input("enter the element: "))
                print("{} occurs {} times in list provided".format(self.ele,self.occur()))

            elif choice.lower()=='exit':
                flag=False

            else:
                print('Wrong Choice')

stuff()
