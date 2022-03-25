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
Dane = AdapterIO.IEN_v1('Grid_LR25.rec')
N = 7
A = 0
F = 1
t0 = 193.06+15+470.53
t1 = -10
t2 = 90
dt = 5

dis_nmin = 80
dis_dn = 5
dis_nred = 130
dis_nmax = 140


dy2 = 10
ymin = 0
ymax = 100
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
fig, axs = plt.subplots(2, 1, sharex=True)
# Remove horizontal space between axes
fig.subplots_adjust(hspace=0.02, left=0.06, bottom=0.04, right=0.94, top=0.94)

# Plot each graph, and manually set the y tick values
axs[0].plot(X[N], Y[N], label='Speed [%]')
axs[0].fill_between(X[N], 99, 101, alpha=0.2, color='C0', label = r'Nominal speed $\pm 1$%')
axs[0].fill_between(X[N], dis_nred, dis_nmax, alpha=0.2, color='C1', label ='Overspeed protection')
axs[0].grid(True, linestyle='-.')
axs[0].set_title(Tytul, pad=10, fontsize = 10)
axs[0].set_xlim(t1,t2)
axs[0].set_ylim(dis_nmin, dis_nmax)
axs[0].set_xticks(np.arange(t1,t2,dt))
axs[0].set_yticks(np.arange(dis_nmin, dis_nmax, dis_dn))
axs[0].tick_params(labelcolor='blue')

#axs[0].hlines(Nmax,t1,tmax,color='gray', linestyles='dotted')
#axs[0].hlines(Nmin,t1,tmin,color='gray', linestyles='dotted')

axs[0].vlines(tmax, dis_nmin, dis_nmax, color='red', linestyles='dotted')
axs[0].vlines(tolx, dis_nmin, dis_nmax, color='red', linestyles='dotted')
axs[0].vlines(0.0, dis_nmin, dis_nmax, color='red', linestyles='dotted')
#axs[0].annotate('Overspeed \nprotection', xy=(t2, 135))
#axs[0].annotate('Nominal \nspeed', xy=(t2, 100)) #arrowprops=dict(arrowstyle='->'), xytext=(15, -10)
#axs[0].secondary_xaxis('top')
'''
axs[0].annotate(r'$t_{M}$='+str(round(tmax,ndigits=1)),xy=(tmax,dis_nmin))
axs[0].annotate(r'$t_{E}$='+str(round(tolx,ndigits=1)),xy=(tolx,dis_nmin))
axs[0].annotate(r'$N_{MAX}$='+str(round(Nmax,ndigits=1)),xy=(tmax,Nmax),horizontalalignment="center",verticalalignment='bottom')
axs[0].annotate(r'$N_{MIN}$='+str(round(Nmin,ndigits=1)),xy=(tmin,Nmin),horizontalalignment="center",verticalalignment='top')
axs[0].legend(shadow = True, fontsize=11)
'''
#the_table = plt.table(cellText=[[Nmax,Nmin,toly],[tmax,tmin,tolx]], rowLabels=('Speed [%]', 'Time [s]'), colLabels=('Maximal','Minimal','Nominal'), loc='top')

axs[1].plot(X[A], Y[A], label='Wicket gate [%]', color='red')
axs[1].plot(X[F], Y[F], label='Runner blades [%]', color='green')
axs[1].set_xlabel('Time [s]',fontsize=10)
axs[1].grid(True, linestyle='-.')
axs[1].set_ylim(ymin,ymax)
axs[1].set_yticks(np.arange(ymin,ymax,dy2))

axs[1].vlines(tmax,ymin,ymax,color='red', linestyles='dotted')
axs[1].vlines(tolx,ymin,ymax,color='red', linestyles='dotted')
axs[1].vlines(0.0,ymin,ymax,color='red', linestyles='dotted')
axs[1].legend(shadow = True, fontsize=11)
#axs[2].plot(X[3], Y[3])

print(round(tmax))
print(round(tolx))
print(round(Nmax))
print(round(Nmin))
print(round(tolx)/round(tmax))
plt.show()