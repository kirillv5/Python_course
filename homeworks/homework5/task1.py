import sys
import re


data = sys.stdin.read()
result = re.findall("[Yy]ou", data)
print(len(result))
