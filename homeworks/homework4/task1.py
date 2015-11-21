inf = open("yazkora.txt", "r")
text = inf.read()
inf.close()
sent = [i for i in text.replace("\n", " ").split(".")]
for i in range(len(sent)):
    sent[i] = sent[i].split()
i = 0
of = open("answer.txt", "w")
for i in range(len(sent)):
    for j in sent[i]:
        if "yo" in j[len(j) - 2:]:
            of.write(j + " ")
    of.write("\n")
    i+=1
of.close()