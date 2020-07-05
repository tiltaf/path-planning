import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from Path_planning import Astar

class Formatter(object):
    def __init__(self,im):
        self.im = im
    def __call__(self,x,y):
        z = self.im.get_array()[int(x), int(y)]
        return 'x={:0.01f}, y={:0.01f}, z={:0.01f}'.format(x,y,z)
binary_map = 'binary_image.jpg'
original_map = 'original_image.PNG'
map1 = plt.imread(binary_map)
imag = plt.imread(original_map)

def display_path(path,length,width):

    def init():
        patch.center = (20, 20)
        ax.add_patch(patch)
        return patch,

    def animate(i):
        x, y = patch.center
        x = path[i][1]/10
        y = path[i][0]/10
        patch.center = (x, y)
        return patch

    print(len(path))
    fig = plt.figure()
    fig.set_dpi(100)
    fig.set_size_inches(7, 6.5)

    ax = plt.axes(xlim=(0, width), ylim=(length, 0))
    patch = plt.Circle((70, -70), 0.95, fc='b')

    path.reverse()
    global anim
    anim = animation.FuncAnimation(fig, animate,
                                   init_func=init,
                                   frames=len(path),
                                   interval=12,
                                   repeat=False)
    plt.imshow(imag,zorder=0,  extent=[0.1, width,  length, 0.1])
    plt.show()
    return

def getPoints():
    length,width,c = map1.shape
    length = length/10
    width = width/10
    reg_map = map1[:,:,0]
    reg_map = reg_map/255
    map_grid = np.array(reg_map).tolist()
    cost = 2

    coords =[]
    def onclick(event):
        ix, iy = event.xdata, event.ydata
        print ('x = %d, y = %d'%( ix, iy))
        coords.append([int(round(iy)), int(round(ix))])
        if len(coords) == 2:
            fig.canvas.mpl_disconnect(cid)
#            plt.close(1)
            astar = Astar(map_grid,coords)
            path = astar.path_find()
            display_path(path,length,width)
        return
    fig = plt.figure()
    plt.imshow(imag)

    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()
    return

if __name__ =="__main__":
    getPoints()
