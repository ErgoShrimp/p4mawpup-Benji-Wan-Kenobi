import urllib2
import time
from twilio.rest import Client

account_sid = 'ACa7889d2092ab17c8907d142adf8a915b'
auth_token = 'b9ea03d04522dc1051bc991bf757494b'
twilio_phone_number = '+14042387455'
my_phone_number = "+16787932030"

def WebData():
	
	link = raw_input ("Paste URL here:")
	sec = int(raw_input("How many seconds do you want to test for?"))
	
	URL = urllib2.urlopen(link)
	data = URL.read()
	datastring = str(data)
	lengthB = len(datastring)
	
	timeT = 0
	
	while timeT < sec:
	
		URL = urllib2.urlopen(link)
		data = URL.read()
		datastring = str(data)
		lengthA = len(datastring)
		
		print("Testing...")
		if lengthB != lengthA:
			body = "The site has changed!"
			client = Client(account_sid, auth_token)
			client.messages.create(
				body=body,
				to=my_phone_number,
				from_=twilio_phone_number
			)
			print("Change detected, text sent")
			break
		else:
			lengthA = lengthB
			timeT += 1
			time.sleep(1)
			
		if timeT == sec:
			print ("No changes were made.")
	
WebData()
