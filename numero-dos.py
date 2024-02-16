from math import sqrt

def gg_wp(x):
    return "GG WP"
def g(x):
    return sqrt((1 - x ** 3) / 3)

def g1(x):
    return abs(-sqrt(3) * x ** 2 / (2 * sqrt(1 - x ** 3)))

a = 0.5
b = 0.6

h = b - a
a -= h
b += h

q = g1(b)

x = [(a + b) / 2]

e = 0.0001

err = [b - a]
n = 1

while True:
    x.append(g(x[n - 1]))
    err.append(q * abs(x[n] - x[n - 1]) / (1 - q))

    print(f'{n:>}  {x[n]:>.4f}  {err[n]:>.4f}')

    if err[n] < e:
        break

    n += 1

t = (x[len(x) - 1]) / 2
print(f't = {t:.5f} +- {err[len(err) - 1]:.5f}')



