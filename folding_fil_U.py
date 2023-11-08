import numpy as np
import matplotlib.pyplot as plt
import struct
import sys

if (len(sys.argv) < 5):
    print("python folding_fil.py <time resolution> <period (s)> <total number of samples> <number of channels>")
    exit(1)
filename='Read_stokes_U_dedisp_fcosed.dat'
fn=open(filename,'rb')
fp=open("profile_U.txt","w")
fp1=open("profile1_U.txt","w")
del_t=float(sys.argv[1])                   ############  sampling time interval in seconds
period=float(sys.argv[2])   ##0.2265359                   ##############    Size of runnign boxcar in seconds
samples=int(sys.argv[3])    ##1830000
chans=int(sys.argv[4])          ##128
noise=np.zeros((chans,samples),dtype='float')
for i in range(samples):
	for j in range(chans):
		
        	num=fn.read(4)
        	if num==b'':
                	break;
        	noise[j][i]=struct.unpack('f',num)[0]

#for j in range(chans):
#	noise[j]=noise[j]-np.mean(noise[j])

p=int(period/del_t)
phase=np.arange(p)/float(p)
I1=np.ones(p)
print(str(p))
profile=np.zeros((chans,p),dtype='float')
for j in range(chans):
        for i in range(samples):
                k0=((i*del_t)/period-int((i*del_t)/period))*p
                k=int(k0)
                f=k0-k
                profile[j][k]=profile[j][k]+f*noise[j][i]
                profile[j][k-1]=profile[j][k-1]+(1-f)*noise[j][i]
        profile[j]=profile[j]/(float(samples)/p)
        print(str(j)+" chans done\n")
for j in range(chans):
        for i in range(p):
            fp.write(str(profile[j][i])+" ")
        fp.write("\n")
profile1=np.mean(profile[10:110:1],axis=0)
profile1=profile1-np.mean(profile1[300:550:1])
c=plt.imshow(profile,cmap='hot',vmin=-3,vmax=3,aspect='auto')
plt.colorbar(c)
plt.savefig('Profile_U2D.png')
plt.clf()
prof=np.mean(profile[10:110:1], axis=0)
plt.plot(phase,prof)
plt.savefig('profile_U1D.png')
plt.clf()
plt.plot(phase,profile1)
plt.savefig('profile_U1Da.png')
for r in profile1:
    fp1.write(str(r)+"\n")
fn.close()
fp.close()
fp1.close()
