from calendar import *
class MyDate:
    # def __init__(self, day,month,year):
    #     self.day = day
    #     self.month = month
    #     self.year = year
    day =0
    month =0
    year =0
    def addDays(self, day):
        self.day = day
    def addMonths(self,month):
        self.month = month
    def addYears(self,year):
        self.year = year
    def weekday(self):
        wkday = weekday(self.year,self.month,self.day)
        print(day_name[wkday])
    def diffDates(self,day,month,year):
        print("Days",abs(day-self.day),"Month",abs(month-self.month),"Year",abs(year-self.year))

dat = MyDate()
dat.addDays(27)
dat.addMonths(7)
dat.addYears(2025)
dat.weekday()
dat.diffDates(25,8,2026)

