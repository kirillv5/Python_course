n, k = (int(i) for i in input().split())
def combination(n, k):
    def factorial(x):
        c = 1
        lst = [i for i in range(1, x+1)]
        for i in lst:
            c *= i
        return(c)
    if k > n:
        return(0)
    elif n == k or k == 0:
        return(1)
    else:
        return(factorial(n) / (factorial(k) * factorial(n - k)))
print(int(combination(n, k))) 