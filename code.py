'''
Гармоничные колебания маятника
'''
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

g = 9.8

l = int(input('Введите значение для длины нити маятника:'))
m = int(input('Введите значение для массы тела:'))

def sh(r):								#уравнение маятника
	theta, omega = r
	sh_theta = omega
	sh_omega = -g / l * sin(theta)
	return np.array([sh_theta,sh_omega], float)

init_state = np.radians([89.0,0])
time = np.arange(0, 1000, 0.1)			#кол-во точек

state = integrate.odeint(sh, init_state, time)

fig = plt.figure(figsize = (8,6))
ax = plt.axes(xlim = (-2 * l, 2 * l), ylim = (-2 * l, l))
line, = ax.plot([],[],'-o', lw = 2, ms = 10, color = 'b')

def init():
	return line,

def animate(i):							#счетчик точек

	phi = state[i, 0]

	line.set_data([0,l * sin(phi)], [0, -l * cos(phi)])
	return line,

edge = l * 1.5
plt.axis('equal')
plt.title('Колебания маятника')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

anim = animation.FuncAnimation(fig,animate,
								init_func = init,
								frames = len(time),
								interval = 40,
								blit = True)
anim.save('kolebania.mp4')
plt.show()
