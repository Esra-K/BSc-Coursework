#include<stdio.h>
#include<math.h>
 int isPrime(long long int n)
 {
     long long int i = 0;
     if(n == 1)
     {
         return 0;
     }
     for(i = 2; i <= sqrt(n); i++)
     {
         if(n % i == 0)
         {
             return 0;
         }
     }
     return 1;
 }
 long long int fasele(long int k)
 {
    long long int i = 0, more = 0, less = 0;
    for(i = 0;i < k - 2;i++)
    {
        more = k + i;
        less = k - i;
        if(isPrime(less) == 1)
        {
            return i;
        }
        else if(isPrime(more) == 1)
        {
           return i;
        }

    }
    return k - 2;
 }


 int main()
 {
     long long int num = 0;
     long long int input = 0;
     scanf("%d", &num);
     long long int minnie = 9998;
     long long int counter = 0;
     for(counter = 0; counter < num; counter++)
     {
         scanf("%lld", &input);
        if(fasele(input) <= minnie)
        {
            minnie = fasele(input);
        }
     }
     printf("%lld", minnie);
     return 0;

 }

