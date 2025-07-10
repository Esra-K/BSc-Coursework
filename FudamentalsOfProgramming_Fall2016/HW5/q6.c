#include<stdio.h>
#include<math.h>
//#include<conio.h>
void bubble(int a[],int s)
{
 int i,j;
 int temp;
 for(i=1;i<s;i++)
  {
    for(j=0;j<s-i;j++)
     {
      if(a[j]>a[j+1])
       {
        temp=a[j];
        a[j]=a[j+1];
        a[j+1]=temp;
       }
     }
   }
}
int main()
{
    int n = 0;
    scanf("%d", &n);
    int x[n], y[n];
    int i = 0;
    for(i = 0; i <= n - 1; i++)
    {
        scanf("%d %d", &x[i], &y[i]);
    }
//    if(n == 1 || n == 2)
//    {
//        printf("0");
//        return 0;
//    }
    int num = n * (n - 1) / 2;
    int j = 0, k = 0, com = 0, shib[num], arz[num];
    for(i = 0; i < n - 1; i++)
    {
        for(j = i + 1; j < n - 1; j++)
        {
            if(x[i] == x[j])
            {
                shib[k] = 1006;
                arz[k] = 2017;
            }
            else
            {
                shib[k] = (y[j] - y[i]) / (x[j] - x[i]);
                arz[k] = y[i] - shib[k] * x[i];
            }
            k++;
        }
    }
    int cntr[num];
    int counter2 = 1;
    for(counter2 = 0; counter2 < num; counter2++)
    {
        cntr[counter2] = 1;
    }
    int counterline = 0, counter = 0,counterplus = 0;

    for(counter = 0; counter < num - 1; counter++)
    {
      for(counterplus = counter + 1; counterplus < num; counterplus++)
      {
          if(shib[counter] == shib[counterplus] && arz[counter] == arz[counterplus])
            cntr[counterline]++;
            //cntr[counterplus] = -1000;
      }
      counter++;
    }
    int dots = 0, number = 0;
    for(number = 0; number < num; number++)
    {
        if(cntr[number] > 1)
        {
          dots+= (1 + sqrt(1 + 8 * cntr[number])) / 2;
        }
    }
    printf("%d", dots);
    return 0;
}
