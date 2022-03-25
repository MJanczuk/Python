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
Dane = AdapterIO.IEN_v1('RB.rec')
N = 2
A = 2
F = 1
P = 0
K = 3
t0 = 1809.481+920.63-0.417+50-0.124
t1 = -2
t2 = 36
dt = 2

dis_nmin = 0
dis_dn = 10
dis_nmax = 101
dis_nred = 130

dis_ymin = 0
dis_dy = 10
dis_ymax = 101

dis_pmin = 45
dis_dp = 1
dis_pmax = 65

dis_op = 2

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
axs[0].plot(X[A], Y[A], label='Runner blades servomotor [%]', color='green')
axs[0].grid(True, linestyle='-.')
axs[0].set_title(Tytul, pad=10, fontsize = 10)
axs[0].set_ylim(dis_nmin-dis_op, dis_nmax+dis_op)
axs[0].set_xlim(t1,t2)
axs[0].set_xticks(np.arange(t1,t2,dt))
axs[0].set_yticks(np.arange(dis_nmin, dis_nmax, dis_dn))
axs[0].tick_params(labelcolor='green')
axs[0].legend(shadow = True, fontsize=11)

axs[1].plot(X[F], Y[F], label='Runner blades distributor [%]', color='black')
axs[1].grid(True, linestyle='-.')
axs[1].set_ylim(dis_ymin-dis_op, dis_ymax+dis_op)
axs[1].set_yticks(np.arange(dis_ymin, dis_ymax, dis_dy))
axs[1].tick_params(labelcolor='black')
axs[1].legend(shadow = True, fontsize=11)
'''
axs[2].plot(X[P], Y[P], label='Wicket gate actuator [%]', color='violet')
axs[2].grid(True, linestyle='-.')
axs[2].set_ylim(dis_pmin-dis_op,dis_pmax+dis_op)
axs[2].set_yticks(np.arange(dis_pmin,dis_pmax,dis_dp))
axs[2].tick_params(labelcolor='violet')
axs[2].set_xlabel('Time [s]', fontsize=10)
axs[2].legend(shadow = True, fontsize=11)
'''
plt.show()