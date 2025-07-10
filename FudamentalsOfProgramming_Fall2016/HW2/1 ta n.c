#include<stdio.h>
#include<math.h>

int main()
{
    int n;
    scanf("%d", &n);
    int i;
        int j=0;

    double gonde = 0;
    for(i =1; i <= n; i++){
            int k = 0;
            while (i / pow( 10, k +1) > 0)
            {
                k++;
            }
      gonde += i * pow(10,(-i)) * pow(10, k);
    }

    while(j <= n)
         {
        gonde*=10;
        j++;
    }
    printf("%d", (int)gonde % 10);

}
