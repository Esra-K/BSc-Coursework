#include<stdio.h>
#include<string.h>
int main()
{
    char b[1200];
    int K = 0;
    while(b[K - 1] != 10)
    {
        scanf("%c", &b[K]);
        K++;
    }
    b[K] = NULL;

    //printf("%s", b);
    char a[1200];
    int J = 0;
    for(K = 0; K < strlen(b); K++)
    {
        if(b[K] == '8')
        {
            if(b[K + 1] == NULL)
            {
                a[J] = 'a';
                J++;
                a[J] = 't';
                J++;
                a[J] = 'e';
                J++;
            }
            else if(b[K - 1] == ' ' || K == 0)
            {
                a[J] = 'b';
                J++;
            }
            else if(b[K + 1] != ' ' && b[K - 1] != ' ' && K < strlen(b) - 2 )
            {
              a[J] = 'o';
              J++;
              a[J] = 'o';
              J++;
            }
            else //if(b[K + 1] == ' ')
            {
                a[J] = 'a';
                J++;
                a[J] = 't';
                J++;
                a[J] = 'e';
                J++;
            }

        }
        else
        {
            a[J] = b[K];
            J++;
        }
    }
    a[J] = NULL;
    //printf("%s", a);
    for(J = 0; J < strlen(a); J++)
    {
        if(a[J] == 'l')
        a[J] = '1';

        if(a[J] == 'g')
        a[J] = '9';

        if(a[J] == 'r')
        a[J] = '7';

        if(a[J] == 'z')
        a[J] = '2';
    }


    // edame
    char asghar[1200];
    int k = 0;

    while(asghar[k-1] != 10)
    {
        scanf("%c", &asghar[k] );
        k++;
    }
    asghar[k] = NULL;
    int cnt = 0;
    for(cnt = 0; cnt < strlen(asghar); cnt++)
    {
        if(asghar[cnt] == '1')
        asghar[cnt] = 'l';

        if(asghar[cnt] == '9')
        asghar[cnt] = 'g';

        if(asghar[cnt] == '7')
        asghar[cnt] = 'r';

        if(asghar[cnt] == '2')
        asghar[cnt] = 'z';
    }
    int i = 0, j = 0;
    int num = strlen(asghar);
    char behrooz[num];
    for(i = 0; i < num; i++)
    {
        if(asghar[i] == 'a' && asghar[i + 1] == 't' && asghar[i + 2] == 'e' && (asghar[i + 3] == ' ' || asghar[i + 3] == NULL))
        {
            behrooz[j] = '8';
            j++;
            behrooz[j] = ' ';
            j++;

            i+= 3;
        }
        else if((asghar[i-1] == ' ' || i == 0) && asghar[i ] == 'b')
        {
            behrooz[j] = '8';
            j++;

        }
        else if((asghar[i - 1] != ' '&& i !=0 ) && asghar[i] == 'o' && asghar[i + 1] == 'o' && asghar[i + 2] != ' ' && i < strlen(asghar) - 3)
           {
            behrooz[j] = '8';
            j++;
            i+= 1;
           }
        else
        {
            behrooz[j] = asghar[i];
            j++;
        }

    }
    behrooz[j] = NULL;
    printf("%s", a);
    printf("%s", behrooz);
    return 0;
}

