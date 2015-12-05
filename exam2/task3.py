import re
import requests
from bs4 import BeautifulSoup

link = "https://twitter.com/googlefacts"
r = requests.get(link)
soup = BeautifulSoup(r.content, "html.parser")
txt1 = soup.find_all("p")
twits = re.findall("(?<=lang=\"en\">).*?(?=</p>)", a)

out = open("twitter.txt", "w")
for i in twits:
    out.write(i + "\n")
out.close()