'''
Гармоничные колебания маятника
'''
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

edge = 60
g = 9.8

l = int(input('Введите значение для длины нити маятника:'))
m = int(input('Введите значение для массы тела:'))

def sh(r, t):
	theta, omega = r
	sh_theta = omega
	sh_omega = -g / l * sin(theta)
	return np.array([sh_theta,sh_omega], float)

init_state = np.radians([89.0,0])
dt = 0.1
time = np.arange(0, 1000, dt)

state = integrate.odeint(sh, init_state, time)


fig = plt.figure(figsize = (8,6))
ax = plt.axes(xlim = (-2 * l, 2 * l), ylim = (-2 * l, l))
line, = ax.plot([],[],'-o', lw = 2, ms = 10, color = 'g')

def init():
	return line,

def animate(i):

	phi = state[i, 0]

	line.set_data([0,l * sin(phi)], [0, -l * cos(phi)])
	return line,


plt.axis('equal')
plt.title('Колебания маятника')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

anim = animation.FuncAnimation(fig,animate,
								init_func = init,
								frames = len(time),
								interval = 40,
								blit = True)

plt.show()