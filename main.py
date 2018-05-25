import csv
from twilio.rest import Client
import json
import sys

# verification
f = open("secret.json", 'r')
secret = json.load(f)

auth_token = secret['auth_token']
account_sid = secret['account_sid']

f.close()
client = Client(account_sid, auth_token)

names = []
numbers = []

f = open(sys.argv[1])

reader = csv.reader(f)

for row in reader:
    names.append(row[0])
    numbers.append(row[1])



for name, number in zip(names, numbers):
    print("Assalamualaikum {},\nplease donate to ACC {}".format(name, number))

    client.messages.create(
        to=number,
	    from_="+1 (469) 754-9682",
	    body="Assalamualaikum {},\nplease donate to ACC".format(name)
	    )