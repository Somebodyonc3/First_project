import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# Определяем переменную величину
frames = 100
seconds_in_cycle = 60
cycles = 50
t = np.linspace(0, cycles * seconds_in_cycle, frames)

# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    (x, v_x, y, v_y) = s

    dxdt = v_x
    dv_xdt = - G * earthM * x / (x**2 + y**2)**1.5
    dydt = v_y
    dv_ydt = - G * earthM * y / (x**2 + y**2)**1.5

    return (dxdt, dv_xdt, dydt, dv_ydt)
    
# Определяем начальные значения и параметры
satH = 408 * 10**3 # 408 км высотп МКС
satV = 7.66 * 10**3 # скорость МКС
satM = 420 * 10**3 # масса МКС

earthR = 6371 * 10**3
earthM = 5.9742 * 10**24

G = 6.67 * 10**(-11)

x0 = (earthR + satH)
v_x0 = 0
y0 = 0.0
v_y0 = satV

s0 = (x0, v_x0, y0, v_y0)

sol = odeint(move_func, s0, t)

post_sol = [[],[],[],[]]

for i in range(frames):
	x = sol[i, 0]
	y = sol[i, 2]
	h = y - earthR
	d = np.sqrt( x**2 + h**2 )

	if h > 0:
		a = np.arccos(x / d)
		u = np.cos(a)
		v = np.sin(a)
		adeg = np.degrees(a)
		post_sol[0].append(adeg if (adeg < 90) else (180 - adeg))
		post_sol[1].append(u)
		post_sol[2].append(v)
	else:
		post_sol[0].append(0)
		post_sol[1].append(0)
		post_sol[2].append(0)
	post_sol[3].append(h)
		

# Решаем систему диф. уравнений
def solve_func(i, key):
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]

    else:
        x = sol[:i, 0]
        y = sol[:i, 2]

    return (x, y)

# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()
ball1, = plt.plot([], [], 'o', color='r', ms=5)
horizont, = plt.plot([-10**8, 10**8], [earthR, earthR], '--', color='g')
quiver = ax.quiver(0, earthR, 0, 0, scale=4, width=0.01)
circle = plt.Circle((0.0, 0.0), earthR, color="#8080ff")
ax.add_patch(circle)

def update_quiver(i):
	u, v, h = post_sol[1][i], post_sol[2][i], post_sol[3][i]

	quiver.set_UVC(u, v)

	return quiver,

def animate(i):
	ball1.set_data(solve_func(i, 'point'))
	update_quiver(i)


ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
					interval=30)

plt.axis('equal')
edge = (earthR + satH) * 1.1
ax.set_xlim(-edge, edge)
ax.set_ylim(earthR , edge + earthR)
#ani.save("arrow.gif", dpi=200)
plt.show()

ax.set_xlim(1000, 2000)
atg, = plt.plot(t, post_sol[0], '-', color='orange')
plt.savefig("fig.png", dpi=200)
ani.save('1.gif')
plt.show()