#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include <curl/curl.h>
#include<math.h>
#include "cJSON.c"
extern int count;
extern int count1;
extern int j;
#include "phase3(process).c"
typedef struct categnode
{
    char *name;
    int numenews;
    node** khabar;
}categnode;
categnode* Categories;
node* trieOfImp;
int numk[7]= {0,0,0,0,0,0,0};
int keywords = 0, keyN=0;
double*** vector;
double *IDF;
node* eKhabarP3;
double* vectorK3;
FILE* fp3;
void funcM(char* kalameh)//mohasebeyeh had ha ,mohasebeye ekheraf az miangin
{
    int ka=0, tedad=0, koll=0, m1=0,sum=0;
    int tekrar[7];
    int rate[2][7];
    double nesbat1[7], nesbat2[7];
    int trieI=0;
    for(ka = 0; ka < 7; ka++)
    {
        tedad =0;
        koll=0;
        for(m1 = 0; m1 < Categories[ka].numenews; m1++)
        {
            if(findNode(kalameh, strlen(kalameh),Categories[ka].khabar[m1]))
                {
                    tedad++;
                    koll+= findNode(kalameh, strlen(kalameh),Categories[ka].khabar[m1]);
                }
        }
        tekrar[ka] = koll;
        rate[0][ka] = tedad;
        rate[1][ka] = Categories[ka].numenews - rate[0][ka];
        sum+= tedad;
    }
    double enherafM1=0, enherafM2=0, enherafM3=0;
    for(ka = 0; ka < 7; ka++)
    {
        nesbat1[ka] = (double)rate[0][ka] / Categories[ka].numenews;
        nesbat2[ka] = (double)rate[0][ka] / sum;
        enherafM1 += nesbat1[ka];
        enherafM2 += nesbat2[ka];
    }
    enherafM1 /=7;
    enherafM2 /=7;
    for(ka=0; ka<7; ka++)
    {
        if(fabs(enherafM2 - nesbat2[ka])> 0.44 && fabs(enherafM1 - nesbat1[ka])> 0.0065)
        {
            if(!findNode(kalameh, strlen(kalameh), trieOfImp))
                keywords++;
            addNode(kalameh, strlen(kalameh), trieOfImp);
            numk[ka]++;
        }
    }
}
void findSubtree(struct node *subtree, char* word, int level)//yaftane kole kalamate phase2
{
    int i=0;
    if (subtree == NULL)
    {
        return;
    }
    if (subtree->value)
    {
        word[level] = 0;

        funcM(word);
    }
    for (i = 0; i<26;i++)
    {
        if (subtree->child[i]!= NULL) {
            word[level] = 'a' + i;
            findSubtree( subtree->child[i], word, level+1);
        }
    }
}
double findIDF(char* kalameh)//yaftaneh DF
{
    int i=0, j=0;
    double counter=0;
    for(i=0; i<7; i++)
    {
        for(j=0; j<Categories[i].numenews; j++)
        {
            if(findNode(kalameh, strlen(kalameh), Categories[i].khabar[j]))
            {
                counter++;
            }
        }
    }
    return counter;
}
void MakeVector(char* kalameh)//sakhte bordar barayeh khabarha
{
    int i=0,j=0, TF=0;
    IDF[keyN] = log10((double)count1 / findIDF(kalameh));
    for(i=0; i<7; i++)
    {
        for(j=0; j<Categories[i].numenews; j++)
        {
            TF = (double)findNode(kalameh, strlen(kalameh), Categories[i].khabar[j]);//mohasebeyeh TF[i][j][keyN]
            vector[i][j][keyN] = (double)TF * IDF[keyN];
        }
    }
    keyN++;
}
void findSubtree1(struct node *r, char* word, int l)// peymayeshe kalamate mohem
{
    int i=0;
    if (r == NULL)
    {
        return;
    }
    if (r->value)
    {
        word[l] = 0;
        MakeVector(word);
    }
    for (i = 0; i<26;i++)
    {
        if (r->child[i]!= NULL) {
            word[l] = 'a' + i;
            findSubtree1( r->child[i], word, l+1);
        }
    }
}
void MakeVectorK3(char* kalameh)//sakhte bordar barayeh magholat
{
    double TF = 0.0;
    TF = (double)findNode(kalameh, strlen(kalameh), eKhabarP3);
    vectorK3[keyN] = (double)TF * IDF[keyN];
    keyN++;
}
void findSubtree2(struct node *r, char* word, int l)//peymayeshe kalamate mohem
{
    int i=0;
    if (r == NULL)
    {
        return;
    }
    if (r->value)
    {
        word[l] = 0;
        MakeVectorK3(word);
    }
    for (i = 0; i<26;i++)
    {
        if (r->child[i]!= NULL) {
            word[l] = 'a' + i;
            findSubtree2( r->child[i], word, l+1);
        }
    }
}
double AndazehVec(double* vec)//yaftane andazeh bordar ha
{
    int i=0;
    double andazeh=0;
    for(i=0; i<keywords; i++)
    {
        andazeh += pow(vec[i], 2);
    }
    return sqrt(andazeh);
}
void make_json_string(struct NEWS s, char* jsonR)
{
    strcat(jsonR, "{");
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
    strcat(jsonR, "false");
    strcat(jsonR, ",");
    strcat(jsonR, "\"categories\"");
    strcat(jsonR, ": ");
    strcat(jsonR, "[\"");
    strcat(jsonR, s.category[0]);
    strcat(jsonR, "\"]");
    strcat(jsonR, "}");
    strcat(jsonR, "\0");
}


int main()
{
    //freopen("output.txt","w",stdout);
    CURL * myHandle;
    CURLcode result;
    myHandle = curl_easy_init ( ) ;
    curl_easy_setopt(myHandle, CURLOPT_URL, "http://team19:akrami17@www.fop-project.ir/news/get-urls/?phase=2");
    curl_easy_setopt(myHandle, CURLOPT_FOLLOWLOCATION, 1L);
    FILE *fp = fopen("URLfile.txt", "w");
    curl_easy_setopt(myHandle, CURLOPT_WRITEDATA, fp);
    result = curl_easy_perform( myHandle );
     if(result != CURLE_OK)
    {
        fprintf(stderr, "curl_easy_perform() failed :%sn",curl_easy_strerror(result));
    }
    curl_easy_cleanup(myHandle);
    fclose(fp); //// darkhast be adrese phase 2

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
    int k=1;
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
          k=1;
      }
  }
  int p=0;
  for(i=0;i<=nUrl; i++)
  {
    for(p=0;p<7;p++)
        url[i][p]=url[i][p+1];
    url[i][7]= '@';
  }
    CURL * Handle;
    CURLcode res;
    int r=0;
    FILE *fp1 ;
    char text[8]; // /// joda kardaneh har URL
  for(i=0; i<=nUrl;i++)
  {
    strcpy(text,"urla.txt");
    Handle = curl_easy_init ( ) ;
    curl_easy_setopt(Handle, CURLOPT_URL, url[i]);
    curl_easy_setopt(Handle, CURLOPT_FOLLOWLOCATION, 1L);
    fp1 = fopen(text, "a");
    curl_easy_setopt(Handle, CURLOPT_WRITEDATA, fp1);
    res = curl_easy_perform( Handle );
     if(res != CURLE_OK)
    {
        fprintf(stderr, "curl_easy_perform() failed :%sn",curl_easy_strerror(result));
    }
    curl_easy_cleanup(Handle);
    fclose(fp1);
  }
    fp1 = fopen("urla.txt", "r");
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
    find_str_rec(txt1, "<item>", "</item>"); ///// joda kardaneh Title , link o ina
    node* KoleMatn = newNode();
    Categories = (categnode*)calloc(7,sizeof(categnode));
        Categories[0].name = "business";
        Categories[1].name = "entertainment";
        Categories[2].name = "health";
        Categories[3].name = "world";
        Categories[4].name = "us";
        Categories[5].name = "sport";
        Categories[6].name = "sci_tech";
        for(i=0; i<count1; i++)
        {
            for(j=0; j<7; j++)
            {
                if(strcmp(news[i].category[0], Categories[j].name)== 0)
                {
                    Categories[j].numenews++;
                }
            }
        }
        for(i=0; i<7; i++)
        {
            Categories[i].khabar = (node**)calloc(Categories[i].numenews,sizeof(node*));
            for(j=0; j<Categories[i].numenews; j++)
            {
                Categories[i].khabar[j] = newNode();
            }
        }
        char* matn;
        char* kalameh;
        char** wbyw;
        int cnt=0, size=0, currentN[7]={0,0,0,0,0,0,0}; //// sakteh chiz hyeh morede niaz(alocating!!)
        for(i=0; i<count1; i++)
        {
            for(j=0; j<7; j++)
            {
                if(strcmp(news[i].category[0], Categories[j].name)== 0)
                {
                    break;
                }
            }
                if(j ==7)
                    continue;
                matn =(char*)calloc(strlen(news[i].title)+ strlen(news[i].description) +2, sizeof(char));
                strcpy(matn, news[i].title);
                strcat(matn , " ");
                strcat(matn, news[i].description);
                kalameh = (char*)calloc(strlen(matn), sizeof(matn));
                int counter = 0;
                for(cnt=0; cnt<strlen(matn); cnt++)
                {
                    if(matn[cnt]>='a' && matn[cnt]<='z')
                    {
                        kalameh[size++] = matn[cnt];
                    }
                    else if (matn[cnt]>='A' && matn[cnt]<= 'Z')
                        kalameh[size++] = matn[cnt]+32;
                    else if( (size !=0) && (matn[cnt] == ' ' || matn[cnt] == '\n' || matn[cnt] == '\t'))
                    {
                        kalameh[size]=0;

                        addNode(kalameh, size, Categories[j].khabar[currentN[j]]);
                        addNode(kalameh, size, KoleMatn);

                        kalameh = (char*)calloc(strlen(matn), sizeof(matn));
                        size =0 ;
                    }
                }
                currentN[j]++;
        } ///// joda kardane matn har khabar dar phase 2 , sakhte derakht barayeh har khabar
        char* buf = (char*)calloc(100,sizeof(char));
        trieOfImp = newNode();
        findSubtree(KoleMatn,buf, 0);
        char* buf1 = (char*)calloc(100,sizeof(char));
        vector = (double***)calloc(7, sizeof(double**));
        for(i=0; i<7; i++)
        {
            vector[i] = (double**)calloc(Categories[i].numenews, sizeof(double*));
            for(j=0; j<Categories[i].numenews; j++)
            {
                vector[i][j] = (double*)calloc(keywords, sizeof(double));
            }
        }
        IDF = (double*)calloc(keywords, sizeof(double));
        findSubtree1(trieOfImp, buf1, 0);
        double *vectorCat[7];
        for(i=0; i<7; i++)
            vectorCat[i] = (double*)calloc(keywords, sizeof(double));
        for(keyN=0; keyN<keywords; keyN++)
        {
            for(i=0; i<7; i++)
            {
                for(j=0; j<Categories[i].numenews; j++)
                {
                    vectorCat[i][keyN] += vector[i][j][keyN];
                }
            }
        } // sakhte vectore barayeh category
        double andazehOf_cat[7]={0,0,0,0,0,0,0};
        for(i=0; i<7; i++)
        {
            andazehOf_cat[i]= AndazehVec(vectorCat[i]);
        }
///////////////////phase 33333
    myHandle = curl_easy_init ( ) ;
    curl_easy_setopt(myHandle, CURLOPT_URL, "http://team19:akrami17@www.fop-project.ir/news/get-urls/?phase=3");
    curl_easy_setopt(myHandle, CURLOPT_FOLLOWLOCATION, 1L);
    fp = fopen("URLfile1.txt", "w");
    curl_easy_setopt(myHandle, CURLOPT_WRITEDATA, fp);
    result = curl_easy_perform( myHandle );
     if(result != CURLE_OK)
    {
        fprintf(stderr, "curl_easy_perform() failed :%sn",curl_easy_strerror(result));
    }
    curl_easy_cleanup(myHandle);
    fclose(fp);

  fp = fopen("URLfile1.txt", "r");
  i=0, nUrl=0, j1=0;
  sizeOfText=0;
  while( ( ch = fgetc(fp) ) != EOF )
    {
        if(ch!='\0')
            sizeOfText++;
    }
  rewind(fp);
  txt = (char*) calloc(sizeOfText, sizeof(char*));
  while( (ch = fgetc(fp)) != EOF)
    {
        txt[i++] = ch;
    }
  txt[i] = 0;
  fclose(fp);
  i=0;
  max_length=0, length=0;
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
    k=1;
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
          k=1;
      }
  }
  p=0;
  for(i=0;i<=nUrl; i++)
  {
    for(p=0;p<7;p++)
        url[i][p]=url[i][p+1];
    url[i][7]= '@';
  }
    Handle;
    res;
    r=0;
    fp1 ;
    text[8];
  for(i=0; i<=nUrl;i++)
  {
    strcpy(text,"urlb.txt");
    Handle = curl_easy_init ( ) ;
    curl_easy_setopt(Handle, CURLOPT_URL, url[i]);
    curl_easy_setopt(Handle, CURLOPT_FOLLOWLOCATION, 1L);
    fp1 = fopen(text, "a");
    curl_easy_setopt(Handle, CURLOPT_WRITEDATA, fp1);
    res = curl_easy_perform( Handle );
     if(res != CURLE_OK)
    {
        fprintf(stderr, "curl_easy_perform() failed :%sn",curl_easy_strerror(result));
    }
    curl_easy_cleanup(Handle);
    fclose(fp1);
  }
    fp1 = fopen("urlb.txt", "r");
    i1=0;
    sizeOfText1=0;
    count=0;
    while( ( ch1 = fgetc(fp1) ) != EOF )
    {
        if(ch1!='\0')
            sizeOfText1++;
    }
    rewind(fp1);
    txt1 = (char*) calloc(sizeOfText1, sizeof(char*));
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
    double andazeh=0;
    double max=0.0;
    int tmp=0;
    int shomar = 0;
    for(i=0; i<count1; i++)
    {
        double zarbD[7] = {0, 0, 0, 0, 0, 0, 0};
        vectorK3 = (double*)calloc(keywords, sizeof(double));
        eKhabarP3=newNode();
        matn = (char*)calloc(strlen(news[i].title)+strlen(news[i].description)+2, sizeof(char));
        strcpy(matn, news[i].title);
        strcat(matn, " ");
        strcat(matn, news[i].description);
        matn[strlen(news[i].title)+strlen(news[i].description)+1]=0;
        kalameh = (char*)calloc(strlen(matn), sizeof(char));
        size=0; /////// chasbondaneh matn khabar ha:)
        for(cnt=0; cnt<strlen(matn);cnt++)
        {
            if(matn[cnt]>='a' && matn[cnt]<='z')
                kalameh[size++] = matn[cnt];
            else if(matn[cnt]>='A' && matn[cnt]<='Z')
                kalameh[size++] = matn[cnt]+32;
            else if((size !=0) && (matn[cnt] == ' ' || matn[cnt] == '\n' || matn[cnt] == '\t'))
            {
                kalameh[size]=0;
                addNode(kalameh, size, eKhabarP3);
                size=0;
                kalameh = (char*)calloc(strlen(matn), sizeof(char));
            }
        } ///// add kardan kalameh be trie
        keyN=0;
        char* buf2=(char*)calloc(100, sizeof(char));
        findSubtree2(trieOfImp, buf2, 0);
        andazeh = AndazehVec(vectorK3);
        max = 0.0;
        tmp = 0;
        double result=0;
        for(cnt = 0; cnt < 7; cnt++)
        {
            result=0;
            for(shomar = 0; shomar < keywords; shomar++)
            {
                result += vectorK3[shomar]*(vectorCat[cnt][shomar]);

            }
            zarbD[cnt]=result;
            zarbD[cnt] /= ((andazeh) * (andazehOf_cat[cnt]));
            if(zarbD[cnt] >= max)
            {
                max = zarbD[cnt];
                tmp = cnt;
            }
        }
        news[i].category[0] = (char*)calloc(strlen(Categories[tmp].name),sizeof(char));
        strcpy(news[i].category[0], Categories[tmp].name);
        int d=0, W_s=0;
        char* des = (char*)calloc(strlen(news[i].description), sizeof(char));
        while(news[i].description[d]=='\n'|| news[i].description[d]=='\t' || news[i].description[d]==' ')
        {
            W_s++;
            d++;
        }
        strcpy(des,news[i].description+k);
        int W_s1=0;
        d = strlen(des)-1;
        while(des[d]=='\n'|| des[d]=='\t' || des[d]==' ')
        {
            W_s1++;
            d--;
        }
        des[strlen(des)- W_s1]= 0 ;
        strcpy(news[i].description,des);
        cJSON *root;
    cJSON *fmt;
    root = cJSON_CreateObject();
    cJSON_AddItemToObject(root, "title", cJSON_CreateString(news[i].title));
    cJSON_AddItemToObject(root, "date", cJSON_CreateString(news[i].pubDate));
    cJSON_AddItemToObject(root, "description", cJSON_CreateString(news[i].description));
    cJSON_AddItemToObject(root, "categorized", cJSON_CreateFalse());
    cJSON_AddItemToObject(root, "categories",cJSON_CreateStringArray(news[i].category,1));
        char *out;
        out = cJSON_Print(root);
        cJSON_Delete(root);
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
    curl_easy_setopt(Handle1, CURLOPT_POSTFIELDS,out );
    result1 = curl_easy_perform(Handle1);
    curl_easy_cleanup(Handle1 );

    }
        return 0;
}
