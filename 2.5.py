def NOD(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n

a = int(input())
b = int(input())

print(NOD(a, b))
