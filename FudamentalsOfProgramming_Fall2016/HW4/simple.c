#include<stdio.h>
#include<math.h>
long long int fact(int n)
{
    if(n == 0)
        return 1;
    return n * fact(n - 1);
}
int main()
{
int n = 0;
scanf("%d", &n);
long long int answer = fact(2 * n - 1) / (fact(n) * fact(n) * fact(n - 1));
printf("%lld", answer);
return 0;
}
