class Proper_Fractions:
    
    #Note: the numerator can be an integer, the denominator - natural
    
    def __init__(self, num, den):
        
        self.num = num
        self.den = den
    
    def example(self):

        print(f"Example of proper fraction: {self.num}/{self.den}")
    
    def check_fraction(self):
        
        if self.den != 0:
            
            if (self.num/self.den) >= 1:
                
                print("This is not proper fraction")
                
            else:
                
                print("Good. You can continue")
            
        else:
            
            print("Error")

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def display_all(self):
        
        print(f"General view of the fraction: {self.num}/{self.den}")

    def __add__(self,other):
        
        newnum = self.num*other.den + self.den*other.num
        newden = self.den * other.den
        return Proper_Fractions(newnum,newden)

    def __sub__(self,other):
        
        newnum = self.num*other.den - self.den*other.num
        newden = self.den * other.den
        return Proper_Fractions(newnum,newden)

    def __mul__(self,other):
        
        newnum = self.num * other.num
        newden = self.den * other.den
        return Proper_Fractions(newnum,newden)
 
    def __del__(self):
        print("Class deleted")

def look(f1, f2):
    print("Sum:", f1 + f2)
    print("Difference:", f1 - f2)
    print("Product:", f1 * f2)

class Fractions(Proper_Fractions):
    
    def get_info(self):
        
        print (f"The mixed fraction : {self.num // self.den} and {self.num % self.den}/{self.den}")

    def __add__(self,other):
        
        newnum = self.num*other.den + self.den*other.num
        newden = self.den * other.den
        return Proper_Fractions(newnum,newden)

    def __sub__(self,other):
        
        newnum = self.num*other.den - self.den*other.num
        newden = self.den * other.den
        return Proper_Fractions(newnum,newden)

    def __mul__(self,other):
        
        newnum = self.num * other.num
        newden = self.den * other.den
        return Proper_Fractions(newnum,newden)

def look(f3, f4):
    print("Sum:", f3 + f4)
    print("Difference:", f3 - f4)
    print("Product:", f3 * f4)  

    
f1 = Proper_Fractions(1, 3)
f2 = Proper_Fractions(5, 7)
f3 = Fractions(6, 4)
f4 = Fractions(15, 2)
f5 = Proper_Fractions(1, 2)
