import re


inf = open("hp5.txt", "r")
lines = inf.readlines()
inf.close()
whisp_lines = []
whisp_count = {}
for line in lines:
        whisp_lines += re.findall("whispered [A-Z][a-z]+ [A-Z][a-z]+|whispered [A-Z][a-z]+|[A-Z][a-z]+ [A-Z][a-z]+ whispered|[A-Z][a-z]+ whispered", line)
for i in range(len(whisp_lines)):
    whisp_lines[i] = whisp_lines[i].replace("whispered", "").replace(" ", "")
for person in whisp_lines:
    if person in whisp_count:
        whisp_count[person] += 1
    else:
        whisp_count[person] = 1

for key, value in whisp_count.items():
    if value == max(whisp_count.values()):
            print(value, key)
