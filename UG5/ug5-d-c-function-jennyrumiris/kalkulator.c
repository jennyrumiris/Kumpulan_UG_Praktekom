#include <stdio.h>

int main() 
{
    char operator;
    int a, b;
    float c, d, result;

    printf("================================\n");
    printf("     KALKULATOR SEDERHANA       \n");
    printf("================================\n");
    printf("== PILIH OPERATOR == \n");
    printf("(+, -, *, /) : ");
    scanf("%c", &operator);

    switch (operator) {
        case '+':
            printf("\n 1. Penjumlahan \n");
            printf("Masukkan Nilai yang Pertama = ");
            scanf("%i", &a);
            printf("Masukkan Nilai yang Kedua = ");
            scanf("%i", &b);
            result = a + b;
            printf("----------------------------------- = \n");
            printf("Result =\t\t\t %g\n", result);
            break;
        case '-':
            printf("\n 1. Pengurangan \n");
            printf("Masukkan Nilai yang Pertama = ");
            scanf("%i", &a);
            printf("Masukkan Nilai yang Kedua = ");
            scanf("%i", &b);
            result = a - b;
            printf("----------------------------------- = \n");
            printf("Result =\t\t\t %g\n", result);
            break;
        case '*':
            printf("\n 1. Perkalian \n");
            printf("Masukkan Nilai yang Pertama = ");
            scanf("%i", &a);
            printf("Masukkan Nilai yang Kedua = ");
            scanf("%i", &b);
            result = a * b;
            printf("----------------------------------- = \n");
            printf("Result =\t\t\t %g\n", result);
            break;
        case '/':
            printf("\n 1. Pembagian \n");
            printf("Masukkan Nilai yang Pertama = ");
            scanf("%f", &c);
            printf("Masukkan Nilai yang Kedua = ");
            scanf("%f", &d);
            if(d != 0){
                result = c / d;
                printf("----------------------------------- = \n");
                printf("Result =\t\t\t %g\n", result);
            }else{
                printf("Error: Tidak dapat melakukan pembagian dengan niali 0.\n");
            }
            break;
        default:
            printf("Operator Salah.\n");
            return 1; 
        }
        return 0;
}