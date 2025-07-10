#include<stdio.h>
int main()
{
    int n = 0;
    scanf("%d", &n);
     int i = 1;
     int count = 0;
     int num = 0;
     for(i = 1;count < n ; i++)
     {
         num = (i * (i+1)) / 2;
         count = 1;
         int d = 1;
         while( d * d <= num )
         {
            if(num % d == 0)
         {
             count+= 2;
         }
             d++;
         }

         if((d - 1) * (d - 1) == num)
         {
             count--;
         }

            printf("%d\n", num);


         }
         int f = 2;
         for( f = 2;(f * f) <= num; f++ )
         {
             while(num % f ==0)
             {
                 printf("%d,", &f);
                 num/= f;
             }
         }
     return 0;
}
