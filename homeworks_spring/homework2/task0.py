out = []
if issubclass(D, A) is True:
    out.append('A')
if issubclass(D, B) is True:
    out.append('B')
if issubclass(D, C) is True:
    out.append('C')
        
out.sort()
print(" ".join(out))