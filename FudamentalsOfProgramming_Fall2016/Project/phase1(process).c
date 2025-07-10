#include<stdio.h>
#include<string.h>
#include<stdlib.h>
void find_struct_size(char*, char*, char*);
void find_str_rec(char*, char*, char*);
void delete_garbage(char*);
struct NEWS{
    char* title;
    char* link;
    char* pubDate;
    char* description;
    char** category;
    int nCateg;
}*news;
int count=0;
int count1;
int j=0;
void find_struct_size(char* s,char* PATTERN1, char* PATTERN2)
{
    char *start, *end;
    if ( start = strstr( s, PATTERN1 ) )
    {
        start += strlen( PATTERN1 );
        if ( end = strstr( start, PATTERN2 ) )
        {
            count++;
            find_struct_size(end+strlen(PATTERN2), PATTERN1, PATTERN2);
        }
    }
}

void find_str_rec(char* s,char* PATTERN1, char* PATTERN2)
{

    char *target = NULL;
    char *start, *end;
    count=0;
    if( j == count1)
        return;
    if ( start = strstr( s, PATTERN1 ) )
    {
        start += strlen( PATTERN1 );
        if ( end = strstr( start, PATTERN2 ) )
        {
            target = (char*)malloc( end - start + 1 );
            memcpy( target, start, end - start );
            target[end - start] = '\0';
        }
    }
    if ( target )
    {
        char *start1, *end1;
        if(start1 = strstr(target,"<title>"))
        {
            start1 += strlen("<title>");
            if( end1 = strstr(start1, "</title>"))
            {
                news[j].title = (char*)malloc(end1 - start1 + 1);
                memcpy(news[j].title, start1, end1- start1);
                news[j].title[end1-start1]='\0';
            }
        }
        if(start1 = strstr(target,"<link>"))
        {
            start1 += strlen("<link>");
            if( end1 = strstr(start1, "</link>"))
            {
                news[j].link = (char*)malloc(end1 - start1 + 1);
                memcpy(news[j].link, start1, end1- start1);
                news[j].link[end1-start1]='\0';
            }
        }
        if(start1 = strstr(target,"<pubDate>"))
        {
            start1 += strlen("<pubDate>");
            if( end1 = strstr(start1, " +0000"))
            {
                news[j].pubDate = (char*)malloc(end1 - start1 + 1);
                memcpy(news[j].pubDate, start1, end1- start1);
                news[j].pubDate[end1-start1]='\0';
            }
        }
        if(start1 = strstr(target,"<description>"))
        {
            start1 += strlen("<description>");
            if( end1 = strstr(start1, "</description>"))
            {
                char* total_description = (char*)malloc(end1 - start1 -11);
                memcpy(total_description, start1+9, end1- start1-12);
                total_description[end1-start1-12]='\0';
                delete_garbage(total_description);
            }
        }
        find_struct_size(target, "<category>", "</category>");
        news[j].nCateg = count;
        news[j].category = (char**)calloc(count, sizeof(char*));
        int i;
        for(i=0; i<count; i++)
        {
            if(start1 = strstr(target,"<category>"))
            {
                start1 += strlen("<category>");
                if( end1 = strstr(start1, "</category>"))
                {
                    news[j].category[i] = (char*)malloc(end1 - start1 -11);
                    memcpy(news[j].category[i], start1+9, end1- start1-12);
                    news[j].category[i][end1-start1-12]='\0';
                }
            }
            target = end1 + 11;
        }
    }
    j++;
    find_str_rec(end+strlen(PATTERN2), PATTERN1, PATTERN2);
}
void delete_garbage(char* x)
{
    news[j].description = (char*)calloc(strlen(x), sizeof(char));
    int i=0, k=0;
    while(i<strlen(x)-1)
    {
        if(x[i] == '<')
        {
            i++;
            while(x[i] != '>')
                i++;
            i++;
        }
        else
        {
            while(x[i] != '<' && i != strlen(x)-1)
            {
                if(x[i] != '\n')
                {
                    news[j].description[k] = x[i];
                    k++;
                }
                i++;
            }
        }
    }
    news[j].description[k]=0;
}
