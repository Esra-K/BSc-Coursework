#include<stdio.h>
int main(){
    int n = 0;
int a = 0;
int b = 0;
int c = 0;
scanf("%d", &n);
scanf("%d%d%d", &a, &b, &c);
int counter = n - 3;
int ultimatum = 0;
while(counter > 0)
{
    if((b - a) * (c - b) < 0)
    {
        ultimatum++;
    }
    a = b;
    b = c;
    scanf("%d", &c);
    counter--;
    }
    int u = ultimatum;
    if(u <= 1)
    {
        printf("No");
    }
    else
    {
        printf("Yes");
    }
}
