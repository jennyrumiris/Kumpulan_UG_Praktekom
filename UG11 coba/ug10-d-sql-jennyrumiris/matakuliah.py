import sqlite3

# Fungsi untuk membuat tabel matakuliah jika belum ada
def create_table():
    connection = sqlite3.connect("matakuliah.db")
    cursor = connection.cursor()

    # Membuat tabel matakuliah
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matakuliah (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kode TEXT NOT NULL,
            nama TEXT NOT NULL,
            sks INTEGER NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

# Fungsi untuk menambahkan matakuliah baru
def tambah_matakuliah(kode, nama, sks):
    connection = ###
    cursor = ###
  
    # Menambahkan matakuliah baru
    # Perintah SQL untuk menambahkan matakuliah baru

    connection.###
    connection.###
  
# Fungsi untuk menampilkan semua matakuliah
def tampilkan_semua_matakuliah():
    connection = ###
    cursor = ###

    # Menampilkan semua matakuliah
    # Perintah SQL untuk menampilkan matakuliah
    rows = cursor.fetchall()

    for ###
        print###

    connection.###

# Fungsi untuk mengupdate data matakuliah
def update_matakuliah(kode, new_nama, new_sks):
    connection = ###
    cursor = ###

    # Mengupdate data matakuliah berdasarkan kode
    # Perintah SQL untuk updated data matakuliah

    connection.###
    connection.###

# Fungsi untuk menghapus matakuliah berdasarkan kode
def hapus_matakuliah(kode):
    connection = ###
    cursor = ###

    # Menghapus matakuliah berdasarkan kode
    # Perintah SQL untuk menghapus data matakuliah

    connection.###
    connection.###

# Membuat tabel jika belum ada
create_table()

# Menambahkan beberapa matakuliah
tambah_matakuliah()

# Menampilkan semua matakuliah
print("Daftar Mata Kuliah:")
tampilkan_semua_matakuliah()

# Mengupdate data matakuliah
update_matakuliah()

# Menampilkan semua matakuliah setelah diupdate
print("\nDaftar Mata Kuliah setelah Update:")
tampilkan_semua_matakuliah()

# Menghapus matakuliah berdasarkan kode
hapus_matakuliah()

# Menampilkan semua matakuliah setelah dihapus
print("\nDaftar Mata Kuliah setelah Hapus:")
tampilkan_semua_matakuliah()

