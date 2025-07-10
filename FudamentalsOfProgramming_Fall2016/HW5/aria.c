#include<stdio.h>
void bubble(int arr[], int n)
{

    int counter = 0, i = 0, sweep = 0;
    for(counter = 0; counter < n; counter++)
    {
        for(i = 0; i < n - 1; i++)
        {
            if(arr[i] > arr[i + 1])
            {
                sweep = arr[i + 1];
                arr[i + 1] = arr[i];
                arr[i] = sweep;
            }
        }
    }
}
int main()
{
    int row = 0, column = 0, snack = 0;
    scanf("%d %d %d", &row, &column, &snack);
    int i = 0, snacky[snack + 1];
        snacky[0] = 0;

    for(i = 1; i <=snack ; i++)
    {
        scanf("%d", &snacky[i]);
    }
    int r = 0, c = 0, seat[row + 1][column + 1], extra = 0;
    for(r = 1; r <= row; r++)
    {
        for(c = 1; c <= column; c++)
        {
            scanf("%d ", &seat[r][c]);
            if(seat[r][c] == -1)
                extra++;
        }
        scanf("\n");
    }
    int right = 0, left = 0, cost[extra],costy = 0, cost1 = 0, cost2 = 0;
    for(r = 1;r <= row; r++)
    {
        for(c = 1; c <= column; c++)
        {
            if(seat[r][c] == -1)
            {
                for(right = c + 1; right <= column; right++)
                {
                    cost1+= snacky[seat[r][right]];
                }
                for(left = c - 1;left > 0; left--)
                {
                    cost2+= snacky[seat[r][left]];
                }
                if(cost1 > cost2)
                {
                    cost[costy] = cost2;
                }
                else
                {
                    cost[costy] = cost1;
                }
                costy ++;
            }
        }
    }
    bubble(cost, extra);
    printf("%d", cost[0]);
    return 0;
}

