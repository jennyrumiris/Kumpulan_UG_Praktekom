//b. modifikasi program diatas agar jumlah tingkatan piramida dapat di-inputkan melalui prompt input. 
// #include <stdio.h>

// int main(void) {
//     int banyak;
//     //input dari pengguna
//     printf("Masukkan Berapa Tingginya: ");
//     scanf("%d", &banyak);
//     //Perulangan untuk setiap baris piramida
//     for(int j = 0; j < banyak; j++) {
//         //Perulangan untuk mencetak spasi
//         for(int i = 0; i < banyak - j - 1; i++) {
//             printf(" ");
//         }
//         // Perulangan untuk mencetak (#)
//         for(int k = 0; k <= j; k++) {
//             printf("#");
//         }
//         // Pindah ke baris berikutnya
//         printf("\n");
//     }
// }