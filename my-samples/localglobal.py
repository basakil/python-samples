x = 100


def myfunc():
    x = 300

    def myinnerfunc():
        # nonlocal x
        global x
        x = 400
        print(f'{x}\t myinnerfunc')

    myinnerfunc()
    print(f'{x}\t myfunc')


myfunc()
print(f'{x}\t module')
