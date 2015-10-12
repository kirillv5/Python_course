n, k = (int(i) for i in input().split())


def combination(n, k):
    if k > n:
        return 0
    elif n == k or k == 0:
        return 1
    else:
        return combination(n - 1, k - 1) + combination(n - 1, k)
print(combination(n, k))
