#include<stdio.h>
#include<math.h>
 int isPrime(int n)
 {

     int i = 0;
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

 int help(int c)
 {
     int hh = 0;
     int d = 0;
     int j = 1;
     for( j = 1; d < c; j++)
     {
         if(isPrime((j) == 1))
         {
             d++;
             hh = j;
         }
     }
     return hh;
}

int function(int k)
 {

 int counter = 0;
 int lesserprime = 1;
 int particle = 1;
     if(isPrime(k) == 1)
     {
         for(lesserprime = 2; lesserprime < k; lesserprime++)
         {
             if(isPrime(lesserprime) == 1)
                counter++;
         }
     }

     else
     {
         for(particle = 2; particle <= k / 2; particle++)
         {
             if(isPrime(particle) == 1)
                 if(k % particle == 0)
                 {
                     counter++;
                 }
         }
     }
     return counter;
}


     int main()
     {
         int x = 0;

         scanf("%d", &x);

         int sum = 0;
         int input = 0;
         int ctrl = 0;
         for(ctrl = 0; ctrl < x; ctrl++)
         {
          scanf("%d", &input);
          sum+= function(input);
         }
         sum-= function(sum);
         printf("%d", sum);

         return 0;
    }

