#Το πρόγραμμα δημιουργήθηκε για την Python 3.6.4 και μπορεί να παρουσιάσει προβλήματα αν τρέξει σε παλαιότερες εκδόσεις

import datetime
from itertools import takewhile



Years = 10
Start = datetime.date.today()
DayOfWeek = datetime.date.today().isoweekday() #Monday=1, Tuesday=2.....Sunday=7
DayOfMonth = datetime.date.today().day


def years_from(date, years):
	return datetime.date(date.year + years, 12, 31)
	
Max_Date = years_from(Start, Years)
	
	
def intersection(weekday, day, start_date = None):
	if start_date == None:
		date = Start
	else:
		date = start_date
	while True:
		if date.day == day and date.isoweekday() == weekday:
			yield date
		date += datetime.timedelta(days=1)
		
def current_date_ocurrences():
	return intersection(DayOfWeek, DayOfMonth)
	
def enforce_max_date(max_date = Max_Date):
	def date_check(date):
		return date <= max_date
	return takewhile(date_check, current_date_ocurrences())

Occurences = list(enforce_max_date())
OccurNo = len(Occurences)
	
print("Oi parakato hmeromhnies einai oi epanalhpseis ths shmerinhs ta epomena 10 xronia:\n")

for i in Occurences:
	print(i)

print("\nArithmos epanalhpsewn: ", OccurNo)
	
	
