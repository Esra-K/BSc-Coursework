#include<stdio.h>
void swapping(int a, int b)
{
    int hold = 0;
    hold = a;
    a = b;
    b = hold;
}
int main()
{
    int n = 0;
    scanf("%d", &n);
    int i = 0, hei[n], wei[n], area[n], kise[n], mosht[n];
    for(i = 0; i <= n - 1; i++)
    {
        scanf("%d %d %d %d %d", &hei[i], &wei[i], &area[i], &kise[i], &mosht[i]);
    }
    int bubble = 1;
    for(bubble = 1; bubble != 0; bubble++)
    {   bubble = 0;
        for(i = 0; i < n - 1; i++)
        {
            if(wei[i] > wei[i + 1])
            { bubble++;
              swapping(hei[i], hei[i + 1]);
              swapping(wei[i], wei[i + 1]);
              swapping(area[i], area[i + 1]);
              swapping(kise[i], kise[i + 1]);
              swapping(mosht[i], mosht[i + 1]);
            }
        }
    }
    for(i = 0; i <= n - 1; i++)
    {
      printf("%d %d %d %d %d\n", hei[i], wei[i], area[i], kise[i], mosht[i]);
    }
    return 0;
}
