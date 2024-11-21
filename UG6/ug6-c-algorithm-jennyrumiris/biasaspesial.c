#include <stdio.h>

int main() {

    int angka;
    
    printf("Masukkan Bilangan Bulat Positif : ");
    scanf("%i", &angka);
    if (angka <= 0) {
        printf("Bilangan Harus Positf\n");
        return 1;
    }
    if (angka % 11 == 0) {
        printf("BILANGAN SPESIAL\n");
    } else {
        printf("BILANGAN BIASA\n");
    }
    return 0;
}