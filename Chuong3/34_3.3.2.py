n=int(input('n='))
for i in range (0,10000):
    if n<10:
        print(n,'co 1 chu so')
    if 10<=n<=99:
        print(n,'co 2 chu so')
    if 100<=n<=999:
        print(n,'co 3 chu so')
    if n>=1000 and n<=9999:
        print(n,'co 4 chu so')
    break        