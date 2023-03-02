#include<stdio.h>
int main(void){
    int a = 3465, b = 1323, i=0; int temp;
    printf("loop       a    b\n");
    while (b != 0) { 
        printf("%4d    ",i);
        temp = a%b; a = b; b = temp;
        printf("%4d %4d\n",a,b); 
        i++;
        }
        printf("GCD=%d",a);
    return 0;
    }



