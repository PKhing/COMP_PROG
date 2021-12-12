import matplotlib.pyplot as plt
from matplotlib import animation, rc
import random
import math

def main():
    import sys
    # check if this code is running in colab
    in_colab = 'google.colab' in sys.modules
    
    random.seed(1111)
    W, H = 120, 100
    # 200 birds on a WxH window
    x,y,dx,dy = gen_data(200, W, H)

    fig = plt.figure(figsize=(4*W/H, 4))
    anim = animation.FuncAnimation(fig, animate, 
                    fargs=(x, y, dx, dy, W, H),
                    frames=(60 if in_colab else None), 
                    repeat=False, interval=50)
    if in_colab:
        rc('animation', html='jshtml')
        return anim
    else:
        plt.show()

def animate(n, x, y, dx, dy, W, H):   
    NOISE = 0.3        # +/- direction noise radians
    R = 0.10*min(W, H) # neighbors within R
    V = 0.02*min(W, H) # velocity -> displacement in each time step  
    move_all(x, y, dx, dy, V, W, H)
    ax = [0.0]*len(x)
    ay = [0.0]*len(x)
    for k in range(len(x)):
        ax[k],ay[k] = neighbor_average_direction(x, y, dx, dy, k, R)
        t = math.atan2(ay[k],ax[k]) + (NOISE - 2*NOISE*random.random())
        ax[k] = math.cos(t)
        ay[k] = math.sin(t)
    dx[:] = ax   # update the orginal dir vector
    dy[:] = ay
    plt.clf()    # clear figure
    plt.quiver(x, y, dx, dy) # plot a 2D field of arrows
    plt.xlim((0, W))
    plt.ylim((0, H))

#-------------------------------------------
# HW5: Vicsek Model
# ID: Name

def gen_data(N, W, H):
  x = [random.random()*W for i in range(N)]
  y = [random.random()*H for i in range(N)]
  dx = []
  dy = []
  for i in range(N):
    rad = 2*math.pi*random.random()
    dx.append(math.cos(rad))
    dy.append(math.sin(rad))
  return x,y,dx,dy



#-------------------------------------------
def move_all(x, y, dx, dy, d, W, H):
  for i in range(len(x)):
    x[i]+=d*dx[i]
    y[i]+=d*dy[i]
    while x[i]>=W:
      x[i]-=W
    while x[i]<0:
      x[i]+=W
    while y[i]>=H:
      y[i]-=H
    while y[i]<0:
      y[i]+=H
x = [0.0, 11.0, 14.75, 5.0]; y = [9.0, 9.5, 5.0, 5]
dx = [-1.0, 0.0, 1.0, 0.0]; dy = [0.0, 1.0, 0.0, 1.]
move_all(x, y, dx, dy, 0.5, 15, 10)
print(x, y)
print(dx, dy)
#-------------------------------------------
def neighbor_average_direction(x, y, dx, dy, k, R):
  sumdx = 0
  sumdy = 0
  for i in range(len(x)):
    if (x[i]-x[k])**2+(y[i]-y[k])**2 <= R**2:
      sumdx+=dx[i]
      sumdy+=dy[i]
  length = math.sqrt(sumdx**2+sumdy**2)
  return sumdx/length, sumdy/length

#-------------------------------------------
main()

