import matplotlib.pyplot as plt
import numpy as np
import statistics as st
from scipy import stats

data = [[73,65,70],[64,61,67],[72,63,66],[58,71,56],[54,70,61],[57,48,56]]

Averaget = []
for i in data:
    Averaget.append(st.mean(i))
    
#define global vars

eoverD = 0.0063

vis = 0.001002 # Pa * s

D = float(0.0127)  #m

rho = 1000 #kg/m^3

vol = 5 * 10**-4 #m^3

height = [1,1.5,2,2.5,3,3.5]

heightM = []
for i in height: 
    heightM.append(i * 0.3048)
    
#define Re

def calcRe(v,vis,D,rho):
    return (D*v*rho)/vis

#calc averageV

areaXS = 3.1415 * (D/2)**2


def flow_rate(vol,t):
    return vol/t

def calcV(flow,area):
    if area > 0:
        return flow/area #m/s

averageV = []
for i in Averaget:
    temp_rate = flow_rate(vol,i)

    temp_v = calcV(temp_rate,areaXS)

    averageV.append(temp_v)

#define the function of Re for friction factor (13-15a)

def ff_turb(Re,eoverD):
    
    inside = 6.9/Re + (eoverD*1/3.7)**(10/9)
    out = -3.6 * np.log10(inside)
    #recip and square to get ff
    
    sq = 1/out
    
    return sq**2

#find the Re of the data

Redata = []

for i in averageV:
    Redata.append(calcRe(i,vis,D,rho))
    
#plot the data
minV = min(averageV)
maxV = max(averageV)

minRe = calcRe(minV,vis,D,rho)
maxRe = calcRe(maxV,vis,D,rho)

#calc ff for data
ffdata = []
for i in Redata:
    ffdata.append(ff_turb(i,eoverD))

X = np.linspace(minRe,maxRe,100)
Y = []
for i in X:
    Y.append(ff_turb(i,eoverD))

X_tick = np.linspace(minRe,maxRe, 3)

plt.plot(X,16/X)
plt.plot(X,Y, label = r'$Formula$')
plt.plot(Redata,ffdata, label = r'$Data$', marker = 'o')
plt.title(r'$f_f \: compared \: to \: Re$')
plt.xlabel(r'$Re$')
plt.xticks(np.arange(minRe,maxRe, step = 25))
plt.ylabel(r'$f_f$')
plt.legend()
plt.show()
