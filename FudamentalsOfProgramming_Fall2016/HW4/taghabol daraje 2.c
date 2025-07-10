#include<stdio.h>
long long int isprime(long long int n)
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
long long int koochektarinmaghsoomelayh(long long int n, long long int p)
{
    long long int i = 2;
    for(i = 2; i < p; i++)
    {
        if(n % i == 0)
            return i;
    }
}
long long int taghabol(long long int a, long long int p)
{
    long long int i = 0;
    if(a == 1)
        return 1;
    if(a == p)
        return 0;
    if(a == 2)
        {
         if(((p * p - 1) / 8) == 0)
          return 1;
        else
          return -1;
        }
     a = a % p;
    if(isprime(a) == 1)
    {    if(((p - 1) * (a - 1) / 4) % 2 == 0)
            return taghabol(p , a);
         else
            return -1 * taghabol(p , a);
    }
        else
        i =koochektarinmaghsoomelayh(a, p);
        a/= i;
        return taghabol(i, p) * taghabol(a , p);
}
long long int taghabol(long long int a, long long int p);
long long int main()
{
    long long int n = 0;
    scanf("%d", &n);
    long long int i = 0;

    for(i = 0; i < n; i++)
    {
        long long int a = 0, p = 0;
        scanf("%d %d", &a, &p);
        printf("%d", taghabol(a, p));
    }

    return 0;
}

