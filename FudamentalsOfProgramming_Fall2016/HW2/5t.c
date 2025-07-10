#include <stdio.h>

#define MAX 30

int main()
{
	int a, b;
	int c, d, e, f;
	int i, j;

	printf("Enter number a (1<=a<=%d):", MAX);
	scanf("%d", &a);
	if((a<1)||(a>MAX)) return(0);
	printf("Enter number b (1<=b<=%d):", a);
	scanf("%d", &b);
	if((b<1)||(b>a)||!(b%2)) return(0);
	st:
	c=2*a-1; d=(c-b)/2;
	for(i=d; i>=0; i--)
	{
		for(j=0; j<i+b; j++) if(j<i)     printf(" "); else printf("*");
		for(   ; j<c-i; j++) if(j<c-b-i) printf(" "); else printf("*");
		printf("\n");
	} 
	for(i=1; i<=d; i++)
	{
		for(j=0; j<i+b; j++) if(j<i)     printf(" "); else printf("*");
		for(   ; j<c-i; j++) if(j<c-b-i) printf(" "); else printf("*");
		printf("\n");
	}
}
