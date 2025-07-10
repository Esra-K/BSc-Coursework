#include<stdio.h>

int x = 0 , y= 0;
void reversing(void)
{
    char a;
    scanf("%c",&a);
    if(a=='S')
        {
            printf("(%d, %d) ", x, y);
            return;
        }
    reversing();

    switch(a)
   {
       case 'R': x++;
       break;
       case 'L': x--;
              break;
       case 'U': y++;
              break;
       case 'D': y--;
          break;
       case '\n':
          return;
   }


   printf("-> (%d, %d) ", x, y);

}


int main()
{
   scanf("%d %d", &x, &y);
   reversing();
   return 0;
}
