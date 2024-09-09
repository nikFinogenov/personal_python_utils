from sympy import diff

print('Варіант 2')
print('Фіноегенов Н.М. ОПК-419')
print('Завдання:  x**3 + 6*x - 5 = 0')

def returnfunc(x):
     return x**3 + 6*x - 5

def reurndiff(differ, x):
    differ = str(differ)
    differ = differ.replace('x', str(x))
    result = eval(differ)
    return result
def toFixed(num, digits=0):
    return f'{num:.{digits}f}'

func = 'x**3 + 6*x -5'
differ = diff(func)
delta = 1
epsilon = 0.0001
x0 = 2
count = 0
print('---------------------')
print('Метод Ньютона')
print('---------------------')
while delta > epsilon:
    x = x0 - returnfunc(x0) / reurndiff(differ, x0)
    print(f'{count} | {toFixed(x, 10)} | {delta}')
    delta = abs(x - x0)
    x0 = x
    count += 1
    if count > 30:
        break
print(f'Відповідь: {x0}')

print('\n\n---------------------')
print('Метод Січних')
print('---------------------')

def f(x):
    return x ** 3 + 6 * x - 5
def secant(x0, x1, e, N):
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error')
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print(f'{step} | {x2} | {abs(f(x2))}')
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            break

        condition = abs(f(x2)) > e
    print(f'Відповідь: {x2}')


x0 = 0
x1 = 1
e = 0.0001
N = 3

x0 = float(x0)
x1 = float(x1)
e = float(e)

N = int(N)
secant(x0, x1, e, N)