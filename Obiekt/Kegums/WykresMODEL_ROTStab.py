import matplotlib.pyplot as plt
import numpy as np

def Zakres(Arr, Min, Max):
    Imin = 0
    Imax = 0
    for i in range(len(Arr)):
        if Arr[i] <= Min:
            Imin = i+1
        if Arr[i] <= Max:
            Imax = i
    return (Imin,Imax)

def Wiekszy(Arr, Max):
    Imax = 0
    for i in range(len(Arr)):
        if Arr[i] <= Max:
            Imax = i
    return (Imax+1)

def Widelki(Arr, Min, Max):
    Ok = 0
    for i in range(len(Arr)):
        if Arr[i] <= Min:
            Ok = i
        if Arr[i] >= Max:
            Ok = i
    return Ok

# make data
import AdapterIO
Dane = AdapterIO.IEN_v1('Model.rec')
N = 4
A = 0
F = 2
P = 5
K = 6
t0 = 400
t1 = -5
t2 = 220
dt = 10

dis_nmin = 95
dis_dn = 1
dis_nmax = 105
dis_nred = 130

ymin = 14
dy2 = 2
ymax = 26

dis_pmin = 0
dis_dp = 1
dis_pmax = 19


Tytul = ''


X = Dane['X']
Y = Dane['Y']


for i in range(len(X)):
    for j in range(len(X[i])):
        X[i][j]= X[i][j] -t0

I1,I2 = Zakres(X[N],t1,t2)


# plot
fig, axs = plt.subplots(2, 1, sharex=True)
fig.subplots_adjust(hspace=0.02, left=0.06, bottom=0.06, right=0.94, top=0.94)

# Plot each graph, and manually set the y tick values
axs[0].plot(X[N], Y[N], label='Speed [%]')
#axs[0].plot(X[10], Y[10], label='Setpoint [%]', color='black')
axs[0].grid(True, linestyle='-.')
axs[0].set_title(Tytul, pad=10, fontsize = 10)
axs[0].set_xlim(t1,t2)
axs[0].set_ylim(dis_nmin, dis_nmax)
axs[0].set_xticks(np.arange(t1,t2,dt))
axs[0].set_yticks(np.arange(dis_nmin, dis_nmax, dis_dn))
axs[0].tick_params(labelcolor='blue')
axs[0].legend(shadow = True, fontsize=11)


axs[1].plot(X[A], Y[A], label='Wicket gate [%]', color='red')
axs[1].grid(True, linestyle='-.')
axs[1].set_ylim(ymin,ymax)
axs[1].set_yticks(np.arange(ymin,ymax,dy2))
axs[1].tick_params(labelcolor='black')
axs[1].set_xlabel('Time [s]', fontsize=10)
axs[1].legend(shadow = True, fontsize=11)

plt.show()