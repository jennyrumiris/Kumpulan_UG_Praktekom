from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/mhslist')
def mhslist():
    with sqlite3.connect("mahasiswa.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT nim, nama, tempat_lahir, tanggal_lahir, alamat FROM mahasiswa")
        data = cursor.fetchall()  # Data harus berbentuk list of tuples
        print(data)  # Debugging: cek data di terminal

    return render_template('index.html', data=data)

# Halaman daftar mahasiswa
@app.route('/mhslist')
def another_mhslist():
    with sqlite3.connect("mahasiswa.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT nim, nama, tempat_lahir, tanggal_lahir, alamat FROM mahasiswa")
        data = cursor.fetchall()  # Ambil semua data dari tabel mahasiswa

    return render_template('index.html', data=data)

# Halaman tambah mahasiswa
@app.route('/add', methods=['GET', 'POST'])
def add_mahasiswa():
    if request.method == 'POST':
        nim = request.form['nim']
        nama = request.form['nama']
        tempat_lahir = request.form['tempat_lahir']
        tanggal_lahir = request.form['tanggal_lahir']
        alamat = request.form['alamat']

        with sqlite3.connect("mahasiswa.db") as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO mahasiswa (nim, nama, tempat_lahir, tanggal_lahir, alamat)
                    VALUES (?, ?, ?, ?, ?)
                """, (nim, nama, tempat_lahir, tanggal_lahir, alamat))
                conn.commit()
            except sqlite3.IntegrityError:
                return "Error: NIM sudah terdaftar!", 400

        return redirect(url_for('mhslist'))
    return render_template('insert.html')

# Halaman update mahasiswa
@app.route('/update/<nim>', methods=['GET', 'POST'])
def update_mahasiswa(nim):
    if request.method == 'POST':
        nama = request.form['nama']
        tempat_lahir = request.form['tempat_lahir']
        tanggal_lahir = request.form['tanggal_lahir']
        alamat = request.form['alamat']

        with sqlite3.connect("mahasiswa.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE mahasiswa
                SET nama = ?, tempat_lahir = ?, tanggal_lahir = ?, alamat = ?
                WHERE nim = ?
            """, (nama, tempat_lahir, tanggal_lahir, alamat, nim))
            conn.commit()

        return redirect(url_for('mhslist'))

    # Ambil data mahasiswa berdasarkan NIM
    with sqlite3.connect("mahasiswa.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mahasiswa WHERE nim = ?", (nim,))
        data = cursor.fetchone()

    if not data:
        return "Mahasiswa tidak ditemukan!", 404

    return render_template('update.html', mahasiswa=data)

@app.route('/delete_mahasiswa', methods=['GET', 'POST'])
def delete_mahasiswa():
    if request.method == 'POST':
        nim = request.form['nim']  # Ambil NIM dari input formulir
        conn = sqlite3.connect('mahasiswa.db')
        cursor = conn.cursor()
        try:
            # Hapus data mahasiswa berdasarkan NIM
            cursor.execute("DELETE FROM mahasiswa WHERE nim = ?", (nim,))
            conn.commit()
            print(f"Data dengan NIM {nim} berhasil dihapus.")
        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            conn.close()
        # Redirect ke halaman daftar mahasiswa
        return redirect(url_for('mhslist'))
    return render_template('delete.html')


if __name__ == '__main__':
    app.run(debug=True)
