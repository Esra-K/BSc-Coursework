#include<stdio.h>
#include<math.h>
int f(int a)
{
    int fdemand = 0;
    int d = 1;
    for(d = 1; d <= sqrt(a); d++)
    {
        if(a % d == 0)
        {
            fdemand+= d;
            fdemand+= (a / d);
        }
    }
    if (pow(d - 1, 2) == a)
    {
        fdemand-= (d - 1);
    }
    return fdemand;
}

int g(int b, int base)
{
 int basenum = 0;
 while(b>= base)
 {
     basenum+= (b % base);
     b/= base;
 }
 basenum+= b;
 return basenum;
}
int main()
{
    int n = 0;
    int k = 0;
    scanf("%d %d", &n, &k);
    int answer = 0;
    int i = 1;
    for( i = 1; i <= (n / 2); i++)
    {
        if((n % i) == 0)
        answer+= (f(i) * g((n / i), k));
    }
    answer+= (f(n) * g(1, k));
    printf("%d", answer);
}
