#include<stdio.h>


void main()

{
   int D=0;
   printf("enter the degree you want to be massaged(edit:massacred) to");
   scanf("%d",&D);
   
   int t=5;
   int s=45 * (D-1);
   int m=s / 60;
   float c=03.29 + (D-1) * 0.04;

   printf("Welcome to my hammam!\nI will rub you with kise with degree %d and this will approximately last %d:%d!\nAt the end you should give me $ %.2f.Have fun!", D, t + m, s % 60, c);
}
   








#include<stdio.h>


void main()
{
    int i=0, j=0;
    printf("shomareha lotfan!");
    scanf("Mr.Bit's answer is %d\nMr.Bit's friend's answer is %d", &i, &j);
    
    int k= i ^ j;
    int l= k % 2;
    int m= (k / 2) % 2;
    int n= ((k / 2) / 2) % 2;
    int o= ((k / 2) / 2) / 2;
    printf("%d", m + n + o);
}










#include<stdio.h>

void main()
{ 
	unsigned int m=0;
	printf("some input,please!");	
	 scanf("%u",m);
      int d= m % 2;
      if(d= 0)
{
      unsigned int n= m / 2;
      printf(" %o", n);
}
      else
{
      unsigned int v= (m / 2) + 128;
      printf("%o", v);
}  
}    
 



















#include<stdio.h>

void main()
{     
	int n=0;
 	int a=1;
	int b=2;
	int c=4;
	int d=8;
	int e=16;
	int f=32;
	int g=64;
	int h=128;
        
       printf("enter a number");
	scanf("%u",&n);
        if(n % 2==0);
{ 	printf("%d",a);
}
        else if ((n>>1) % 2==0);
{ 	printf("%d",b);
}
	else if ((n>>2) % 2==0);
{ 	printf("%d",c);
}
	else if ((n>>3) % 2==0);
{ 	printf("%d",d);
}
	else if ((n>>4) % 2==0);
{ 	printf("%d",e);
}
	else if ((n>>5) % 2==0);
{ 	printf("%d",f);
}
	else if ((n>>6) % 2==0);
{ 	printf("%d",g);
}
	else if (n>>7 % 2==0);
{ 	printf("%d",h);
}
	else
{	printf("the number is 255 and has no 1 in the binary system");
}
}
   