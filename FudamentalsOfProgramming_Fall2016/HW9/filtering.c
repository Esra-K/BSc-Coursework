#include<stdio.h>
#include<string.h>
#include<stdbool.h>
int main()
{
    int n = 5;
    //printf("adad yadet nare");
    scanf("%d", &n);
    char c;
    while((c= getchar()) != '\n' && c != EOF)
            /* discard */ ;
    char name[100000];// = "is let the skyfall when is crumblescrumble at at skyfall at  skyfall is where we start skyfall h gh";

    //printf("hi there");
    gets(name);
    //puts(name);
    //printf("%d", n);
    int n2 = 0;
    scanf("%d", &n2);
    int a[n2];
    int d = 0;
    for(d = 0; d < n2; d++)
    {
        char wrd[50];
        scanf("%s", &wrd);
        int i = 0, j = 0, cnt = 0;
        bool flag = 1;
        for(i = 0; i < strlen(name); i++)
        {
            //int k = i + strlen(wrd);
            if((name[i - 1] == 32 || i == 0) && (name[i + strlen(wrd)] == 32 || i + strlen(wrd) >= strlen(name)))
            {
                for(j = 0; j < strlen(wrd); j++)
            {
                if(name[i] != wrd[j])
                {
                    flag = 0;
                    break;
                }
                i++;
            }
            if(flag == 1)
            {
                cnt++;
            }
            flag = 1;
            }
        }
       // printf("%d", cnt);
       a[d] = cnt;
    }
     for(d = 0; d < n2; d++)
        printf("%d\n", a[d]);
//char buffer[900];
//   fgets(buffer, 900, stdin);
//   printf("%s" , buffer);
    return 0;
}
