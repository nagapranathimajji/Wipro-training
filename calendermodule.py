from calendar import *
from datetime import *

Year=int(input("Enter the year: "))
Month=int(input("Enter the month: "))
str=month(Year, Month)
print(str)

#leap year or not?

if isleap(Year):
    print(Year,"is leap year")
else:
    print(Year,"is not leap year")

d=date.today()
print(d)
#d= date(1966,6,29)
for x in range(1,10):
    nextdate= d+timedelta(days=x)
    print(nextdate)