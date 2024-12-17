#include <stdio.h>

void main(void){
    int a, c, baris;
    printf("masukan jumlah baris:");
    scanf("%d", & baris);
    for (a = 1; a <= baris ; ++a) {
        for (c = 1 ; c <= a ; ++c) {
            printf("#");
        }
        printf("\n");
    }
    return 0;  
}