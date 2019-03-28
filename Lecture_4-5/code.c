#include<stdio.h>

int main(){
	if (fork()) printf("True");
	else printf("False");

	return 0;
}
