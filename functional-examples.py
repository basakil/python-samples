#!/usr/bin/env python

from functools import reduce
import math
# from math import *
# from math import gcd

from decimal import Decimal

months = [('Jan', 31), ('Feb', 28), ('Mar', 31)]

print(reduce(lambda x, y: (" ", x[1] + y[1]), months)[1])
print(reduce(lambda x, y: x if x[1] < y[1] else y, months))

print(list(map(lambda x: str(x[0])+":"+str(x[1]), months)))

print(3.5 - 3.2)

## from decimal import Decimal
print(Decimal('3.5') - Decimal('3.2'))

from collections import deque
deque([3, 5, 8])

## deque(list) has append, appendleft, pop, popleft

list = [6, 3, 8, 0, 56, 11, 5]
for index, item in enumerate(list):
    print(f'{index} => {item}')
