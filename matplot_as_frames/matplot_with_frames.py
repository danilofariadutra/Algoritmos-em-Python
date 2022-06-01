import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_positions = list()
y_positions = list()
xy_positions = list()

x_data = list()
y_data = list()

pos = 0

def get_split_positions(path_file):
    with open(path_file) as file:
        with open(path_file) as file:
            for line in file:
                xy_positions.append(line.strip())         
    return xy_positions
    
def get_xy_positions(split_var, xy):
    trajectory = list()
    for line in split_var:
        float_trajectory = list()
        items = line.replace('[', '').replace(']', '').split(',')
        for pos in range(len(items)):
            float_trajectory.append(float(items[pos]))
        trajectory.append(float_trajectory)

    for pos in range(len(trajectory)):
        x_positions.append(trajectory[pos][1])
        y_positions.append(trajectory[pos][2])
        
    if xy == 'x':
        return x_positions
    elif xy == 'y':
        return y_positions
    elif xy == 'xy':
        return x_positions, y_positions
    else:
        return x_positions, y_positions
    


def matplot_as_frames(file, interval=1000, axis=True):
    split_xy = get_split_positions(file)
    x = get_xy_positions(split_xy, 'x')
    y = get_xy_positions(split_xy, 'y')
    
    fig, ax = plt.subplots()
    ax.set_xlim(0, 80)
    ax.set_ylim(0, 80)
    line, = ax.plot(50,0)

    def animation_frame(i):
        global pos
        x_data.append(x[pos])
        y_data.append(y[pos])    

        line.set_xdata(x_data)
        line.set_ydata(y_data)
        pos = pos + 1
        
        return line, 

    animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 1, 0.1), interval=interval)
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()

    if axis == True:
        ax = plt.gca()
        ax.spines['top'].set_color('none')
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        plt.grid(True)
    
    plt.show()

file = r'coordinates_example_1.txt'

matplot_as_frames(file, interval=100, axis=True)
