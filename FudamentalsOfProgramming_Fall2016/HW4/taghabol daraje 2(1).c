#include<stdio.h>
#include<math.h>
int isprime(long long int n)
{
    if(n == 1)
        return 0;
    long long int i = 2;
    for(i = 2; i * i <= n; i++)
    {
        if(n % i == 0)
            return 0;
    }
    return 1;
}
int koochektarinmaghsoomelayh(long long int n)
{
    long long int i = 2;
    for(i = 2; i * i < n; i++)
    {
        if(n % i == 0)
            return i;
    }
}
int taghabol(long long int a, long long int p)
{
    a = a % p;
    long long int i = 0;
    if(a == 1)
        return 1;
    if(a == 0)
        return 0;
    if(a == 2)
        {
         if(((p * p - 1) / 8) % 2 == 0)
          return 1;
          return -1;
        }
    if(isprime(a) == 1)
    {    if(((p - 1) * (a - 1) / 4) % 2 == 0)
            return taghabol(p , a);
         else
            return -1 * taghabol(p , a);
    }
        else
        i =koochektarinmaghsoomelayh(a);
        a/= i;
        return taghabol(i, p) * taghabol(a , p);
}

int main()
{
    long long int n = 0;
    scanf("%lld", &n);
    long long int i = 0;
    for(i = 0; i < n; i++)
    {
        long long int a = 0, p = 0;
        scanf("%lld %lld", &a, &p);
        printf("%lld", taghabol(a, p));
    }

    return 0;
}

