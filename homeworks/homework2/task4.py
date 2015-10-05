def rpfilter(a, *arg):
    lst_output = []
    def euclid(n, m):
        if n % m == 0:
            return m
        else:
            return euclid(m, n % m)
    for i in arg:
        if euclid(a, i) == 1:
            lst_output.append(i)
    return lst_output
lst_input = (int(i) for i in input().split())  
lst_output = rpfilter(*lst_input)
if lst_output != []:
    for i in lst_output:
        print(i, end=' ')
else:
    print(None)
