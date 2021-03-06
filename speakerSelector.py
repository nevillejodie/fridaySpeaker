from datetime import date, timedelta
import random

theTeam = ["Steve", "John", "Jodie"]

def getTeamMember():
 teamMember = random.choice(theTeam)
 print(teamMember)


def allFridays(year):
   d = date(year, 10, 2)                    # Todays date
   d += timedelta(days = 4 - d.weekday())  # First Friday
   while d.year == year:
      yield d
      d += timedelta(days = 7)

for d in allFridays(2020):
 print (str(d), getTeamMember())


