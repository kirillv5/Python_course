lst_output = []


def rpfilter(a, *arg):
    def euclid(n, m):
        if n % m == 0:
            return(m)
        else:
            return(euclid(m, n % m))
    for i in arg:
        if euclid(a, i) == 1:
            lst_output.append(i)
lst_input = (int(i) for i in input().split())  
rpfilter(*lst_input)
if lst_output != []:
    for i in lst_output:
        print(i, end=' ')
else:
    print(None)
