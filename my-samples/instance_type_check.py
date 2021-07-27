
x = 5
# x = '5'

if type(x) is int and (1 == 1 or 1 == 0):
    print('x is int')
if type(x) in (int, float):
    print('x is numeric')

if isinstance(x, (int, float)):
    print('x is numeric')