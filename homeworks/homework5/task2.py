import sys
import re


data = sys.stdin.read()
result = re.findall("([0-9]*(0{3}|1{3}|2{3}|3{3}|4{3}|5{3}|6{3}|7{3}|8{3}|9{3})[0-9]*)", data)
for i in result:
    print(i[0])