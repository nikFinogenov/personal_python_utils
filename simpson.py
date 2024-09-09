from __future__ import division
import sympy
import math

x = sympy.Symbol('x')

f_x = (1 / (1 + x))
eps = 0.0001
a = 0
b = 1.2
nNotEven = (b - a) / sympy.sqrt(sympy.sqrt(eps))
n = math.ceil(nNotEven / 2) * 2
def formatNumber(num):
  if num % 1 == 0:
    return int(num)
  else:
    return num
def f(x):
    return sympy.log(1 + pow(x, 2))

def simpson(a, b, n, f):
  sum = 0
  inc = (b - a) / n
  for k in range(n + 1):
    x = a + (k * inc)
    summand = f(x)
    if (k != 0) and (k != n):
      summand *= (2 + (2 * (k % 2)))
    sum += summand
    print(f'{k} | {x} | {summand} | {sum} ')
  return ((b - a) / (3 * n)) * sum

# print(simpson(0, 1, 6, lambda x: 1 / math.sqrt(1 + x * x)))
result = simpson(a, b, n, f)

print("Результат: ", result)