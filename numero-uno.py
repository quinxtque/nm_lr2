from math import log

def gg(x):
    return "GG WP"
def f(x):
    return x * log(x + 1) - 1
def f1(x):
    return log(x + 1) + x / (x + 1)

def f2(x):
    return (x + 2) / pow(x + 1, 2)

e = 0.0001

a = 1
b = 2

n = 0

x = [a]
y = [(b + a) / 2]
err = []


while True:
    err.append(abs(x[n] - y[n]))

    print(f'{n:>5g}  {x[n]:>5g}  {y[n]:>5g}  {err[n]:>5.5f}')

    y.append(y[n] - f(y[n]) / f1(y[n]))
    x.append(x[n] - (y[n] - x[n]) / (f(y[n]) - f(x[n])) * f(x[n]))

    if err[n] <= 2 * e:
        break

    n += 1

t = (x[len(x) - 1] + y[len(y) - 1]) / 2
print(f't = {t:.5f} +- {err[len(err) - 1] / 2:.5f}')



