from flask import Flask, redirect, render_template, request, url_for
import sqlite3

app = Flask(__name__)

@app.route('/success/<thenim>', methods=['GET'] )
def success(thenim):
    return 'Proses data Mahasiswa NIM: %s berhasil' % thenim

@app.route("/insertmhs", methods=['POST'])  
def insertmahasiswa():
    return insertmahasiswa

@app.route("/updatemhs", methods=['POST'])  
def updatemahasiswa():
    return updateMahasiswa

@app.route("/deletemhs", methods=['POST'])  
def deletemahasiswa():
    return deleteMahasiswa

@app.route('/mhslist')
def userList():
    mhses = getAllMahasiswa()
    return render_template('mhslist.html', title='Daftar Mahasiswa', listmhs=mhses)

def insertMahasiswa(nim, nama, tempat_lahir, tanggal_lahir, alamat):
    input("nim", nim)
    input("nama", nama)
    input("tempat lahir", tempat_lahir)
    input("tanggal lahir", tanggal_lahir)
    input("alamat", alamat)

    

def updateMahasiswa(nim, nama, tempat_lahir, tanggal_lahir, alamat):
    input("nim", nim)
    input("nama", nama)
    input("tempat lahir", tempat_lahir)
    input("tanggal lahir", tanggal_lahir)
    input("alamat", alamat)

def deleteMahasiswa(nim):
    nim 
    return deleteMahasiswa
 
  
def getAllMahasiswa():
    # Open database connection
    connection = sqlite3.connect("mhs.db")
    cursor = connection.cursor()
    # Execute the query
    cursor.execute("SELECT nim, nama, tempat_lahir, tanggal_lahir, alamat FROM mahasiswa;")    

    # convert it into dictionary
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
    # Close the connection
    connection.close()
    return data

if __name__ == '__main__':
    app.run()

