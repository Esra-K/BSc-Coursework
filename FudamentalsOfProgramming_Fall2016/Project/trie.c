#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct node
{
	int value;
	struct node *child[26];
}node;

node *newNode();
void addNode(char *word, int length, node* root);
//node *root;

//node* start()
//{
//	root = newNode();
//	return root;
//}

node *newNode()
{
	int i;
	node *ret = calloc(1, sizeof(node));
	for(i = 0; i < 26; i++)
		ret->child[i] = NULL;
	ret->value = 0;
	return ret;
}

void addNode(char *word, int length, node* root)
{
	int i;
	node *current = root;
	for(i = 0; i < length; i++)
	{
		int tmp = (int)(word[i] - 'a');
		if(current->child[tmp] == NULL)
			current->child[tmp] = newNode();
		current = current->child[tmp];
	}
	current->value++;
	return;
}

int findNode(char *word, int length, node* root)
{
	int i;
	node *current = root;
	for(i = 0; i < length; i++)
	{
		int tmp = (int)(word[i] - 'a');
		if(current->child[tmp] == NULL)
			return 0;
		current = current->child[tmp];
	}
	return current->value;
}


//int main()
//{
//    int n, m, i;
//    char* word = (char*)malloc(100*sizeof(char));
//    scanf("%d", &n);
//    node* root = newNode();
//    for(i=0; i<n; i++)
//    {
//        scanf("%s", word);
//        addNode(word, strlen(word), root);
//    }
//    scanf("%d", &m);
//    for(i=0; i<m; i++)
//    {
//        scanf("%s", word);
//        printf("%d\n", findNode(word, strlen(word), root));
//    }
//	return 0;
//}
