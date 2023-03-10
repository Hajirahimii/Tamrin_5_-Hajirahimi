# Hamid HajiRahimi
# Tamrin: 5-1
# SUM-Subtraction-Division Object-Oriented Programming (OOP)
############################################################


class Fraction:
    def __init__(self,s,m):
        if m==0:
            print("Makhraj must not be zero !" ) 
        self.soorat=s
        self.makhraj=m

############################################################

    def show(self):
       print(self.soorat,"/",self.makhraj)

############################################################
# SUM of 2 fractions:

    def sum(self,f1):
        result=Fraction(None,None)
        result.soorat=self.soorat*f1.makhraj+self.makhraj*f1.soorat
        result.makhraj=self.makhraj*f1.makhraj
        return result

############################################################
# Subtraction of 2 fractions:

    def subtraction(self,f1):
        result=Fraction(None,None)
        result.soorat=self.soorat*f1.makhraj-self.makhraj*f1.soorat
        result.makhraj=self.makhraj*f1.makhraj
        return result

############################################################
# Division of 2 fractions:

    def division(self,f1):
        result=Fraction(None,None)
        result.soorat=self.soorat*f1.makhraj 
        result.makhraj=self.makhraj*f1.soorat   
        return result

############################################################
# Print Result

faraction1=Fraction(3,5)
print("1st Fraction: " ) 
faraction1.show()
faraction2=Fraction(2,7)
print("2nd Fraction: " ) 
faraction2.show()
m=faraction1.sum(faraction2)
print("SUM of 2 fractions: " ) 
m.show()
tafrigh=faraction1.subtraction(faraction2)
print("Subtraction of 2 fractions: " ) 
tafrigh.show()
d=faraction1.division(faraction2)
print("Division of 2 fractions: " ) 
d.show()