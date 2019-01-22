#include<stdio.h>
int main() {
	char a[200000] = { 0 };
	FILE *fp;
	fp = fopen("a.txt", "r");
	if (fp == NULL) {
		return 0;
	}
	fread(a, 1, sizeof(a), fp);
	printf("%s", a);
	system("Pause");
}
