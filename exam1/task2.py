import math 

inf = open("dict.txt", "r")
dct = inf.read().replace("\n", " ").split(" ")
inf.close()
noun = 0
adj = 0
verb = 0
for word in dct:
    if word.endswith("ka"):
        noun += 1
    elif word.endswith("yo"):
        adj += 1
    else:
        verb += 1

adj_comb = 0
for k in range(1, 8):
    adj_comb += math.factorial(adj) / (math.factorial(adj - k) * math.factorial(k))
    
cool_sent = int(adj_comb * noun * verb)

print(cool_sent)