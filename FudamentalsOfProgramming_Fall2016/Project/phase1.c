#include <stdio.h>
#include<stdlib.h>
#include <curl/curl.h>
extern int count;
extern int count1;
extern int j;
#include "phase1(process).c"
void make_json_string(struct NEWS s, char* categ, char* jsonR)
{
    jsonR[0] = '{';
    strcat(jsonR, "\"title\"");
    strcat(jsonR, ": ");
    strcat(jsonR, "\"");
    strcat(jsonR, s.title);
    strcat(jsonR, "\"");
    strcat(jsonR, ",");
    strcat(jsonR, "\"date\"");
    strcat(jsonR, ": ");
    strcat(jsonR, "\"");
    strcat(jsonR,s.pubDate);
    strcat(jsonR, "\"");
    strcat(jsonR, ",");
    strcat(jsonR, "\"description\"");
    strcat(jsonR, ": ");
    strcat(jsonR, "\"");
    strcat(jsonR,s.description);
    strcat(jsonR, "\"");
    strcat(jsonR, ",");
    strcat(jsonR, "\"categorized\"");
    strcat(jsonR, ": ");
    strcat(jsonR, "true");
    strcat(jsonR, ",");
    strcat(jsonR, "\"categories\"");
    strcat(jsonR, ": ");
    strcat(jsonR, categ);
    strcat(jsonR, "}");
}

int main()
{
    CURL * myHandle;
    CURLcode result;
    myHandle = curl_easy_init ( ) ;
    curl_easy_setopt(myHandle, CURLOPT_URL, "http://team19:akrami17@www.fop-project.ir/news/get-urls");
    curl_easy_setopt(myHandle, CURLOPT_FOLLOWLOCATION, 1L);
    FILE *fp = fopen("URLfile.txt", "w");
    curl_easy_setopt(myHandle, CURLOPT_WRITEDATA, fp);
    result = curl_easy_perform( myHandle );
     if(result != CURLE_OK)
    {
        fprintf(stderr, "curl_easy_perform() failed :%sn",curl_easy_strerror(result));
    }
    curl_easy_cleanup(myHandle);
    fclose(fp);

  fp = fopen("URLfile.txt", "r");
  char** url;
  int i=0, nUrl=0, j1=0;
  int sizeOfText=0;
  char ch;
  while( ( ch = fgetc(fp) ) != EOF )
    {
        if(ch!='\0')
            sizeOfText++;
    }
  rewind(fp);
  char * txt = (char*) calloc(sizeOfText, sizeof(char*));
  while( (ch = fgetc(fp)) != EOF)
    {
        txt[i++] = ch;
    }
  txt[i] = 0;
  fclose(fp);
  i=0;
  int max_length=0, length=0;
  while(i<sizeOfText)
  {
      length=0;
      while(txt[i]!=' ' && i <= sizeOfText)
      {
          length++;
          i++;
      }
      if(txt[i]==' ')
      {
          nUrl++;
          i++;
      }
      if(length > max_length)
        max_length = length;
  }
  url = (char**)calloc(nUrl+1, sizeof(char*));
  for(i=0; i<nUrl+1; i++)
    url[i] = (char*)calloc(max_length+1, sizeof(char));
    i=0;
    int k=0;
    while(i<sizeOfText)
  {
      while(txt[i]!=' ' && i <= sizeOfText)
      {
          url[j1][k++]=txt[i];
          i++;
      }
      if(txt[i]==' ')
      {
          url[j1][k]=0;
          i++;
          j1++;
          k=0;
      }
  }
  for(i=0;i<=nUrl; i++)
  {
      url[i][4]= url[i][5];
      url[i][5]= url[i][6];
      url[i][6]= url[i][7];
      url[i][7]= '@';
  }
    CURL * Handle;
    CURLcode res;
    int r=0;
  char text[8];
  for(i=0; i<=nUrl;i++)
  {
    text[0] = 'u';
    text[1] = 'r';
    text[2] = 'l';
    text[3] = i + 'A';
    text[4] = '.' ;
    text[5] = 't' ;
    text[6] = 'x' ;
    text[7] = 't' ;
    text[8] = 0;

    Handle = curl_easy_init ( ) ;
    curl_easy_setopt(Handle, CURLOPT_URL, url[i]);
    curl_easy_setopt(Handle, CURLOPT_FOLLOWLOCATION, 1L);
    FILE *fp1 = fopen(text, "w");
    curl_easy_setopt(Handle, CURLOPT_WRITEDATA, fp1);
    res = curl_easy_perform( Handle );
     if(res != CURLE_OK)
    {
        fprintf(stderr, "curl_easy_perform() failed :%sn",curl_easy_strerror(result));
    }
    curl_easy_cleanup(Handle);
    fclose(fp1);

  fp1 = fopen(text, "r");
    int i1=0;
    int sizeOfText1=0;
    char ch1;
    count=0;
    while( ( ch1 = fgetc(fp1) ) != EOF )
    {
        if(ch1!='\0')
            sizeOfText1++;
    }
    rewind(fp1);
    char * txt1 = (char*) calloc(sizeOfText1, sizeof(char*));
    while( (ch1 = fgetc(fp1)) != EOF)
    {
        txt1[i1++] = ch1;
    }
    txt1[i1] = 0;
    find_struct_size(txt1, "<item>", "</item>");
    news = (struct NEWS*)calloc(count, sizeof(struct NEWS));
    count1= count;
    count=0;
    j=0;
    find_str_rec(txt1, "<item>", "</item>");

    int a = 0, b=0;
    for(a = 0; a < count1; a++)
{
    int j = 0;
    int len = 0;
    for(j = 0; j < news[a].nCateg; j++)
    {
        len+= (strlen(news[a].category[j]) + 3);
    }
    len+= 2;
    char* categ = calloc(len, 2);
    *(categ + 0) = '[';
    for(j = 0; j < news[a].nCateg; j++)
    {
        strcat(categ,"\"");
        strcat(categ,news[a].category[j]);
        strcat(categ,"\",");
    }
    *(categ + len - 2) = ']';
    *(categ + len - 1) = 0;
    //printf("%s\n",categ );
    char* jsonR = (char*)malloc(strlen(news[a].title)+strlen(news[a].pubDate)+strlen(news[a].description)+strlen(categ)+60);
    make_json_string(news[a], categ, jsonR);
    curl_global_init( CURL_GLOBAL_ALL );
    CURL * Handle1;
    CURLcode result1;
    Handle1 = curl_easy_init ( ) ;
    struct curl_slist *headers = NULL;
    headers = curl_slist_append(headers, "X-Requested-With: XMLHttpRequest");
    headers = curl_slist_append(headers, "Content-Type: application/json");
    headers = curl_slist_append(headers, "charsets: utf-8");
    curl_easy_setopt(Handle1, CURLOPT_HTTPHEADER, headers);
    curl_easy_setopt(Handle1, CURLOPT_URL, "http://team19:akrami17@www.fop-project.ir/news");
    curl_easy_setopt(Handle1, CURLOPT_POSTFIELDS,jsonR );
    result1 = curl_easy_perform(Handle1);
    curl_easy_cleanup(Handle1 );

}
}
  return 0;
}
