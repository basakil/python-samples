def fib():
     first = 0
     last = 1
     while True:
         first, last = last, first + last
         yield first

for x in fib():
    print(x)
    if x > 12:
        break
