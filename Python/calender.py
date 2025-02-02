import calendar

print(calendar.TextCalendar(firstweekday=6).formatyear(2015))
print(calendar.firstweekday())
print(calendar.isleap(2015))  #To check if a year is a leap year

for i in range(calendar.leapdays(2000, 2025)):  #To print leap years between 2000 to 2025
    print(i)
    
print(calendar.weekday(2015, 12, 31))  #To print the day of the week for a given date


def weekDay(y, m, d):
    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    print(days[calendar.weekday(y, m, d)])

if __name__ == "__main__":
    m, d, y = map(int, input().split()) #input: 08 05 2015
    weekDay(y, m, d) 
        

