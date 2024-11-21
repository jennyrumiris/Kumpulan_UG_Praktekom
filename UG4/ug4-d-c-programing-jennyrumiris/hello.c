#include <stdio.h>

int main(void){
    char NamaDepan[100];
    printf("Siapakah Namamu ? ");
    scanf("%[^\n]", NamaDepan);
    printf("Hello %s\n", NamaDepan);
    return 0;
}