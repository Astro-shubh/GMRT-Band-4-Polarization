import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def fit_line(x,m,c):
        y=m*x+c
        return(y)
fI=open('profile_I.txt','r')
fV=open('profile_V.txt','r')
fQ=open("profile_Q.txt","r")
fU=open("profile_U.txt","r")
fl=open("profile_L.txt","w")
fpsi=open("profile_psi.txt","w")

fcal=open("calibration.txt","r")
for line in fcal:
        s=[float(r) for r in line.split()]
        ch_start=int(s[0])
        ch_end=int(s[1])
        m=s[2]
        c=s[3]
        chans=int(s[4])
        s_start=int(s[5])
        s_end=int(s[6])
        bins=int(s[7])
ref_samp=635
Q=[]
U=[]
prof_I=np.zeros((chans,bins),dtype='float')
prof_V=np.zeros((chans,bins),dtype='float')
prof_Q=np.zeros((chans,bins),dtype='float')
prof_U=np.zeros((chans,bins),dtype='float')
i=0
for line in fQ:
	s=[float(r) for r in line.split()]
	prof_Q[i]=np.array(s)
	i=i+1 
i=0

for line in fU:
        s=[float(r) for r in line.split()]
        prof_U[i]=np.array(s)
        i=i+1

i=0

for line in fI:
        s=[float(r) for r in line.split()]
        prof_I[i]=np.array(s)
        i=i+1
i=0

for line in fV:
        s=[float(r) for r in line.split()]
        prof_V[i]=np.array(s)
        i=i+1
old_I=np.sum(prof_I[ch_start:ch_end,:],axis=0)
old_I=old_I-np.mean(old_I[s_start:s_end:1])
old_V=np.sum(prof_V[ch_start:ch_end,:],axis=0)
old_V=old_V-np.mean(old_V[s_start:s_end:1])
old_U=np.sum(prof_U[ch_start:ch_end,:],axis=0)
old_U=old_U-np.mean(old_U[s_start:s_end:1])
old_Q=np.sum(prof_Q[ch_start:ch_end,:],axis=0)
old_Q=old_Q-np.mean(old_Q[s_start:s_end:1])
L_old=np.zeros((bins),dtype='float')
PSI_old=np.zeros((bins),dtype='float')
norm=max(old_I)

for i in range(bins):
        L_old[i]=np.sqrt(old_U[i]*old_U[i]+old_Q[i]*old_Q[i])
        PSI_old[i]=0.5*np.arctan2(old_Q[i],old_U[i])



L_prof=np.zeros((bins),dtype='float')/norm
old_V=old_V/norm
L_old=L_old/norm
old_I=old_I/norm
PSI_prof=np.zeros((bins),dtype='float')
phase=np.arange(len(L_old))/float((len(L_old)))
PSI_old=PSI_old*180/np.pi
fig=plt.figure()
ax1=fig.add_axes([0.1,0.1,0.8,0.3],xlabel="Phase",ylabel="PPA(degrees)")
ax2=fig.add_axes([0.1,0.45,0.8,0.5],xlabel="Phase",ylabel="Stokes Parameters")
ax1.plot(phase,PSI_old)
ax2.plot(phase,old_I,label="total intensity")
ax2.plot(phase,L_old,label="linear polarisation")
ax2.plot(phase,old_V,label="Circular polarisation")
plt.legend()
plt.show()


new_U=[]
new_Q=[]


for i in range(bins):
        Qnew=0
        Unew=0
        for j in range(ch_start,ch_end):
                Unew=Unew+prof_U[j][i]*np.cos(2.*(m*j+c))+prof_Q[j][i]*np.sin(2.*(m*j+c))
                Qnew=Qnew+prof_Q[j][i]*np.cos(2.*(m*j+c))-prof_U[j][i]*np.sin(2.*(m*j+c))
#	new_U.append(Unew/(float(ch_end-ch_start)))
#	new_Q.append(Qnew/(float(ch_end-ch_start)))
        new_U.append(Unew)
        new_Q.append(Qnew)
	
new_U=np.array(new_U)
new_U=new_U-np.mean(new_U[s_start:s_end:1])
new_Q=np.array(new_Q)
new_Q=new_Q-np.mean(new_Q[s_start:s_end:1])
for i in range(bins):
	L_prof[i]=np.sqrt(new_U[i]*new_U[i]+new_Q[i]*new_Q[i])
	PSI_prof[i]=0.5*np.arctan2(new_Q[i],new_U[i])		

PSI_prof=PSI_prof*180/np.pi
L_prof=L_prof/norm
phase=np.arange(bins)/float(bins)
fig=plt.figure()
ax1=fig.add_axes([0.1,0.1,0.8,0.3],xlabel="Phase",ylabel="PPA(degrees)")
ax2=fig.add_axes([0.1,0.45,0.8,0.5],xticklabels=[],ylabel="Stokes Parameters")
ax1.plot(phase,PSI_prof)
ax2.plot(phase,old_I,label="total intensity")
ax2.plot(phase,L_prof,label="linear polarisation")
ax2.plot(phase,old_V,label="Circular polarisation")
plt.legend()
plt.show()

plt.scatter(phase,PSI_prof)
plt.scatter(phase,PSI_old)
plt.show()
for r in L_prof:
	fl.write(str(r)+"\n")
for r in PSI_prof:
        fpsi.write(str(r)+"\n")
fl.close()
fpsi.close()
fQ.close()
fU.close()



