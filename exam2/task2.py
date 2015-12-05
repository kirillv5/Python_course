import re
import requests


inf = open("links.txt", "r")
links = inf.readlines()
inf.close()
emails = []
for link in links:
    r = requests.get(link).text
    emails += re.findall("[0-9\w._]+@[0-9\w._]+", r)

out = set(emails)
of = open("email_addresses.txt", "w")
for mail in out:
    of.write(mail + "\n")