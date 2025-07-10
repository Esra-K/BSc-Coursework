#include<stdio.h>
int main(){
    float n = 0;
    scanf("%f", &n);
int i = 1, j = 1, k = 1, t = 1;
int counter = 0;
for( i = 1 ; i < n /2 ; i++)
{
        for( j = 1 ; j < n /2 ; j++)
{for( k = 1 ; k < n /2 ; k++)
{for( t = 1 ; t < n /2 ; t++)
{
    if(i + j + k + t == n)
    {
        counter++;
    }
}
}
}
}
    printf("%d", counter);


}
