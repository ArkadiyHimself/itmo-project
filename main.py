def summ(*args):
    a = sum(*args)
    return a

b = [int(x) for x in input().split()]


print(summ(b))