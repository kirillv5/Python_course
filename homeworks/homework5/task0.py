import sys
import re


data = sys.stdin.read()
result = re.findall("you", data)
print(len(result))
