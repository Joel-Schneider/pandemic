#!/usr/bin/python
# License: GPL3
# Copyright 2020 Joel Schneider
# Pandemic "simulator". DOES NOT predict real pandemics!

import datetime, random, sys, copy
global POPULATION, CITY_COUNT, RURAL_COUNT, age_risk #, total_infections, total_deaths
#TODAY = datetime.datetime(2020, 3, 20)
POPULATION = 66440 #000
CITY_COUNT = 4
RURAL_COUNT = 60

if len(sys.argv) < 3:
	print "Usage:", sys.argv[0], "options"
	print "Options:\tR (infectivity rate)"
	print "\t\truns (number of runs)"
	print "\t\tdays (number of days)"
	sys.exit()
else:
	R = float(sys.argv[1])
	runs = int(sys.argv[2])
	days = int(sys.argv[3])

age_risk = {}
for age in range(99):
	age_risk[age] = (1.0-(1.0/(age+1.0)))/(100-age)
#	print age, age_risk[age], " ",
#sys.exit()

class Person:
	def __init__(self):
		TODAY = datetime.datetime(2020, 3, 20)
		#print(TODAY)
		first_date = datetime.datetime(1922, 1, 1)
		#print(first_date)
		delta = TODAY - first_date
		#print(delta)
		self.DOB = TODAY - (int(10000*random.random()) * delta)/10000
		#print(self.DOB)
		self.alive = True
		self.infected = False
		self.symptomatic = False
		self.immune = False
	def try_infecting(risk, person):
		if self.infected == True:
			return
		if (random.random() < risk):
			self.infected = True
			self.days_infected = 0
	def get_age(self):
		now = datetime.datetime.now()
		#print(now, self.DOB)
		#sys.exit()
		return int((now-self.DOB).days /365.25)

	def next_day(self, infection_rate):
		if(self.immune == True):
			return "immune"
		elif(self.infected == True):
			self.days_infected += 1
			if(self.symptomatic == True):
				if(self.days_infected > 21):
					self.infected = False
					self.symptomatic = False
					self.immune = True
					return "cured"
				dead = random.random()/(22-self.days_infected) #*age_risk[self.get_age()]
				if(dead > age_risk[self.get_age()]):
					#print "Dead ", self.infected, self.symptomatic, self.days_infected, self.immune
					#print "Dead-", self.days_infected, "/7"
					return "death"
				#print("DOB", self.DOB, infect,"infect", age_risk[self.get_age()])
				#print(dead,"Dead")
			elif(random.random()>0.9):
				self.symptomatic = True
		else:
			infect = random.random() #*age_risk[self.get_age()]
			if(infect < (infection_rate/10)):
				self.infected = True
				self.days_infected = 1
				#print "Infected!"
				return "new infection"
			#
		#print "",
		return "not infected"
		
#print(age_risk)

def random_date(start, end):
	"""Generate a random datetime between `start` and `end`"""
	
	return start + datetime.timedelta(
		# Get a random amount of seconds between `start` and `end`
		seconds=random.randint(0, int((end - start).total_seconds())),
    )

class City:
	def __init__(self, population):
		self.population = population
		self.infection_count = 1
		self.infection_rate = 1.0/population
	def add_people(self, people):
		self.people = people
	def get_population(self):
		self.population = len(self.people)
		return self.population

def simulation (_cities, days, _R):
	#global TODAY, POPULATION, CITY_COUNT, RURAL_COUNT, age_risk, total_infections, total_deaths
	#print "Day", day, ": ", 
	_total_infections = 1
	_total_deaths = 0
	_total_population = 0
	for city in _cities:
		_total_population += city.get_population()
	#print _total_population
	TODAY = datetime.datetime(2020, 3, 20)
	day = 0
	#print _R, ",", day, ",", _total_infections, ",", _total_deaths, ",", _total_population

	for day in range(days):
		for city in _cities:
			for person in city.people:
				result = person.next_day(_R * city.infection_rate)
				if result == "new infection":
					city.infection_count += 1
					_total_infections += 1
				elif result == "death":
					city.people.remove(person)
					city.infection_count -= 1
					_total_infections -= 1
					_total_deaths += 1
					_total_population -= 1
			#print (city.infection_count) , (city.population)
			#sys.exit()
			city.infection_rate = float(city.infection_count) / float(city.population)
			#print city.infection_rate
			#sys.exit()
			#_total_population += city.get_population()
			#print city.infection_rate
			#print city.infection_rate
			#sys.exit()
			if city.get_population() < 1000:
				del(city)
				break
				#print "AA!", city.get_population(), _total_population
				#sys.exit()
		IR = 0.0
		for city in _cities:
			IR += city.infection_rate
		_average_infection_rate = IR/len(_cities)
		print _R, ",", day, ",", _total_infections, ",", _total_deaths, ",", _total_population, ",", _average_infection_rate, ",", len(cities)
		TODAY = TODAY + datetime.timedelta(days = 1)
	#sys.exit()

cities = []
#one_inf = False
for c in range(CITY_COUNT):
	one_inf = False
	#global TODAY, POPULATION, CITY_COUNT, RURAL_COUNT, age_risk, total_infections, total_deaths
	population = POPULATION/(CITY_COUNT+RURAL_COUNT)
	_city = City(population)
	# Create a city
	_pop = []
	for p in range(population):
		temp = Person()
		if one_inf == False:
			one_inf = True
			temp.infected = True
			temp.days_infected = 0
			_city.infection_count += 1
		_pop.append(temp)
	_city.add_people(_pop)
	cities.append(_city)
#print cities

print "R, Day, infections, deaths, population, sample infection rate, city count"
#__c = [cities, cities, cities, cities, cities, 

for run in range(runs):
	_c = copy.deepcopy(cities)
	simulation(_c, days, R)
	_c = []
	print

