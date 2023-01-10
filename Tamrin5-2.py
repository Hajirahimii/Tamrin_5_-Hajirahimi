# Hamid HajiRahimi
# Tamrin: 5-2
# 1- SUM-Subtraction Time (Do not be negative) with Object-Oriented Programming (OOP)
# 2- Convert Second to time and time to Second
############################################################

class Time:
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
############################################################

    def show(self):
        print(self.h,":",self.m,":",self.s)

############################################################
# Jam'E 2 time:

    def sum(self,t2):
        result=Time(None,None,None)
        result.h=self.h+t2.h
        result.m=self.m+t2.m
        result.s=self.s+t2.s
        if result.s >= 60:
           result.s-=60
           result.m+=1
        if result.m >= 60:
           result.m-=60
           result.h+=1    
        return result
############################################################
# Tafrigh'E 2 time:

    def Subtraction(self,t2):
        result=Time(None,None,None)
        result.h=self.h-t2.h
        result.m=self.m-t2.m
        result.s=self.s-t2.s  
        if result.s<0:
            result.s+=60
            result.m-=1
        if result.m<0:
            result.m+=60
            result.h-=1
        return result

############################################################
# Convert time to seconds:

    def conv(self):
        convert=self.h*3600+self.m*60+self.s
        return convert

############################################################
# Convert Second to time:

def conv1(self):     
    hour=int(self/3600)  
    min=int((self-hour*3600)/60)
    second=int((self-hour*3600-min*60))
    return [hour,min,second] 

time_1={"h":11,"m":37,"s":12}
print("Time_1 : " , time_1 ) 
time_1=Time(11,37,12)

time_2={"h":8,"m":45,"s":52}
print("Time_2 : ", time_2 ) 
time_2=Time(8,45,52)
second_2=55000

############################################################
# Print Jam'E 2 time:

s=time_1.sum(time_2)
print("Sum of 2 Times (Hour/Minute/Second): " ) 
s.show()

############################################################
# Print Tafrigh'E 2 time:

sub=time_1.Subtraction(time_2)
print("Subtraction of 2 Times (Hour/Minute/Second): " ) 
sub.show()

############################################################
#Time Convert to Seconds

second_1=time_1.conv()
print("Time Convert to Seconds:  \n" "Time Equal To= " , second_1 ,"Seconds" ) 

############################################################
#Seconds Convert to Time

time=conv1(second_2)
print("Seconds Convert to Time :" ) 
time_={"h":time[0],"M":time[1],"S":time[2]}
print(time_)