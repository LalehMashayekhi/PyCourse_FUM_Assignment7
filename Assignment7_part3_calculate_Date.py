class Date:
    def __init__(self,year1,month1,day1,year2,month2,day2):
        self.year1=year1
        self.month1=month1
        self.day1=day1
        self.year2=year2
        self.month2=month2
        self.day2=day2
        self.result={"year":self.year1,"month":self.month1,"day":self.day1}
    def Is_Date_Valid(self):
        if 0<=self.month1<=12 and 0<=self.month2<=12 and 0<=self.day1<=30 and 0<=self.day2<=30:
            return True
        else:
            return False
    def Get_Month_Name(self):
        month_list=["Farvardin","Ordibehesht","Khordad","Tir","Mordad","Shahrivar","Mehr","Aban","Azar","Day","Bahman","Esfand"]
        for i in range(12):
            if self.month1==i+1:
                self.month=month_list[i]  
    def show(self):
        self.result={"year":self.year1 , "month":self.month , "day":self.day1}
        print(self.result["year"] , "/",self.result["month"] , "/" , self.result["day"])
    def add(self):
        while True:
            self.year2=int(input("Enter year:"))
            self.month2=int(input("Enter month:"))
            self.day2=int(input("Enter day:"))
            if Date.Is_Date_Valid(self)==True:
                day=self.day1+self.day2
                month=self.month1+self.month2
                year=self.year1+self.year2
                if day > 30:
                    day=day-30
                    month+=1
                while month>12:
                    month=month-12
                    year+=1
                self.day1=day
                self.month1=month
                self.year1=year
                break
            else:
                print("Please Enter a Valid Date")
    def sub(self):
        while True:
            self.year2=int(input("Enter year:"))
            self.month2=int(input("Enter month:"))
            self.day2=int(input("Enter day:"))
            if Date.Is_Date_Valid(self)==True:
                day=self.day1-self.day2
                month=self.month1-self.month2
                year=self.year1-self.year2
                if day < 0:
                    month-=1
                    day=30+day
                if month < 0:
                    year-=1
                    month=12+month
                self.day1=day
                self.month1=month
                self.year1=year
                break
            else:
                print("Please Enter a Valid Date")
while True:
    go_on=bool(input("Do you want to continue: 1/0: "))
    if go_on==0:
        break
    date_format=Date(0,0,0,0,0,0)
    print("Date")
    while True:
        date_format.year1=int(input("Enter year:"))
        date_format.month1=int(input("Enter month:"))
        date_format.day1=int(input("Enter day:"))
        if date_format.Is_Date_Valid()==True:
            while True:
                print("1.show")
                print("2.add")
                print("3.subtract")
                print("4.change the first date")
                op=input("Enter your Choice :")
                if op=="1":
                    date_format.Get_Month_Name()
                    date_format.show()
                elif op=="2":
                    date_format.add()
                    date_format.Get_Month_Name()
                    date_format.show()
                elif op=="3":
                    date_format.sub()
                    date_format.Get_Month_Name()
                    date_format.show()
                elif op=="4":
                    break
                else :
                    print("Please pick a number from the menu")
        else:
            print("Please Enter a Valid Date")