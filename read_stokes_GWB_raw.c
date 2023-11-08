#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[])
	{
	char filename[200];
	if (argc < 5){
		printf("./EXECUTABLE filename samples blocksize channels \n");
		exit(1);
	}
//	printf("Enter raw file name:");
//	scanf("%s",filename);
	char ch,ch1;
	long int i=0,val,j=0,k=0,samples=0,done=0,channels,block_size,bs;
	sscanf(argv[1], "%s", filename);
	sscanf(argv[2], "%ld", &samples);
	sscanf(argv[3], "%ld", &block_size);
	sscanf(argv[4], "%ld", &channels);
	bs=block_size*channels*4;
	float val1;
	FILE *fptr;
	FILE *fptr1,*fptr2,*fptr3,*fptr4;
        fptr1=fopen("Read_stokes_RR.dat","wb");
        fptr2=fopen("Read_stokes_lr.dat","wb");
        fptr3=fopen("Read_stokes_LL.dat","wb");
        fptr4=fopen("Read_stokes_rl.dat","wb");

	fptr=fopen(filename,"rb");
	while(1==fread(&ch1,sizeof(ch),1,fptr))
		{
			if(i%bs==0){done=done+block_size;printf("%ld samples done\n",done);} // Number of entries in 10000 samples
			val=ch1;
			val1=val;	
                       // val1=atof(&ch1);
                       //printf("%f\n",val1);
			if(i%4==0){fwrite(&val1,sizeof(val1),1,fptr1);}
			if(i%4==1){fwrite(&val1,sizeof(val1),1,fptr2);}
			if(i%4==2){fwrite(&val1,sizeof(val1),1,fptr3);}
			if(i%4==3){fwrite(&val1,sizeof(val1),1,fptr4);}
			i=i+1;
		}
	rewind(fptr);
fclose(fptr);		
fclose(fptr1);
fclose(fptr2);
fclose(fptr3);
fclose(fptr4);
}
