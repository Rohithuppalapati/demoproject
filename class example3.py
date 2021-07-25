# Create a Time class and initialize it with hours and minutes.
# 1. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# 2. Make a method displayTime which should print the time.
# 3. Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.

# answers @ https://www.codesdope.com/practice/python-your-class/

class Time1():
    def __init__(self,hours,minutes):
        self.hours=int(hours)
        self.minutes=int(minutes)

    def displayTime(self):
        print(f'current time is {self.hours} hours and {self.minutes} minutes')

    def DisplayMinute(self):
        m=self.hours*60 + self.minutes
        print(f'time in minutes {m}')

    def addTime(t1, t2):
        t3 = Time1(0,0) # creating new object
        t3.hours = t1.hours + t2.hours # sum of hours
        t3.minutes = t1.minutes + t2.minutes # sum of minutes
        while t3.minutes >= 60:
            t3.hours += 1
            t3.minutes -= 60
        return t3


time1=Time1('4','34')
time2=Time1(5,40)

time1.displayTime()
print()
time2.displayTime()

print()
time2.DisplayMinute()
print()
time1.DisplayMinute()

print()
#result=Time1.addTime(time1,time2)
#print(result)
