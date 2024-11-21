#include <stdio.h>

int main() {
    int a, b, c;

    // Meminta input tiga bilangan dari pengguna
    printf("Masukkan tiga bilangan (a, b, c): ");
    scanf("%d %d %d", &a, &b, &c);

    // Mengecek apakah dua atau lebih digit paling kanan sama
    if (a % 10 == b % 10 || a % 10 == c % 10 || b % 10 == c % 10) {
        printf("SAMA\n");
    } else {
        printf("TIDAK SAMA\n");
    }

    return 0;
}
 