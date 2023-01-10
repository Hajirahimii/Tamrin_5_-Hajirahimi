# Hamid HajiRahimi
# Tamrin: 5-3
# SUM-Subtraction date (Do not be negative) with Object-Oriented Programming (OOP)

############################################################

class Date:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

############################################################

    def show(self):
        print(self.y, "/", self.m, "/", self.d)

############################################################
#Jam'E 2 Dates:

    def sum(self, d2):
        result = Date(None, None, None)
        result.y = self.y + d2.y
        result.m = self.m + d2.m
        result.d = self.d + d2.d

        if result.d >= 30:
            result.d -= 30
            result.m += 1

        if result.m >= 12:
            result.m -= 12
            result.y += 1

        return result

############################################################
#Tafrigh'E 2 Dates:


    def subtraction(self, d2):
        result = Date(None, None, None)
        result.y = d2.y - self.y
        result.m = d2.m - self.m
        result.d = d2.d - self.d

        if result.d < 0:
            result.d += 30
            result.m -= 1

        if result.m < 12:
            result.m += 12
            result.y -= 1

        return result

############################################################
# Get_Month_Names:


    def Get_Month_Name (self):
        
        if self.m == 1: 

            month="FARVARDIN"

        elif self.m == 2:
            month = "ORDIBEHESHT"
        elif self.m == 3:
            month ="KHORDAD"

        elif self.m == 4:
            month = "TIR"

        elif self.m == 5:
            month = "MORDAD"

        elif self.m == 6:
            month = "SHAHRIVAR"

        elif self.m == 7:
            month = "MEHR"

        elif self.m == 8:
            month = "ABAN"

        elif self.m == 9:
            month = "AZAR"            

        elif self.m == 10:
            month = "DEY"

        elif self.m == 11:
            month = "BAHMAN"

        elif self.m == 12:
            month = "ESFAND"           

        return month

        
############################################################

############################################################
# Is Valid Date:



    def Is_Valid_Date (self):
        
        if self.d < 1 or self.d > 31: 

            day=("False Day")
            return day

        if self.m < 1 or self.m > 12: 

            month=("False month")
            return month

        if self.y < 1 or self.y > 9999: 

            year=("False Year")
            return year
        
Date_1 = Date(1399,10,19)
Date_2 = Date(1401,6,9)
############################################################
# Print Result:

print("1st Date (Year/Month/Day): ")
Date_1.show()

print("2nd Date (Year/Month/Day):")
Date_2.show()

s = Date_1.sum(Date_2)
print("Sum of 2 Dates (Year/Month/Day) : ")
s.show()

Subtraction = Date_1.subtraction(Date_2)
print("Subtraction of 2 Dates (Year/Month/Day) : ")
Subtraction.show()

Month_Name = Date_2.Get_Month_Name()
print("Month of Date: ", Month_Name)

Valid_date = Date_1.Is_Valid_Date()
print("False Input in Date_1:",   Valid_date)

Valid_date = Date_2.Is_Valid_Date()
print("False Input in Date_2:",   Valid_date)