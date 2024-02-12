# Tucil1_13522054

PROGRAM CYBERPUNK 2077 BREACH PROTOCOL SOLVER

DESKRIPSI
Program ini terinspirasi dari game https://cyberpunk-hacker.com/
Ada 4 komponen penting pada game ini:
1. Token – terdiri dari dua karakter alfanumerik seperti E9, BD, dan 55.
2. Matriks – terdiri atas token-token yang akan dipilih untuk menyusun urutan kode.
3. Sekuens – sebuah rangkaian token (dua atau lebih) yang harus dicocokkan.
4. Buffer – kumpulan token yang dapat disusun secara sekuensial.
Pada program ini, setiap sekuens memiliki bonus. 
Untuk mendapatkan bonus, sekuens harus terdapat pada buffer.
Program ini akan mencari solusi buffer yang memiliki bonus terbanyak dan ukuran terpendek (terkecil).
Buffer adalah kumpulan token yang diambil dari matriks dengan mekanisme berikut:
1. Token pertama akan diambil dari baris teratas matriks
2. Token selanjutnya akan diambil dari token yang berada di atas atau di bawah token sebelumnya
3. Token selanjutnya akan diambil dari token yang berada di kanan atau di kiri token sebelumnya
4. Proses 2 dan 3 akan diulangi sampai buffer optimal atau penuh

REQUIREMENT
- python
- pip
- pyinstaller

CARA KOMPILASI (jika perlu, sudah ada file .exe di bin)
1. Buka Command Prompt
2. Pindah ke directory tempat cyber.py berada
3. Masukkan command 
    pyinstaller --onefile cyber.py
4. File executable akan berada di folder dist

CARA MENJALAN PROGRAM
1. Buka file executable pada folder bin atau folder hasil kompilasi.
2. Pilih metode input.
3. Jika input menggunakan file (.txt), masukkan nama path file dengan lengkap.
4. Jika input menggunakan CLI, masukkan data sesuai format yang ada di CLI. 
5. Pilih apakah solusi ingin disimpan atau tidak.
6. Tekan enter untuk keluar.

IDENTITAS PEMBUAT
Nama: Benjamin Sihombing
NIM: 13522054
Kelas: K02
