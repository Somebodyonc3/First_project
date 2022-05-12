import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# Определяем переменную величину
frames = 30
seconds_in_year = 30 * 24 * 60 * 60
years = 1.5
t = np.linspace(0, years*seconds_in_year, frames)

# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2) = s

    dxdt1 = v_x1
    dv_xdt1 = - G * m * x1 / (x1**2 + y1**2)**1.5
    dydt1 = v_y1
    dv_ydt1 = - G * m * y1 / (x1**2 + y1**2)**1.5

    dxdt2 = v_x2
    dv_xdt2 = - G * m * x2 / (x2**2 + y2**2)**1.5
    dydt2 = v_y2
    dv_ydt2 = - G * m * y2 / (x2**2 + y2**2)**1.5

    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2)
    
# Определяем начальные значения и параметры
    
G = 6.67 * 10**(-11)
m = 1.98 * 10**(30)

x10 = -0.387 * 149 * 10**9
v_x10 = 0
y10 = 0
v_y10 = 41000

x20 = 0
v_x20 = -32020
y20 = 0.723332 * 149 * 10**9
v_y20 = 0

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20)

sol = odeint(move_func, s0, t)
#Цикл над sol 
# Решаем систему диф. уравнений
def solve_func(i, key):
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]
        x2 = sol[i, 4]
        y2 = sol[i, 6]

    else:
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]
        x2 = sol[:i, 4]
        y2 = sol[:i, 6]

    return ((x1, y1), (x2, y2))

# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='r', ms=15)

def get_arrow(theta):
    x = 0
    y = 10e4
    u = np.sin(theta)
    v = np.cos(theta)
    return x, y, u, v

quiver = ax.quiver(*get_arrow(100), scale=4, width=0.001)

def update(theta):
    global quiver
    quiver.remove()
    quiver = ax.quiver(*get_arrow(theta), scale=4, width=0.001)

plt.plot([0], [0], 'o', color='orange', ms=40)

def animate(i):
    ball1.set_data(solve_func(i, 'point')[0])


ani = FuncAnimation(fig,
                    animate,
                    frames=30,
                    interval=30)

ani1 = FuncAnimation(fig,
                    update,
                    frames=30,
                    interval=30)

plt.axis('equal')
edge = 10e10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
plt.show()