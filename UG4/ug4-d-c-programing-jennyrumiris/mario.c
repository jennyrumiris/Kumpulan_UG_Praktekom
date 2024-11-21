// //a. Dalam file bernama mario.c, buatlah program dalam C yang menggambar sebuah piramida menggunakan karakter hash(#).
#include <stdio.h>

int main(void) {
    // Tinggi piramida
    int tinggi = 8;
    //Perulangan
    for (int i = 1; i <= tinggi; i++) {
        // Perulangan untuk setiap pencetkan spasi
        for (int j = 1; j <= tinggi - i; j++) {
            printf(" ");
        }
        //Perulangan untuk mencetak (#)
        for (int k = 1; k <= i; k++) {
            printf("#");
        }
        // Pindah ke baris berikutnya
        printf("\n");
    }
}




// //b. modifikasi program diatas agar jumlah tingkatan piramida dapat di-inputkan melalui prompt input.
#include <stdio.h>

int main(void) {
    int banyak;
    //inputan dari pengguna untuk banyak pagar
    printf("Masukkan Berapa Tingginya: ");
    scanf("%d", &banyak);
    //Perulangan untuk setiap baris piramida
    for(int a = 0; a < banyak; a++) {
        //Perulangan untuk mencetak spasi
        for(int b = 0; b < banyak - a - 1; b++) {
            printf(" ");
        }
        // Perulangan untuk mencetak (#)
        for(int c = 0; c <= a; c++) {
            printf("#");
        }
        // Pindah ke baris berikutnya
        printf("\n");
    }
}


#include <stdio.h>

int main(void) {
    int banyak;
    printf("Masukkan Berapa Tingginya: ");
    scanf("%d", &banyak);
    
    for(int a = banyak; a > 0; a--) {
        for(int b = 0; b <= banyak - a; b++) {
            printf(" ");
        }
        for(int c = 0; c <= a; c++) {
            printf("#");
        }
        printf("\n");
    }

    return 0;
}
