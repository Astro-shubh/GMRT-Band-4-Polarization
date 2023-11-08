#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc, char *argv[])
        {
        if (argc < 4){
                printf("./EXECUTABLE <total samples> <number of channels> <number of channels to collapse> \n");
                exit(1);
        }

        char ch,ch1;
        long int i=0,val,j=0,k,dl,size=0,sample=1830000,chans=4096,rr=0,rl=0,lr=0,ll=0;
	float df,sumj,val1,samplef=1830000.0,chansf=4096.0;
        sscanf(argv[1], "%ld", &sample);
        sscanf(argv[1], "%f", &samplef);
        sscanf(argv[2], "%ld", &chans);
        sscanf(argv[2], "%f", &chansf);
        sscanf(argv[3], "%f", &df);
	sscanf(argv[3], "%ld", &dl);

	FILE *fptr,*fptw;
	fptr=fopen("Read_stokes_V_dedisp.dat","rb");
	fptw=fopen("Read_stokes_V_dedisp_fcosed.dat","wb");
	for(i=0;i<sample;i++)
	{
		sumj=0.0;
		for(j=0;j<chans;j++)
		{
			fread(&val1,sizeof(val1),1,fptr);
			sumj=sumj+val1/df;
			if(j%dl==0){fwrite(&sumj,sizeof(sumj),1,fptw);sumj=0.0;}
		}
		if(i%100000==0){printf("%ld samples done\n",i);}
	}
	fclose(fptr);
	fclose(fptw);
			
	}
