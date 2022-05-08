#include <stdio.h>
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
	printf("%x %x %x\n",(void*)secret_function,string,&global);
	return 0;
}
