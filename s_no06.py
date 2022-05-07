class stuff:
    def vowels(self):
        vowel=['a','e','i','o','u']
        count=0
        for i in self.string:
            if i in vowel:
                count+=1
        return count

    def listinput(self):
        print("Enter your list values separated by commas (,): ")
        raw = input(": ")
        raw = raw.split(",")
        self.data = list(x.strip() for x in raw)

    def total(self):
        l = self.data
        total = 0
        for i in l:
            try:
                total += int(i)
            except:
                continue
        return total

    def loca(self):
        return self.data.index(self.ele)

    def occur(self):
        freq=0
        for i in self.data:
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
                self.string=input("Enter the String : ").lower()
                print("occurence of vowel is {}".format(self.vowels()))

            elif choice=='2':
                self.listinput()
                print("Sum of all elements in provided list is ",self.total())

            elif choice=='3':
                self.listinput()
                self.ele=input("enter the element: ").strip()
                print("{} in list is found at index = {}".format(self.ele,self.loca()))

            elif choice=='4':
                self.listinput()
                self.ele=input("enter the element: ")
                print("{} occurs {} times in list provided".format(self.ele,self.occur()))

            elif choice.lower()=='exit':
                flag=False

            else:
                print('Wrong Choice')

stuff()
