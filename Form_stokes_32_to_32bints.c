#include <stdio.h>
#include <stdlib.h>
#include<math.h>

int main(int argc, char *argv[])
        {
//    CHecking arguments
        if (argc < 4){
                printf("./EXECUTABLE <blocksize> <total samples> <channels> \n");
                exit(1);
        }
// Defining variables

        char ch,ch1;
        long int i=0,val,j=0,k,size=0,sample=100000,chans=4096,blocks,total_samps=1840000,SI,SQ,SU,SV;
        float rr,rl,lr,ll,I,Q,U,V,rsqrt,lsqrt,val1,bandr[chans],bandl[chans],nsamp=100000.0,nchan=4096.0,ntot=1830000.0;

        FILE *fpt1,*fpt2,*fpt3,*fpt4,*frrb,*fllb;
        FILE *fptr1,*fptr2,*fptr3,*fptr4;
// Parsing variables
        sscanf(argv[1], "%ld", &sample);
	sscanf(argv[1], "%f", &nsamp);
        sscanf(argv[2], "%ld", &total_samps);
	sscanf(argv[2], "%f", &ntot);
        sscanf(argv[3], "%ld", &chans);
        sscanf(argv[3], "%f", &nchan);


//opening files
        fptr1=fopen("Read_stokes_RR.dat","rb");
        fptr2=fopen("Read_stokes_lr.dat","rb");
        fptr3=fopen("Read_stokes_LL.dat","rb");
        fptr4=fopen("Read_stokes_rl.dat","rb");
        fpt1=fopen("Form_stokes_I.dat","wb");
        fpt2=fopen("Form_stokes_Q.dat","wb");
        fpt3=fopen("Form_stokes_U.dat","wb");
        fpt4=fopen("Form_stokes_V.dat","wb");
	frrb=fopen("bandshape_RR.txt","r");
	fllb=fopen("bandshape_LL.txt","r");
// Reading bandshape
	for(i=0;i<chans;i++)
	{
		fscanf(frrb,"%f",&val1);
		bandr[i]=val1;
	//	printf("%f\n",val1);
	}
        for(i=0;i<chans;i++)
        {
                fscanf(fllb,"%f",&val1);
                bandl[i]=val1;
        //        printf("%f\n",val1);
        }
	for(i=0;i<total_samps;i++)
	{
		for(j=0;j<chans;j++)
		{
			fread(&rr,sizeof(rr),1,fptr1);
			fread(&rl,sizeof(rl),1,fptr4);
			fread(&lr,sizeof(lr),1,fptr2);
			fread(&ll,sizeof(ll),1,fptr3);
//			rsqrt=sqrt(bandr[j]+1.0)
//			lsqrt=sqrt(bandl[j]+1.0)
			I=(rr/(bandr[j]+1.0))+(ll/(bandl[j]+1.0));
			V=(rr/(bandr[j]+1.0))-(ll/(bandl[j]+1.0));
			Q=2.0*rl/sqrt((bandr[j]+1.0)*(bandl[j]+1.0));
			U=2.0*lr/sqrt((bandr[j]+1.0)*(bandl[j]+1.0));
			fwrite(&I,sizeof(I),1,fpt1);
			fwrite(&V,sizeof(V),1,fpt4);
			fwrite(&Q,sizeof(Q),1,fpt2);
			fwrite(&U,sizeof(U),1,fpt3);
		}
		if(i%10000==0){printf("%ld samples done\n",i);}
	}				
	
fclose(frrb);
fclose(fllb);
fclose(fpt1);
fclose(fpt2);
fclose(fpt3);
fclose(fpt4);
fclose(fptr1);
fclose(fptr2);
fclose(fptr3);
fclose(fptr4);
}



