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
Dane = AdapterIO.IEN_v1('TSO_FSM2LFSM.rec')
N = 2
A = 0
F = 1
P = 4
K = 3
t0 = 6200
t1 = 0
t2 = 1000
dt = 100

dis_nmin = 50
dis_dn = 10
dis_nmax = 100
dis_nred = 130

ymin = 0
dy2 = 10
ymax = 100

dis_pmin = 6
dis_dp = 1
dis_pmax = 18


Tytul = ''


X = Dane['X']
Y = Dane['Y']


for i in range(len(X)):
    for j in range(len(X[i])):
        X[i][j]= X[i][j] -t0

I1,I2 = Zakres(X[N],t1,t2)


Nmax = max(Y[N][I1:I2])
imax = Y[N][I1:I2].index(Nmax)
tmax = X[N][imax+I1]

Nmin = min(Y[N][I1:I2])
imin = Y[N][I1:I2].index(Nmin)
tmin = X[N][imin+I1]

tol = Widelki(Y[N][I1:I2],99.0,101.0)
tolx = X[N][tol+I1]
toly = Y[N][tol+I1]

# plot
fig, axs = plt.subplots(3, 1, sharex=True)
fig.subplots_adjust(hspace=0.02, left=0.06, bottom=0.06, right=0.94, top=0.94)

# Plot each graph, and manually set the y tick values
axs[0].plot(X[A], Y[A], label='Wicket gate [%]', color='red')
axs[0].grid(True, linestyle='-.')
axs[0].set_title(Tytul, pad=10, fontsize = 10)
axs[0].set_xlim(t1,t2)
axs[0].set_ylim(dis_nmin, dis_nmax)
axs[0].set_xticks(np.arange(t1,t2,dt))
axs[0].set_yticks(np.arange(dis_nmin, dis_nmax, dis_dn))
axs[0].tick_params(labelcolor='red')
axs[0].legend(shadow = True, fontsize=11)



axs[1].plot(X[F], Y[F], label='Runner blades [%]', color='green')
axs[1].grid(True, linestyle='-.')
axs[1].set_ylim(ymin,ymax)
axs[1].set_yticks(np.arange(ymin,ymax,dy2))
axs[1].tick_params(labelcolor='green')
axs[1].legend(shadow = True, fontsize=11)


axs[2].plot(X[P], Y[P], label='Active power [MW]', color='orange')
axs[2].plot(X[7], Y[7], label='Setpoint [MW]', color='black')
axs[2].set_xlabel('Time [s]', fontsize=10)
axs[2].grid(True, linestyle='-.')
axs[2].set_ylim(dis_pmin, dis_pmax)
axs[2].set_yticks(np.arange(dis_pmin, dis_pmax, dis_dp))
axs[2].tick_params(labelcolor='orange')
axs[2].legend(shadow = True, fontsize=11)


print(round(tmax))
print(round(Nmax))
print(round(Nmin))
print(round(tolx)/round(tmax))
plt.show()