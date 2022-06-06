#include <stdio.h>
#include<stdlib.h>
#include <string.h>
#include <time.h>
#include <errno.h>
int global = 1000;

void secret_function(){
	printf("Shhhhh it's a secret !\n");
}
int main(int argc, char *argv[])
{
	char string[30]; 
	strcpy(string,"This is a string very cool.");
	int *array = malloc(5*sizeof(int));
	printf("%x %x %x %x\n",(unsigned int)secret_function,
		(unsigned int)string,(unsigned int)&global,(unsigned int)array);
	return 0;
}
