import datetime       #Times, dates, etc
import webbrowser     #Webstuff
import urllib.request #Checking internetconnection etc
import os


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

		self.options()
		chosenOption = (input("Option (number): "))
		#webbrowser.open('https://www.google.be/?gfe_rd=cr&ei=U1-jWNauLYHEXsK_nJAH&gws_rd=ssl#q='+string)	Open a browser
		while (self.optionIsValid(chosenOption) == False):
			print("That is not possible Ian")
			chosenOption = int(input("Option (number): "))

		self.optionsController(chosenOption)

	#Displays the several options JARVIS can do
	def options(self):
		print("Would you like me to:")
		print("(1) Google something")
		print("(2) Open a website")

		print("(3) Play music")
		print("(4) Put on the radio")
		#To be added

	#Acceps an url or a term and opens the website
	def openWebsite(self):

		websiteQuery = input("Enter a specific url or name the website: ")

		if (websiteQuery[0:3] == "www"):
			webbrowser.open('http://' + websiteQuery)
			

		elif (websiteQuery[0:7] == "http://"):
			webbrowser.open(websiteQuery)
			

		else:
			webbrowser.open('http://www.' + websiteQuery + '.com')
			
	#Opens Google
	def googleSomething(self):

		query = self.queryParser()
		webbrowser.open('http://www.google.be/?gfe_rd=cr&ei=U1-jWNauLYHEXsK_nJAH&gws_rd=ssl#q='+query)

	#Accepts input and changes all the spaces into '+'
	def queryParser(self):

		query = input("What would you like me to google: ")

		newQuery = ""

		for i in range(len(query)):
			if (query[i] == ' '):
				newQuery += '+'
			else:
				newQuery += query[i]

		return newQuery


	#Controls and calls the correct functions
	def optionsController(self, option):

		if (option == '1'):
			self.googleSomething()
			self.jarvisControlCenter()

		elif (option == '2'):
			self.openWebsite()
			self.jarvisControlCenter()

		elif (option == '3'):
			self.playMusic()
			self.jarvisControlCenter()

		elif (option == '4'):
			self.putOnTheRadio()
			self.jarvisControlCenter()

		else:
			print("JARVIS is shutting down ....")
			exit()

	#Checks wether an option is valid or not
	def optionIsValid(self, option):

		optionList = ['0', '1', '2', '3', '4']

		if option in optionList:
			return True

		else:
			return False

	#Controls wether JARVIS has an active internet connection
	def internet_on(self):
		try:
			urllib.request.urlopen('http://www.google.com', timeout=1)
			return True
		except urllib.request.URLError as err:
			return False

	#Function that plays the music when asked for
	def playMusic(self):
		if (self.internet_on()):
			webbrowser.open('https://www.youtube.com/watch?v=U9FzgsF2T-s&list=PL4UGiGyQzjtnA6M-GflE4RUQm5wrCv8HZ')

		else:
			os.startfile('C:/Users/Ian/Desktop/Development/PROJECT_JARVIS/music/Ghost-Elizabeth.mp3')

	def putOnTheRadio(self):
		if (self.internet_on()):
			radio = input("Wich radio would you like to listen to: ")
			self.activateTheCorrectRadio(radio)


		else:
			print("There is no active internet connection, therefore I cannot put on the radio.")

	#Function that sorts out wich radio should be put on
	def activateTheCorrectRadio(self, radio):
		if (self.radioStuBru(radio)):
			webbrowser.open('http://radioplus.be/#/stubru/herbeluister')

		elif (self.radioQMu(radio)):
			webbrowser.open('http://qmusic.be/')

		elif (self.radioJoe(radio)):
			webbrowser.open('http://joe.be/live/joe')

		elif (self.radioNostalgie(radio)):
			webbrowser.open('http://www.radioviainternet.be/radio-nostalgie')

		#Add more radios

		else:
			print("I couldn't find the radio in my database, but I can search for it on google for you instead.")
			webbrowser.open('http://www.google.be/?gfe_rd=cr&ei=U1-jWNauLYHEXsK_nJAH&gws_rd=ssl#q=' + radio)

	#Hulpfunction activateTheCorrectRadio(self, radio) for Studio Brussel
	def radioStuBru(self, radio):
		stuBruList = ["Studio Brussel", "Stu Bru", "stu bru", "stubru", "StuBru", "Stubru", "stuBru", "studio brussel", "Studio brussel", "STUDIOBRUSSEL", "STUDIO BRUSSEL"]
		
		if radio in stuBruList:
			return True

		else:
			return False

	#Hulpfunction activateTheCorrectRadio(self, radio) for Q-Music
	def radioQMu(self, radio):
		qMuList = ["QMusic", "Q-music", "Qmusic", "qmusic", "qMusic", "q-music", "q-Music", "QMUSIC"]

		if radio in qMuList:
			return True

		else:
			return False

	#Fulpfunction activateTheCorrectRadio(self, radio) for Joe FM
	def radioJoe(self, radio):
		joeList = ["Joe", "joe", "JOEFM", "JoeFm", "joefm", "JoeFM", "joe fm", "joe-fm", "Joe FM", "Joe-FM"]

		if radio in joeList:
			return True

		else:
			return False

	#HulpFunction activateTheCorrectRadio(self, radio) for Nostalgie
	def radioNostalgie(self, radio):
		nostalgieList = ["Nostalgie", "nostalgie"]

		if radio in nostalgieList:
			return True

		else:
			return False


jarvis = Jarvis()