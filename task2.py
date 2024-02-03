import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt


def f(x):
    return x ** 2


a = 0
b = 2
n = 10000

x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, f(b), n)
under_curve = y_random < f(x_random)
area = (b - a) * f(b)
integral_monte_carlo = area * np.sum(under_curve) / n
print("Інтеграл (Монте-Карло):", integral_monte_carlo)

result, error = spi.quad(f, a, b)
print("Інтеграл (quad):", result)

x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


