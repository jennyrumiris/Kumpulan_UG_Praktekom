[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/IWVzZS7F)
# **FOMO KONSER 2024**

Program ini bertujuan untuk menghitung total pengeluaran yang diperlukan untuk menonton konser berdasarkan **tipe tiket**, **lokasi konser**, dan **lama waktu menginap**. Program ini mempertimbangkan harga tiket konser, biaya transportasi sesuai lokasi, dan biaya tambahan penginapan jika menginap lebih dari 24 jam.

---

## **Petunjuk Penggunaan**

### **1. Parameter Fungsi: Tiket, Lokasi, WaktuPenginapan**

- **Tiket**: Menyimpan tipe tiket yang dipilih, yaitu:
  - **Tiket A** - Tipe terbaik (**350.000** IDR)
  - **Tiket B** - Fasilitas cukup (**270.000** IDR)
  - **Tiket C** - Cukup dekat dengan panggung (**150.000** IDR)

  Harga tiket ini akan digunakan dalam perhitungan total biaya.

- **Lokasi**: Menyimpan lokasi konser. Lokasi ini menentukan biaya transportasi dari Yogyakarta, yaitu:
  - **Jakarta**: **400.000** IDR
  - **Surabaya**: **360.000** IDR
  - **Bandung**: **390.000** IDR
  - **Yogyakarta**: **0** IDR (tidak memerlukan transportasi karena domisili)

- **WaktuPenginapan**: Menyimpan total waktu menginap dalam format jam. Berdasarkan waktu menginap:
  - Jika lebih dari 24 jam, penonton dikenakan biaya tambahan per jam sesuai kota penginapan.
  - Jika kurang dari 24 jam, penonton menerima refund biaya penginapan.
  - Jika tepat 24 jam, maka dikenakan biaya satu hari sesuai lokasi penginapan.

### **2. Biaya Penginapan Berdasarkan Lokasi**

Berikut adalah biaya penginapan per hari dan biaya tambahan per jam untuk masing-masing kota, jika menginap lebih dari 24 jam.

- **Jakarta**:
  - Biaya per hari: **250.000** IDR
  - Biaya tambahan per jam: **40.000** IDR

- **Bandung**:
  - Biaya per hari: **200.000** IDR
  - Biaya tambahan per jam: **30.000** IDR

- **Surabaya**:
  - Biaya per hari: **220.000** IDR
  - Biaya tambahan per jam: **35.000** IDR

- **Yogyakarta**:
  - Biaya per hari: **0** IDR
  - Biaya tambahan per jam: **0** IDR

---

## **Rumus Penghitungan Total Biaya**

Total biaya untuk menonton konser dihitung sebagai berikut:


- **Biaya Penginapan**:
  - Jika WaktuPenginapan < 24 jam: Biaya penginapan = 0 (refund).
  - Jika WaktuPenginapan = 24 jam: Biaya penginapan = Biaya harian lokasi tersebut.
  - Jika WaktuPenginapan > 24 jam: Biaya penginapan = Biaya harian + Biaya tambahan per jam untuk kelebihan waktu di lokasi.<br>
## Rumus
```
Total Biaya = Tiket Konser + Biaya Transportasi + Total Biaya Penginapan
```
