import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('default')
frames = 30
seconds_in_year = 30 * 24 * 60 * 60
years = 1.5
t = np.arange(0, years*seconds_in_year, frames)

edge = 10e10
figure = plt.figure()
axis = plt.axes(xlim=(-edge, edge), ylim=(-edge, edge))
line, = axis.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

def animate(t):
    x = np.cos(t)
    y = np.sin(t)
    line.set_data(x, y)
    return line,

anim = FuncAnimation(figure, animate, init_func=init,
                               frames=520, interval=20)

anim.save('test 1.gif')