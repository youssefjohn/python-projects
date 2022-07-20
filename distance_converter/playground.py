def add(*args):
    x = 0
    for n in args:
        x += n

    return x

print(add(3, 4, 5))


def myfunc(**kwargs):
    print(kwargs)





myfunc(hi=2, bye=4)


print(round(43.2))

print("s,fs,f".split(","))
print(''.join("sd dd"))
print(list("sddds"))
