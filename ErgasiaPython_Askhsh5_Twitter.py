#Το πρόγραμμα δημιουργήθηκε για την Python 3.6.4 και μπορεί να παρουσιάσει προβλήματα αν τρέξει σε παλαιότερες εκδόσεις
#Χρησιμοποιήθηκε η βιβλιοθήκη python twitter (pip install python-twitter)

import twitter
import json
import re
import string
import io

api = twitter.Api(consumer_key='ijOlrKeQM01CAInRVd1h5IYOT',
  consumer_secret='dFKTla9ixXjZMNl0AVn9zcHRP7w97sJXqUHRBrvPuFn3qxLhII',
  access_token_key='965315716982468610-hggFgDM1HszrLWYAb6JrTiIrPwNUJIy',
  access_token_secret='pOadHDZd7TNMtzgZXJOQCLNVPJ4BaVJxsWGzakzwliZAs')

InputTwitter = input('Dose onoma xrhsth sto twitter: ')
  
t = api.GetUserTimeline(screen_name=InputTwitter, count=10)

tweets = [i.AsDict() for i in t]

	
with io.open('tweets.json', 'w', encoding='utf8') as  outfile:
	for t in tweets:
		json.dump(t['text'], outfile, ensure_ascii=False)	

frequency = {}
document_text = io.open('tweets.json', 'r', encoding='utf8')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-ω]{4,25}\b', text_string)#Λέξεις με ελληνικούς ή λατινικους χαρακτήρες, από 4-25 γράμματα

 
#Οι εντολές μετά από αυτό το σχόλιο θα μπορούσαν επίσης να αντικατασταθούν με τις εξής:
#Max = Counter(match_pattern).most_common(1)
#print ("Emfanizetai pio syxna h leksh:\n")
#print (Max)
#(χρησιμοποιώντας την from collections import Counter) με το ίδιο αποτέλεσμα.

 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()

MaxFrequency = 0
MaxWord=''

for words in frequency_list:
	if frequency[words] > MaxFrequency:
		MaxFrequency=frequency[words]
		MaxWord=words   

print ("Emfanizetai pio syxna h leksh:\n")		
print (MaxWord, ",", MaxFrequency,"fores")
#print (match_pattern) Ελέγχει ότι βρέθηκαν όλες οι λέξεις
