[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_IVQC5CB)
# Langkah-langkah Penyelesaian: Struktur Data Mahasiswa

### 1. *Gunakan typedef untuk mendefinisikan struct InfoMahasiswa.*
   - Lengkapi atribut InfoMahasiswa sesuai kebutuhan, seperti:
     - NIM
     - Nama
     - Prodi
     - Semester
     - Kampus
     - Jenis Kelamin

### 2. *Enum Gender*
   - Enum gender menentukan jenis kelamin dengan dua opsi:
     - Laki_laki
     - Perempuan
   - Dalam kode, Anda bisa menyimpan informasi ini dalam atribut Gender di InfoMahasiswa.

### 3. *Fungsi Isi Data Mahasiswa*
   - Buat fungsi isiDataMahasiswa untuk mengisi data ke dalam struct InfoMahasiswa.
   - Fungsi ini menerima pointer ke InfoMahasiswa dan beberapa parameter tambahan seperti:
     - NIM
     - Nama
     - Prodi
     - Kampus
     - Semester
     - Gender
   - Gunakan strcpy untuk menyalin data string seperti Nama, Prodi, dan Kampus ke dalam struct.

### 4. *Fungsi Tampilkan Data Mahasiswa*
   - Buat fungsi tampilkanDataMahasiswa untuk menampilkan data mahasiswa.
   - Fungsi ini menerima pointer ke InfoMahasiswa dan mencetak data sesuai format yang diinginkan.
   - Gunakan operator ternary untuk menampilkan Jenis Kelamin berdasarkan nilai yang ada dalam enum gender.

### 5. *Alokasi Memori dan Pembebasan Memori*
   - Di dalam main, alokasikan memori untuk variabel mahasiswa menggunakan malloc.
   - Setelah penggunaan, bebaskan memori menggunakan free untuk menghindari kebocoran memori.

### 6. *Modularisasi dan Kerapihan Kode*
   - Pecah kode menjadi fungsi terpisah untuk pengisian data (isiDataMahasiswa) dan penampilan data (tampilkanDataMahasiswa) agar kode lebih modular dan mudah dipahami.
   - Tambahkan komentar untuk memperjelas bagian-bagian penting.

### 7. *Contoh Penggunaan di Main*
   - Pada main, deklarasikan beberapa objek InfoMahasiswa dan gunakan fungsi isiDataMahasiswa untuk mengisi data masing-masing mahasiswa.
   - Tampilkan data menggunakan tampilkanDataMahasiswa untuk melihat hasilnya.



## Contoh Output
```
NIM             : 123456789
Nama            : Nama Kalian
Jenis Kelamin   : Laki-laki
Kampus          : Universitas Contoh
Prodi           : Teknik Informatika
Semester        : 5
```