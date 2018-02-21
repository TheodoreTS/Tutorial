#Το πρόγραμμα δημιουργήθηκε για την Python 3.6.4 και μπορεί να παρουσιάσει προβλήματα αν τρέξει σε παλαιότερες εκδόσεις


Roman = [
	(1000000, u'M\u0305'),
	(900000, u'C\u0305M\u0305'),
	(500000, u'D\u0305'),
	(400000, u'C\u0305D\u0305'),
	(100000, u'C\u0305'),
	(90000, u'X\u0305C\u0305'),
	(50000, u'L\u0305'),
	(40000, u'X\u0305L\u0305'),	
	(10000, u'X\u0305'),
	(9000, u'I\u0305X\u0305'),
	(5000, u'V\u0305'),
	(4000, u'I\u0305V\u0305'),
	(1000, "M"),
	( 900, "CM"),
	( 500, "D"),
	( 400, "CD"),
	( 100, "C"),
	(  90, "XC"),
	(  50, "L"),
	(  40, "XL"),
	(  10, "X"),
	(   9, "IX"),
	(   5, "V"),
	(   4, "IV"),
	(   1, "I"),
]

def convert_to_roman(number):
	numeral = []
	for (arabic, roman) in Roman:
		(factor, number) = divmod(number, arabic)
		numeral.append(roman * factor)
		if number == 0:
			break
	
	return "".join(numeral)
	
input_is_int = False
while not input_is_int:
	try:
		number = int(input('Dose thetiko akeraio arithmo gia metatropi: '))
		if number > 0:
			input_is_int = True
			print (convert_to_roman(number))
		else:
			print("O arithmos den einai megaluteros tou 0. Prospathise pali: ")
	except ValueError:
		print("Den edoses thetiko akeraio. Prospathise pali: ")
