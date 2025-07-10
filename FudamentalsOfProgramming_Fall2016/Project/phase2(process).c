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
            start1 = strstr(start1, "A[");
            if( end1 = strstr(start1, "]]>"))
            {
                char* total_description = (char*)malloc(end1 - start1 -2);
                memcpy(total_description, start1+3, end1- start1-3);
                total_description[end1-start1-3]='\0';
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
                start1 = strstr (start1, "A[");
                if( end1 = strstr(start1, "</category>"))
                {
                    news[j].category[i] = (char*)malloc(end1 - start1 -9);
                    memcpy(news[j].category[i], start1+3, end1- start1-10);
                    news[j].category[i][end1-start1-10]='\0';
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
// int main()
//{
//    FILE* fp1;
//    fp1 = fopen ("urlA.txt", "r");
//    int i=0;
//    int sizeOfText=0;
//    char ch;
//    while( ( ch = fgetc(fp1) ) != EOF )
//    {
//        if(ch!='\0')
//            sizeOfText++;
//    }
//    rewind(fp1);
//    char * word;
//    char * txt = (char*) calloc(sizeOfText, sizeof(char*));
//    while( (ch = fgetc(fp1)) != EOF)
//    {
//        txt[i++] = ch;
//    }
//    txt[i] = 0;
//    find_struct_size(txt, "<item>", "</item>");
//    news = (struct NEWS*)calloc(count, sizeof(struct NEWS));
//    count1= count;
//    count=0;
//    find_str_rec(txt, "<item>", "</item>");
//    int m=0,n=0,len=0;
//    char* category;
//    for(m=0; m <count1; m++)
//    {
//        len=0;
//        for(n=0; n<news[m].nCateg; n++)
//        {
//            len += (strlen(news[m].category[n]) + 3);
//        }
//    //}
//   // printf("%d", len);
//    category = (char*)calloc((len+2), sizeof(char));
//    //for(m=0; m <count1; m++)
//
//    //{
//    //char* cat = calloc(len, sizeof(char));
//    *(category + 0) = '[';
//    for(n = 0; n < news[m].nCateg; n++)
//    {
//        strcat(category,"\"");
//        strcat(category,news[m].category[n]);
//        strcat(category,"\",");
//    }
//    *(category+len -3) = '"';
//    *(category + len - 2) = ']';
//    *(category + len - 1) = 0;
//    //for(n=0; n<len; n++)
//    printf("%s\n", category);
//    }
//
//    //}
////    FILE * file= fopen("output.txt", "wb");
////    fwrite(news,sizeof(struct NEWS),count1, file);
////    fclose(file);
////    struct NEWS *s = malloc(count1 * sizeof(struct NEWS));
////    file= fopen("output.txt", "rb");
////    if (file != NULL)
////    {
////    fread(s,sizeof(struct NEWS),count1, file);
////    }
// //   int w=0;
////    for(i=0; i<count1; i++)
////    {
////        for(w=0; w<news[i].nCateg; w++)
////            {
////                printf("%s\n\n", news[i].category[w]);
////            }
////    }
//
//   free(news);
//}
