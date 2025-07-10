#include<stdio.h>
#include<math.h>
#define max(x, y) (((x) > (y)) ? (x) : (y))
#define min(x, y) (((x) < (y)) ? (x) : (y))
//int cntr;
void fun(int a, int b, int r, int x, int y, int flag[x + 1][y + 1])
{

    int z = 0, t = 0;
    for(z = max(a - r, 1); z <= min(a + r,x); z++)
    {
        for(t = max(b - r, 1); t <= min(b + r, y); t++)
        {
            if(flag[z][t] == 0)
            {
                //printf("hello");
                //cntr--;
                flag[z][t] = 1;
            }

        }
    }
}
int main()
{
    int x = 0, y = 0, n = 0, a = 0, b = 0;
    int i = 0, j = 0;
    scanf("%d %d", &x, &y);
    int flag[x + 1][y + 1];
    for(i = 0; i < j + 1; i++)
        {
            flag[0][i] = 2;
            flag[i][0] = 2;
        }
    int cntr = 0;
    for(i = 1; i < x + 1; i++)
    {
        for(j = 1; j < y + 1; j++)
        {
            flag[i][j] = 0;
        }
    }
    scanf("%d", &n);
    int bomb[n][3];
    for(i = 0; i < n; i++)
        {
            scanf("%d %d %d", &bomb[i][0], &bomb[i][1], &bomb[i][2]);
        }
    scanf("%d %d", &a, &b);
    flag[a][b] = 1;
    int c = 0;
    for(c = 0; c < n; c++)
    {
        if(flag[bomb[c][0]][bomb[c][1]] == 1)
            {
                fun(bomb[c][0], bomb[c][1], bomb[c][2], x, y, flag);
            }
    }
        for(i = 1; i < x + 1; i++)
    {
        for(j = 1; j < y + 1; j++)
        {
            if(flag[i][j] == 0)
                cntr++;
        }
    }
    printf("%d", cntr);
    return 0;

}
