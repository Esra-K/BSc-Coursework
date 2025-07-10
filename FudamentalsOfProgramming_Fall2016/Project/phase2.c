#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include <curl/curl.h>
#include<math.h>
#include<time.h>
extern int count;
extern int count1;
extern int j;
#include "phase2(process).c"
#include "trie.c"
typedef struct categnode
{
    char *name;
    int numenews;
    node** khabar;
}categnode;
categnode* Categories;
int numk[7]= {0,0,0,0,0,0,0};
node* trieOfImp;
void funcM(char* kalameh)
{
    int ka=0, tedad=0, koll=0, m1=0,sum=0;
    int tekrar[7];
    int rate[2][7];
    double nesbat1[7], nesbat2[7];
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
    float enherafM1=0, enherafM2=0, enherafM3=0;
    for(ka = 0; ka < 7; ka++)
    {
        nesbat1[ka] = (float)rate[0][ka] / Categories[ka].numenews;
        nesbat2[ka] = (float)rate[0][ka] / sum;
        enherafM1 += nesbat1[ka];
        enherafM2 += nesbat2[ka];
    }
    enherafM1 /=7;
    enherafM2 /=7;
    for(ka=0; ka<7; ka++)
    {
        //printf("%.5f %.6f\t%.5f %.6f\n", nesbat1[ka],fabs(enherafM1 - nesbat1[ka]),nesbat2[ka],fabs(enherafM2 - nesbat2[ka]));
        if(fabs(enherafM2 - nesbat2[ka])> 0.44 && fabs(enherafM1 - nesbat1[ka])> 0.0065)
        {
            addNode(kalameh, strlen(kalameh), trieOfImp);
            //printf("%s %d\n%.4f  %.5f\t %.4f  %.5f\n", kalameh, ka+1, nesbat1[trieI], fabs(enherafM1 - nesbat1[trieI]), nesbat2[trieI], fabs(enherafM2 - nesbat2[trieI]));
            numk[ka]++;
        }
    }
}
void findSubtree(struct node *subtree, char* word, int level)
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

int main()
{
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
  char text[8];
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
    find_str_rec(txt1, "<item>", "</item>");
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
        int cnt=0, size=0, currentN[7]={0,0,0,0,0,0,0};
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
        }
        int ka = 0, koll = 0, tedad = 0, sum = 0, sum2 = 0;
        int tekrar[7];
        int rate[2][7];
        double nesbat1[7], nesbat2[7];
        char* buf = (char*)calloc(100,sizeof(char));
        trieOfImp = newNode();
        findSubtree(KoleMatn,buf, 0);
        return 0;
}

