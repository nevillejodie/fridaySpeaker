""" 1. take in the names of staff members
2. take in Friday dates 
3. Arrange speaker name across the dates evenly
4. returns the name of the speaker who's turn it is that week  """
from datetime import date, timedelta
import random

theTeam = ["Steve", "John", "Ken", "Jodie"]
teamMember = random.choice(theTeam)
print(teamMember)


 def allFridays(year):
   d = date(year, 9, 21)                    # January 1st
   d += timedelta(days = 4 - d.weekday())  # First Friday
   while d.year == year:
      yield d
      d += timedelta(days = 7)

for d in allFridays(2020):
 print (d) 


