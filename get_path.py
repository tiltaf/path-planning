import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
from scipy.misc import imread
import numpy as np
from Path_planning import Astar

class Formatter(object):
    def __init__(self,im):
        self.im = im
    def __call__(self,x,y):
        z = self.im.get_array()[int(x), int(y)]
        return 'x={:0.01f}, y={:0.01f}, z={:0.01f}'.format(x,y,z)

filename = 'gulzarnlabbinaryimg.jpg'
imag = plt.imread(filename)
imag1 = plt.imread('gulzarwlab.png')


def display_path(path,length,width):

    def init():
        patch.center = (20, 20)
        ax.add_patch(patch)
        return patch,

    def animate(i):
        x, y = patch.center
    #    x = 50 + 3 * np.sin(np.radians(i))
    #    y = 50 + 3 * np.cos(np.radians(i))
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
                                   repeat = False,
                                   blit=True)

    plt.imshow(imag1,zorder=0,  extent=[0.1, width,  length, 0.1])
    #anim.save('the_movie.mp4', writer = 'ffmpeg', fps=30)
    plt.show()
    return





def getPoints():
    length,width,c = imag.shape
    length = length/10
    width = width/10
    im1 = imag[:,:,0]
    im1 = im1/255
    map_grid  = np.array(im1).tolist()
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
    plt.imshow(imag1)

    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

if __name__ =="__main__":
    getPoints()
