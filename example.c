#include<stdio.h>
#include<string.h>

void root_privilege(){
	printf("You gained root access.\n");
}
int main(void){

	char password[10];

	printf("Enter the password :\n");
	gets(password);
	
	if(strcmp("LOVEASLR",password) == 0)
		printf("Hi user !\n");
	else
		printf("Wrong password. Try again !\n");
}
