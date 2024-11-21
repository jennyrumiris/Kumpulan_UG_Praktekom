#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//semangat😁😁
// Bagian ini yang harus kalian ubah

enum gender{
    Laki_laki, 
    Perempuan
};

typedef struct{
    // Isi dengan data :
    int NIM;                // nim adalah int
    char nama[50];           // nama adalah character
    char kampus[50];         // kampus adalah character
    char prodi[50];          // prodi adalah character
    int semester;            // semester adalah int
    enum gender jenisKelamin;     // Gender adalah Enum 
}InfoMahasiswa;

//fungsi isi data mahasiswa
void main(){
    struct InfoMahasiswa *mahasiswa = malloc(sizeof(InfoMahasiswa)*100);
    //isi dengan data kalian.
    mahasiswa -> NIM = 71220886;
    strcpy(mahasiswa->nama, "Jenny Rumiris Marpaung");
    strcpy(mahasiswa->kampus, "Universitas Kristen Duta Wacana");
    strcpy(mahasiswa->prodi, "Teknologi infoematika");
    mahasiswa -> semester = 5;
    mahasiswa -> kelamin = Perempuan; 

    printf("NIM             : %i\n", mahasiswa -> NIM);
    printf("Nama            : %s\n", mahasiswa -> nama);
    printf("Jenis Kelamin   : %s\n", mahasiswa -> kelamin == Perempuan ? "Laki-laki":"Perempuan");
    printf("Kampus          : %s\n", mahasiswa -> kampus);
    printf("Prodi           : %s\n", mahasiswa -> prodi);
    printf("Semester        : %i\n", mahasiswa -> semester);

    free(mahasiswa);
}