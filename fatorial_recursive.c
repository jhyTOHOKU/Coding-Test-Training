#include<stdio.h>
int fact(int n){
    if (n==0) return 1;
    else return n*fact(n-1);
}

int main(void){
    int n;
    printf("factorial of what?:");
    scanf("%d",&n);
    printf("%d!=%d",n,fact(n));
    return 0;
}