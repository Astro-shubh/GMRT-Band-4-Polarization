import struct
import sys
import matplotlib.pyplot as plt
import numpy as np


if (len(sys.argv) < 3):
    print("python bandshape.py <number of channels> <number of samples to compute bandshape>")
    exit(1)
frr=open('Read_stokes_RR.dat','rb')
frl=open('Read_stokes_rl.dat','rb')
flr=open('Read_stokes_lr.dat','rb')
fll=open('Read_stokes_LL.dat','rb')
frrb=open('bandshape_RR.txt','w')
frlb=open('bandshape_rl.txt','w')
flrb=open('bandshape_lr.txt','w')
fllb=open('bandshape_LL.txt','w')
#del_t=float(sys.argv[1])
chans=int(sys.argv[1])
samps=int(sys.argv[2])

noise=[]
i=0
band=np.zeros(chans)
while True:
        num=frr.read(4)
        if num==b'':
            break;
        noise.append((struct.unpack('f',num)[0]))
        i=i+1
        if i==samps*chans:
            break;
noise=np.array(noise)
j=0
k=0
for r in noise:
        if j%chans==0:
            k=0
        band[k]=band[k]+r/float(samps)
        k=k+1
        j=j+1
for r in band:
        frrb.write(str(r)+"\n")

noise=[]
i=0
band=np.zeros(chans)
while True:
        num=fll.read(4)
        if num==b'':
            break;
        noise.append((struct.unpack('f',num)[0]))
        i=i+1
        if i==samps*chans:
                break;
noise=np.array(noise)
j=0
k=0
for r in noise:
        if j%chans==0:
                k=0
        band[k]=band[k]+r/float(samps)
        k=k+1
        j=j+1
for r in band:
        fllb.write(str(r)+"\n")

noise=[]
i=0
band=np.zeros(chans)
while True:
        num=frl.read(4)
        if num==b'':
                break;
        noise.append((struct.unpack('f',num)[0]))
        i=i+1
        if i==samps*chans:
                break;
noise=np.array(noise)
j=0
k=0
for r in noise:
        if j%chans==0:
                k=0
        band[k]=band[k]+r/float(samps)
        k=k+1
        j=j+1
for r in band:
        frlb.write(str(r)+"\n")

noise=[]
i=0
band=np.zeros(chans)
while True:
        num=flr.read(4)
        if num==b'':
                break;
        noise.append((struct.unpack('f',num)[0]))
        i=i+1
        if i==samps*chans:
                break;
noise=np.array(noise)
j=0
k=0
for r in noise:
        if j%chans==0:
                k=0
        band[k]=band[k]+r/float(samps)
        k=k+1
        j=j+1
for r in band:
        flrb.write(str(r)+"\n")

		
frrb.close()
fllb.close()
frlb.close()
flrb.close()
frr.close()
fll.close()
frl.close()
flr.close()

