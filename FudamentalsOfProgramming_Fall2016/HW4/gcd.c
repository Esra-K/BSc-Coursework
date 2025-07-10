#include<stdio.h>
#include<math.h>
int gcd(int a, int b)
{   int i = 0;
    if(a < b)
    {
        i = a;
        a = b;
        b = i;
    }
    int d = 1;
    int nokhodi = 0;
    while(a % b != 0)
    {
      nokhodi = a % b;
      a = b;
      b = nokhodi;
    }
    return b;
}
int main()
{
    int n = 0;
    scanf("%d", &n);
    int a, b = 0;
    int counter = 0;
    for(counter = 0; counter < n; counter ++)
    {
        scanf("%d %d", &a, &b);
        printf("%d\n", gcd(a, b));
    }
return 0;
}
