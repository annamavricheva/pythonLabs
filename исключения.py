def careless_div(a, b):
    return a/b


try:
    while True:
        a, b = input().split()
        a = int(a)
        b = int(b)

        try:
            print(careless_div(a, b))
        except ZeroDivisionError:
            if a>0:
                print(float('+inf'))
            if a<0:
                print(float('-inf'))
            if a==0 and b==0:
                print('-17.5')
except KeyboardInterrupt:
    print('Bye!')
