#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(int argc, char *argv[])
{

        if (argc < 8){
                printf("./EXECUTABLE <total samples> <block size> <channels> <time resolution (s)> <DM> <Bandwidth (MHz)> <first channel freq (MHz)>\n");
                exit(1);
        }

	FILE *fr,*fw;
	fr=fopen("Form_stokes_V.dat","r");
	fw=fopen("Read_stokes_V_dedisp.dat","w");
	long long int l1,l2,l3,l4;
	long int i,j,k,blr=100000,blr1,max_d,chans=4096,tot_samps=1830000,j0[chans],blocks;
	float BW=200.0,ch1=550.0,del_f,del_t=0.00032768,value,value1,chansf=4096.0,totf=1830000,blf=100000.0,DM=3.2;
	float *read1,*read2,*write;

        sscanf(argv[1], "%ld", &tot_samps);
        sscanf(argv[1], "%f", &totf);
        sscanf(argv[2], "%ld", &blr);
        sscanf(argv[2], "%f", &blf);
        sscanf(argv[3], "%ld", &chans);
        sscanf(argv[3], "%f", &chansf);
	sscanf(argv[4], "%f", &del_t);
        sscanf(argv[5], "%f", &DM);
        sscanf(argv[6], "%f", &BW);
        sscanf(argv[7], "%f", &ch1);

	del_f=BW/chansf;
	for(j=0;j<chans;j++)
	{
		j0[j]=((DM*4150.*(1/((ch1+j*del_f)*(ch1+j*del_f))-1/((ch1+BW)*(ch1+BW))))/del_t);
//		printf("%ld\n",j0[j]);

	}
	max_d=j0[0];
	read1=(float*) calloc(blr*chans,sizeof(float));
	read2=(float*) calloc((blr)*chans,sizeof(float));
	write=(float*) calloc((blr-max_d)*chans,sizeof(float));
	blocks=totf/blf;
	for(k=0;k<blocks;k++)
	{
		printf("started block %ld of %ld",k,blocks); 
		if(k==0)
		{
			l3=blr*chans;
			for(l1=0;l1<l3;l1++)
			{
				fread(&value,sizeof(float),1,fr);
				*(read1+l1)=value;
				if(l1>l3-max_d*chans)
				{
					l4=l1+max_d*chans-l3;
					*(read2+l4)=value;
				}
					

			}
//			printf("reading done\n");
			l2=(blr-max_d)*chans;
			for(l1=0;l1<l2;l1++)
			{
				j=l1%chans;
				value1=*(read1+j0[j]*chans+l1);
				fwrite(&value1,sizeof(value1),1,fw);
			}
//		printf("dedisp done\n");
		free(read1);
		free(write);
		}
		else
		{
			read1=(float*) calloc(blr*chans,sizeof(float));
//			printf("started next block\n"); 
			l4=max_d*chans;
			for(i=0;i<l4;i++)
			{
				*(read1+i)=*(read2+i);
			}
//			printf("interchange of arrays done\n");
			free(read1);
			read2=(float*) calloc((blr)*chans,sizeof(float));
			write=(float*) calloc((blr-max_d)*chans,sizeof(float));


                        l3=(blr-max_d)*chans;
			*(read1+1)=10.0;
//			printf("reading started\n");
                        for(l1=0;l1<l3;l1++)
                        {
                                fread(&value,sizeof(float),1,fr);
                                *(read1+l1+max_d*chans)=value;
                                if(l1>l3-max_d*chans)
                                {
                                        l4=l1+max_d*chans-l3;
                                        *(read2+l4)=value;
                                }

                                
                        }
//			printf("reading done\n");
                        l2=(blr-max_d)*chans;
                        for(l1=0;l1<l2;l1++)
                        {
                                j=l1%chans;
                                value1=*(read1+j0[j]*chans+l1);
                                fwrite(&value1,sizeof(value1),1,fw);
                        }
                free(read1);
		}
	}
	
fclose(fr);
fclose(fw);
	
}
	


