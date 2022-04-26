
int aFunction(){
	char c = 'c';
	char b = 'b';
	
	b = c;
	
	return (int) b;
}
int main(){
	int a=2,b=3,c;
	aFunction();
	
	for(int i =0;i<10;i++){
		c = i*(a+b);
		if(c > 10)
			goto label;
	}
label:
	aFunction();
	return 0;
}
