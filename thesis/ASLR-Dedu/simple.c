
int aFunction(){
	char c = 'c';
	char b = 'b';
	
	b = c;
	
	return (int) b;
}
int main(){
	int a=2,b=3,c;
	aFunction();
	c = a+b;
}
