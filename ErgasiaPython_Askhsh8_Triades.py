#Το πρόγραμμα δημιουργήθηκε για την Python 3.6.4 και μπορεί να παρουσιάσει προβλήματα αν τρέξει σε παλαιότερες εκδόσεις

import random

def ThreeNum_ZeroSum(Blist, size, sum):
	
	Found = False
	for i in range (0, size-2):
	
		for j in range (i+1, size-1):
			
			for k in range (j+1, size):
			
				if Blist[i] + Blist[j] + Blist[k] == sum:
					print (Blist[i], ",", Blist[j], ",", Blist[k])
					Found = True

	if (Found == False):
		print ("De brethikan triades")
		return False
	
	
a = list(range(-30, 30))
Blist = []
for i in range(30):
	b = a[random.randint(0, len(a)-i)]
	Blist.append(b)
	a.remove(b)
	#print (b) Χρησιμοποιούνται για έλεγχο της λίστας
#print (Blist)	
sum = 0 #Μπορεί να αφαιρεθεί αν αλλάξουμε το sum μέσα στο def (line 14) σε μηδέν.
		#Σε αυτή τη μορφή όμως ο κώδικας θα μπορούσε να τροποποιηθεί ευκολότερα αν το sum χρησιμοποιούνταν σε πολλά σημεία του.
		
size = len(Blist)
#print (size) Έλεγχος μεγέθους λίστας
print ("Triades me athroisma mhden:\n")
ThreeNum_ZeroSum(Blist, size, sum)