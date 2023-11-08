import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def fit_line(x,m,c):
	y=m*x+c
	return(y)
fQ=open("profile_Q.txt","r")
fU=open("profile_U.txt","r")
fcal=open("calibration.txt","w")
fprof=open("profile1_I.txt","r")
y=[]
for r in fprof:
    y.append(float(r))
y=np.array(y)
x=np.arange(len(y))
bins=len(y)
plt.title('Profile')
plt.plot(x,y)
plt.show()
ref_samp=int(input('Enter ref sample (bin of the peak):'))
off_start=int(input('Enter off start bin:'))
off_end=int(input('Enter off start bin:'))
chans=int(input('Enter number of channels:'))
Q=[]
U=[]

prof_Q=np.zeros((chans,bins),dtype='float')
prof_U=np.zeros((chans,bins),dtype='float')
for line in fQ:
	s=[float(r) for r in line.split()]
	Q.append(s[ref_samp])
for line in fU:
        s=[float(r) for r in line.split()]
        U.append(s[ref_samp])
psi=[]
i=0
for r in Q:
	if(U[i]==0):
		psi.append(0.)
	else:
		psi.append(0.5*np.arctan2(r,U[i]))
	i=i+1
freq=np.arange(chans)
plt.xlabel('Channel number')
plt.ylabel('Phase (rad)')
plt.plot(freq,psi)
plt.show()
ch_start=int(input("Enter start of usable channels\n"))
ch_end=int(input("Enter end of usable channels\n"))
Q1=[]
i=0
freq1=[]
for r in Q:
	if(i>ch_start):
		if(i<ch_end):
			Q1.append(r)
			freq1.append(i)
	i=i+1
i=0
U1=[]
for r in U:
        if(i>ch_start):
                if(i<ch_end):
                        U1.append(r)
        i=i+1
		
psi1=[]
i=0
for r in Q1:
        if(r==0):
                psi1.append(0.)
        else:
                psi1.append(0.5*np.arctan2(r,U1[i]))
        i=i+1
plt.xlabel('Channel number')
plt.ylabel('Phase (rad)')
plt.plot(freq1,psi1)
plt.show()
i=0
psi_unw=[]
for j in range(len(psi1)):
    if(abs(psi1[j]-psi1[j-1])>3.0):
            i=i+1
    psi_unw.append(psi1[j]+i*np.pi)
plt.xlabel('Channel number')
plt.ylabel('Phase (rad)')
plt.plot(freq1,psi_unw)
plt.show()
freq1=np.array(freq1)
psi_unw=np.array(psi_unw)
mc,_=curve_fit(fit_line,freq1,psi_unw)
m,c=mc
print("slope: "+str(m)+"\n intersection: "+str(c))
plt.xlabel('Channel number')
plt.ylabel('Phase (rad)')
plt.plot(freq1,psi_unw)
plt.plot(freq1,fit_line(freq1,m,c))
plt.show()
i=0
U_new=np.zeros((len(freq1)),dtype='float')
Q_new=np.zeros((len(freq1)),dtype='float')
for j in freq1:
	U_new[i]=U1[i]*np.cos(2.*(m*j+c))+Q1[i]*np.sin(2.*(m*j+c))
	Q_new[i]=Q1[i]*np.cos(2.*(m*j+c))-U1[i]*np.sin(2.*(m*j+c))
	i=i+1
psi_new=[]
i=0
for r in Q_new:
        if(r==0):
                psi_new.append(0.)
        else:
                psi_new.append(0.5*np.arctan2(r,U_new[i]))
        i=i+1
fcal.write(str(ch_start)+" "+str(ch_end)+" "+str(m)+" "+str(c)+"  "+str(chans)+"  "+str(off_start)+"  "+str(off_end)+"  "+str(bins))
plt.xlabel('Channel number')
plt.ylabel('Calibrated phase (rad)')
plt.plot(freq1,psi_new)
plt.show()
