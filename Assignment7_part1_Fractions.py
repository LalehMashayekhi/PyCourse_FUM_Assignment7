class Fraction:
    def __init__(self, n,d):
        self.numerator=n
        self.denominator=d
    def show(self):
        print(self.numerator, "/", self.denominator)
    def addition(self, f):
        result=Fraction((self.numerator*f.denominator) + (f.numerator*self.denominator) , (self.denominator*f.denominator) )
        return result
    def subtraction(self,f):
        result=Fraction((self.numerator*f.denominator) - (f.numerator * self.denominator) , (self.denominator*f.denominator))
        return result
    def mult(self, f):
        result=Fraction( (self.numerator * f.numerator) , (self.denominator* f.denominator))
        return result
    def division(self, f):
        if f.numerator==0:
            print("Undefined, devived by zero!!! ")
            return None
        else: 
            result=Fraction((self.numerator * f.denominator),(self.denominator * f.numerator) )
            return result

while True:
    go_on=bool(input("For exit enter 0 (1 or 0): "))
    if go_on==0:
        break
    else:
        f1=Fraction(None,None)
        f1.numerator=int(input("Enter a number as the numerator of the fraction: "))
        f1.denominator=int(input("Enter a number as the denomerator of the fraction: "))
        f2=Fraction(None,None)
        f2.numerator=int(input("Enter a number as the numerator of the fraction: "))
        f2.denominator=int(input("Enter a number as the denomerator of the fraction: "))
        while f1.denominator ==0 or f2.denominator==0: 
            if f1.denominator ==0:
                print("Enter another number as first fractions denominator: ")
                f1.denominator=int(input("Enter a number as the denomerator of the fraction: "))
            elif  f2.denominator ==0:
                print("Enter another number as second fractions denominator: ")
                f2.denominator=int(input("Enter a number as the denomerator of the fraction: "))
            
        f1.show()
        f2.show()
        a=f1.addition(f2)
        a.show()

        m=f1.mult(f2)
        m.show() 

        s=f1.subtraction(f2)
        s.show()

        d=f1.division(f2)
        d.show()






























"""
class Person:
    name = None
    family = None
    city = None
    age = None
    
    # def programming():
    #     pass
    # def hobbies():
    #     pass
    
person1= Person()  #defining an object from the class
person2=Person() 

person1.age=20
person1.name="Neda"
person2.age=200
person2.name="Nedaa"
"""



