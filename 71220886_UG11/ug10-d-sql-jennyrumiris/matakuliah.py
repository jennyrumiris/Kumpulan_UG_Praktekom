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
    connection = sqlite3.connect("matakuliah.db")
    cursor = connection.cursor()
  
    # Menambahkan matakuliah baru
    cursor.execute('INSERT INTO matakuliah (kode, nama, sks) VALUES (?, ?, ?);',(kode, nama, sks))

    connection.commit()
    connection.close()
  
# Fungsi untuk menampilkan semua matakuliah
def tampilkan_semua_matakuliah():
    connection = sqlite3.connect("matakuliah.db")
    cursor = connection.cursor()

    # Menampilkan semua matakuliah
    cursor.execute('SELECT * FROM matakuliah')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()

# Fungsi untuk mengupdate data matakuliah
def update_matakuliah(kode, new_nama, new_sks):
    connection = sqlite3.connect("matakuliah.db")
    cursor = connection.cursor()

    # Mengupdate data matakuliah berdasarkan kode
    cursor.execute('UPDATE matakuliah SET nama = ?, sks = ? WHERE kode = ?', (new_nama, new_sks, kode))

    connection.commit()
    connection.close()

# Fungsi untuk menghapus matakuliah berdasarkan kode
def hapus_matakuliah(kode):
    connection = sqlite3.connect("matakuliah.db")
    cursor = connection.cursor()

    # Menghapus matakuliah berdasarkan kode
    cursor.execute('DELETE FROM matakuliah WHERE kode = ?', (kode,))

    connection.commit()
    connection.close()

# Membuat tabel jika belum ada
create_table()

# Menambahkan beberapa matakuliah
tambah_matakuliah('MK001', 'Matematika Teknik', 3)
tambah_matakuliah('MK002', 'Teknologi Komputer', 3)
tambah_matakuliah('MK003', 'Logika Matematika', 3)

# Menampilkan semua matakuliah
print("Daftar Mata Kuliah:")
tampilkan_semua_matakuliah()

# Mengupdate data matakuliah
update_matakuliah('MK002', 'Teknologi Komputasi', 4)

# Menampilkan semua matakuliah setelah diupdate
print("\nDaftar Mata Kuliah setelah Update:")
tampilkan_semua_matakuliah()

# Menghapus matakuliah berdasarkan kode
hapus_matakuliah('MK003')

# Menampilkan semua matakuliah setelah dihapus
print("\nDaftar Mata Kuliah setelah Hapus:")
tampilkan_semua_matakuliah()