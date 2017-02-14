import datetime
import webbrowser

class Jarvis():
	#Boots Jarvis
	def __init__(self):
		self.name = "Jarvis"
		self.dateAndTimeConfiguration()
		self.presentDateAndTime(self.weekday, self.day, self.month, self.year, self.time, self.hour, self.partOfTheDay)
		self.jarvisControlCenter()

	#Configures the date and time so it is always up to date
	def dateAndTimeConfiguration(self):
		self.dateAndTime = str(datetime.datetime.today())
		self.year = self.dateAndTime[0:4]
		self.month = self.dateAndTime[5:7]
		self.monthParser(self.month)
		self.day = self.dateAndTime[8:10]
		self.weekday = datetime.datetime.today().weekday()
		self.weekdayParser(self.weekday)
		self.time = self.dateAndTime[11:19]
		self.hour = self.dateAndTime[11:13]
		self.partOfTheDay = self.getPartOfTheDay(self.hour)


	#Assings the month to the number of the month(Januari/Februari/March/April/May/June/July/August/September/October/November/December)
	def monthParser(self, month):

		month = int(month)
		
		monthList = ["January", "Februari", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

		self.month = monthList[month-1]


	#Assings weekday to the day (Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday)
	def weekdayParser(self, weekday):

		weekdayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

		self.weekday = weekdayList[weekday]

	#Presents date and time, as the part of the day
	def presentDateAndTime(self, weekday, day, month, year, time, hour, partOfTheDay):
		print("Today it is", weekday, month, day, year)
		print("The time is", time)
		print("It is currently:", partOfTheDay)

	#Gets the part of the day (early morning/late morning/early afternoon/late afternoon/early evening/late evening/night)
	def getPartOfTheDay(self, hour):

		hour = int(hour)
		
		if ((hour >= 6) and  (hour < 9)):
			return "Early morning"

		elif ((hour >= 9) and  (hour < 12)):
			return "Late morning"

		elif ((hour >= 12) and  (hour < 15)):
			return "Early afternoon"

		elif ((hour >= 15) and  (hour < 18)):
			return "Late afternoon"

		elif ((hour >= 18) and  (hour < 21)):
			return "Early evening"

		elif ((hour >= 21) and  (hour < 00)):
			return "Late evening"

		else:
			return "Night"

	#Control center, here is where the magick happens. JARVIS asks for input and manages it
	def jarvisControlCenter(self):

		string = "fries"
		#webbrowser.open('https://www.google.be/?gfe_rd=cr&ei=U1-jWNauLYHEXsK_nJAH&gws_rd=ssl#q='+string)	Open a browser
		string = input("How can I be of your service: ")
	

		print(string)

	       

jarvis = Jarvis()


