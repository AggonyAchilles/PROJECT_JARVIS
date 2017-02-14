import datetime


def main():
	startJarvis()

def startJarvis():
    greetIan()
    dateAndTime = datetime.datetime.today()
    dateAndTimeParser(dateAndTime)
    jarvisController()


#Greeting to Ian when JARVIS wakes up
def greetIan():
    print("Hello Ian")

#Makes a string of the datetime.datetime.today() and assings to variables
def dateAndTimeParser(string):
    string = str(string)
    year = string[0:4]
    month = string[5:7]
    month = monthParser(month)
    day = string[8:10]
    weekday = weekdayParser(datetime.datetime.today().weekday())
    time = string[11:19]

    #hour = string[11:13]
    #minute = string[14:16]
    #second = string[17:19]

    presentDateAndTime(year, month, day, weekday, time)

#Assings a month to the number of the month
def monthParser(month):

    if (month[0] == '0'):
        month = month[1]

    if (month == '1'):
        month = "Januari"
        return month

    elif (month == '2'):
        month = "Februari"
        return month

    elif (month == '3'):
        month = "March"
        return month

    elif (month == '4'):
        month = "April"
        return month

    elif (month == '5'):
        month = "May"
        return month

    elif (month == '6'):
        month = "June"
        return month

    elif (month == '7'):
        month = "July"
        return month

    elif (month == '8'):
        month = "Austust"
        return month

    elif (month == '9'):
        month = "September"
        return month

    elif (month == '10'):
        month = "October"
        return month

    elif (month == '11'):
        month = "November"
        return month

    else:
        month = "December"
        return month

#Assings a day to the number of the day
def weekdayParser(weekday):
    weekday = str(weekday)

    if (weekday == '0'):
        weekday = "Monday"
        return weekday

    elif (weekday == '1'):
        weekday = "Tuesday"
        return weekday

    elif (weekday == '2'):
        weekday = "Wednesday"
        return weekday

    elif (weekday == '3'):
        weekday = "Thursday"
        return weekday

    elif (weekday == '4'):
        weekday = "Friday"
        return weekday

    elif (weekday == '5'):
        weekday = "Saturday"
        return weekday

    else:
        weekday = "Sunday"
        return weekday

def presentDateAndTime(year, month, day, weekday, time):
    print("Today it is", weekday, month, day, year)
    print("The time is", time)

def jarvisController():
    string = ""
    while (string == ""):
        string = input("How can I be of service?: ")


main()