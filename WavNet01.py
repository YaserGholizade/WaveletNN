import numpy as np
import matplotlib.pyplot as plt

n=1
lam=1
#----------------------
def Psi(t,a,b):
    P=np.zeros(len(t))
    for i in range(len(t)):
        if 0<=(a*t[i]-b)<=1:
            P[i]=1
        else:
            P[i]=0
    return P
#----------------------
def FuncApp(x,w):
    z=(x-w[0:n])/w[n:2*n]
    A1=Psi(z,1,0)
   # A2=Psi(z,2,0)
   # A3=Psi(z,2,1)
    B=A1*w[2*n] #+A2*w[2*n+1]+A3*w[2*n+2]
    y=x*(w[2*n+1:-1])+B+w[-1]
    return y




# creat traing data
x=np.arange(0,1,0.05)
y=x#+np.random.uniform(-0.15,0.15,len(x))
plt.plot(x,y,'ob')
Ytra=np.array(y)


eta=0.02
kapa=0.05

w_old=np.random.uniform(0,1,3*n+lam+1)
w_old[0]=0
w_old[1]=1
print(w_old)
Ep=np.zeros(201)
for k in range(201):
    Yapp=np.zeros(len(x))
    ep=np.zeros(len(x))
    for j in range(len(x)):
        Yapp[j]=FuncApp(x[j],w_old)
        ep[j]=(Yapp[j]-Ytra[j])

    Ep[k]=1/2*np.sum(ep**2)
        #print(Ep)
    PLtoPw=np.array([0,0,np.sum(Psi(x,1,0)*ep),np.sum(x*ep),np.sum(ep)])   # np.sum(Psi(x,2,0)*ep),np.sum(Psi(x,2,1)*ep)
    if k==0:
        w_new=w_old-(eta/n)*PLtoPw+kapa*(w_old)
    else:
        w_new=w_old-(eta/n)*PLtoPw+kapa*(w_old-w_older)
    w_older=w_old[:]
    w_old=w_new[:]
    for i in range(len(x)):
        Yapp[i]=FuncApp(x[i],w_new)
    plt.plot(x,Yapp,'r',linewidth=2)
    plt.plot(x,y,'ob')
    plt.title(str(k))
    plt.pause(0.1)
    if k!=200:
        plt.clf()



Yapp=np.zeros(len(x))
for i in range(len(x)):
    Yapp[i]=FuncApp(x[i],w_new)
plt.plot(x,y,'ob')
plt.plot(x,Yapp,'r',linewidth=2)
plt.show()
print(w_new)
plt.show()
print(Ep[-1])




