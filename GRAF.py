import matplotlib.pyplot as plt
import numpy as np
import logging

def DummyCos():
    x = np.linspace(0, 10, 100)
    y = 4 + 2 * np.sin(2 * x)
    return x,y

def DummyRand():
    #np.random.seed(1)
    x = np.linspace(0, 8, 16)
    y1 = 3 + 4*x/8 + np.random.uniform(0.0, 0.5, len(x))
    y2 = 1 + 2*x/8 + np.random.uniform(0.0, 0.5, len(x))
    return x,y1,y2

def DummyPolar():
    r = np.linspace(0, 3, 301)
    theta = 2 * np.pi * r
    return r, theta

def Standard(A):
    # plot
    X, Y  = A
    fig, ax = plt.subplots()
    ax.plot(X, Y, linewidth=2.0)
    plt.show()

def StdPlt(X,Y):
    # plot
    fig, ax = plt.subplots()
    ax.plot(X, Y, linewidth=2.0)
    plt.show()

def Zakres(A):
    x, y1, y2 =A
    fig, ax = plt.subplots()
    ax.fill_between(x, y1, y2, alpha=.5, linewidth=0)
    ax.plot(x, (y1 + y2) / 2, linewidth=2)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))
    plt.show()

def Polar(A):
    r, theta = A
    fig = plt.figure()
    ax = fig.add_subplot(projection="polar", facecolor="lightgoldenrodyellow", theta_offset=np.deg2rad(90))
    ax.plot(theta, r, color="tab:orange", lw=3, label="a line")
    ax.plot(0.5 * theta, r, color="tab:blue", ls="--", lw=3, label="another line")
    ax.tick_params(grid_color="palegoldenrod")
    angle = np.deg2rad(62.5)
    ax.legend(loc="lower left",
              bbox_to_anchor=(.5 + np.cos(angle) / 2, .5 + np.sin(angle) / 2))

    plt.show()

    pass

def BiPolar(fi, Y1, Y2):
    pass


'''
Zakres(DummyRand())
Polar(DummyPolar())
'''
def main():
    Standard(DummyCos())


if __name__ == '__main__':
    main()