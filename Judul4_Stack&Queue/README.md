# Tugas Akhir Percobaan 4

## Judul Program

**Sistem Antrian Laundry Menggunakan Queue**

---

## Deskripsi Singkat

Program ini dibuat untuk menerapkan struktur data **Queue** pada contoh yang dekat dengan kegiatan sehari-hari, yaitu antrian laundry. Pada tempat laundry, pakaian pelanggan biasanya diproses berdasarkan urutan kedatangan. Pelanggan yang datang lebih dulu akan diproses lebih dulu.

Karena itu, struktur data **Queue** cocok dipakai pada program ini. Queue menggunakan prinsip **First In First Out (FIFO)**, yaitu data yang pertama masuk akan menjadi data pertama yang keluar atau diproses.

Contoh sederhananya:

```text
Andi - 3 kg - Cuci Setrika
Budi - 2 kg - Cuci
Sinta - 4 kg - Setrika
```

Dari contoh tersebut, data milik Andi akan diproses terlebih dahulu karena masuk paling awal ke dalam antrian.

---

## Source Code

> Tambahkan screenshot source code di bagian ini setelah file di-upload ke GitHub.

```html
<img width="1320" height="2337" alt="Queue Antrian Laundry" src="LINK_GAMBAR_SOURCE_CODE" />
```

---

## Penjelasan Kode Per Baris

### 1. Bagian awal program

```python
# Program Implementasi Queue
```
Baris ini hanya komentar untuk memberi tahu bahwa program yang dibuat memakai konsep Queue.

```python
# Tema: Sistem Antrian Laundry
```
Baris ini menjelaskan tema program, yaitu antrian laundry.

```python
# Base code: Percobaan IV-2 QueueArray
```
Baris ini menjelaskan bahwa program dikembangkan dari konsep QueueArray pada Percobaan IV.

---

### 2. Membuat class QueueArray

```python
class QueueArray:
```
Baris ini membuat class bernama `QueueArray`. Class ini dipakai sebagai tempat untuk menyimpan operasi-operasi Queue.

```python
def __init__(self, max_size=20):
```
Baris ini adalah constructor. Bagian ini akan berjalan otomatis saat objek Queue dibuat. Nilai `max_size=20` berarti kapasitas awal antrian adalah 20 data.

```python
self.MAXN = max_size
```
Baris ini menyimpan nilai kapasitas maksimum Queue ke dalam variabel `MAXN`.

```python
self.q = [None] * self.MAXN
```
Baris ini membuat list kosong berukuran 20. Nilai awalnya diisi `None` karena belum ada data pelanggan yang masuk.

```python
self.front_idx = -1
```
Baris ini membuat penanda posisi depan antrian. Nilai `-1` berarti antrian masih kosong.

```python
self.rear_idx = -1
```
Baris ini membuat penanda posisi belakang antrian. Nilai awalnya juga `-1` karena belum ada data yang masuk.

---

### 3. Mengecek apakah antrian kosong

```python
def is_empty(self):
```
Baris ini membuat method untuk mengecek apakah Queue kosong atau tidak.

```python
return self.front_idx == -1
```
Jika `front_idx` bernilai `-1`, berarti belum ada pelanggan dalam antrian. Hasilnya akan bernilai `True`.

---

### 4. Mengecek apakah antrian penuh

```python
def is_full(self):
```
Baris ini membuat method untuk mengecek apakah Queue sudah penuh.

```python
return (self.rear_idx + 1) % self.MAXN == self.front_idx
```
Baris ini memakai rumus circular queue. Jika posisi setelah `rear_idx` sama dengan `front_idx`, berarti antrian sudah penuh.

---

### 5. Menambahkan data ke antrian dengan enqueue

```python
def enqueue(self, x):
```
Baris ini membuat method `enqueue()`. Fungsinya untuk menambahkan data pelanggan ke bagian belakang antrian.

```python
if self.is_full():
```
Baris ini mengecek dulu apakah antrian sudah penuh.

```python
print("Antrian laundry penuh")
```
Jika antrian penuh, program menampilkan pesan bahwa antrian tidak bisa ditambah lagi.

```python
return False
```
Baris ini mengembalikan nilai `False` untuk menandakan data gagal masuk ke antrian.

```python
if self.is_empty():
```
Baris ini mengecek apakah antrian masih kosong.

```python
self.front_idx = 0
self.rear_idx = 0
```
Jika antrian masih kosong, maka data pertama akan disimpan di indeks 0. Karena datanya baru satu, posisi depan dan belakang sama-sama berada di indeks 0.

```python
else:
```
Bagian ini dijalankan kalau antrian sudah berisi data.

```python
self.rear_idx = (self.rear_idx + 1) % self.MAXN
```
Baris ini menggeser posisi belakang ke indeks berikutnya. Operator `%` dipakai supaya indeks bisa kembali ke awal jika sudah sampai ujung list.

```python
self.q[self.rear_idx] = x
```
Baris ini memasukkan data pelanggan ke posisi belakang Queue.

```python
return True
```
Baris ini menandakan bahwa data berhasil masuk ke antrian.

---

### 6. Menghapus data dari antrian dengan dequeue

```python
def dequeue(self):
```
Baris ini membuat method `dequeue()`. Fungsinya untuk mengambil dan menghapus data paling depan dari antrian.

```python
if self.is_empty():
```
Baris ini mengecek apakah antrian kosong.

```python
print("Antrian laundry kosong")
```
Jika antrian kosong, program menampilkan pesan bahwa tidak ada laundry yang bisa diproses.

```python
return None
```
Baris ini mengembalikan `None` karena tidak ada data yang dikeluarkan.

```python
data = self.q[self.front_idx]
```
Baris ini mengambil data yang berada di posisi paling depan antrian.

```python
self.q[self.front_idx] = None
```
Setelah data diambil, posisi tersebut dikosongkan kembali.

```python
if self.front_idx == self.rear_idx:
```
Baris ini mengecek apakah data yang baru saja diambil adalah satu-satunya data dalam antrian.

```python
self.front_idx = -1
self.rear_idx = -1
```
Jika data tersebut adalah satu-satunya data, maka antrian dikembalikan ke kondisi kosong.

```python
else:
```
Bagian ini berjalan kalau setelah data depan dihapus masih ada data lain di dalam Queue.

```python
self.front_idx = (self.front_idx + 1) % self.MAXN
```
Baris ini menggeser posisi depan ke data berikutnya.

```python
return data
```
Baris ini mengembalikan data pelanggan yang sedang diproses.

---

### 7. Melihat data paling depan dengan peek

```python
def peek(self):
```
Baris ini membuat method `peek()`. Fungsinya untuk melihat data paling depan tanpa menghapusnya.

```python
if self.is_empty():
```
Baris ini mengecek apakah antrian kosong.

```python
return None
```
Jika kosong, tidak ada data yang bisa dilihat, jadi fungsi mengembalikan `None`.

```python
return self.q[self.front_idx]
```
Jika tidak kosong, program mengembalikan data yang berada di posisi paling depan.

---

### 8. Menampilkan semua antrian

```python
def display(self):
```
Baris ini membuat method `display()` untuk menampilkan semua data dalam antrian.

```python
if self.is_empty():
```
Baris ini mengecek apakah antrian kosong.

```python
print("Antrian laundry kosong")
return
```
Jika kosong, program menampilkan pesan lalu menghentikan method `display()`.

```python
print("Daftar antrian laundry dari depan ke belakang:")
```
Baris ini menampilkan judul daftar antrian.

```python
i = self.front_idx
```
Variabel `i` dimulai dari posisi depan antrian.

```python
nomor = 1
```
Variabel `nomor` dipakai untuk menampilkan nomor urut saat daftar antrian dicetak.

```python
while True:
```
Perulangan ini dipakai untuk menampilkan semua data dari depan sampai belakang.

```python
print(f"{nomor}. {self.q[i]}")
```
Baris ini mencetak nomor urut dan data pelanggan.

```python
if i == self.rear_idx:
    break
```
Jika posisi `i` sudah sampai di data paling belakang, perulangan dihentikan.

```python
i = (i + 1) % self.MAXN
```
Baris ini memindahkan indeks ke data berikutnya.

```python
nomor += 1
```
Baris ini menaikkan nomor urut tampilan.

---

### 9. Input data laundry

```python
def input_laundry():
```
Baris ini membuat fungsi khusus untuk memasukkan data laundry.

```python
nama = input("Masukkan nama pelanggan: ")
```
Baris ini meminta nama pelanggan.

```python
while True:
```
Perulangan ini dipakai agar input berat laundry terus diminta sampai datanya benar.

```python
try:
```
Bagian ini dipakai untuk mencoba menjalankan input angka.

```python
berat = float(input("Masukkan berat laundry (kg): "))
```
Baris ini meminta berat laundry. Tipe datanya `float` karena berat laundry bisa berupa angka desimal, misalnya 2.5 kg.

```python
if berat <= 0:
```
Baris ini mengecek apakah berat laundry bernilai nol atau negatif.

```python
print("Berat laundry harus lebih dari 0 kg.")
continue
```
Jika berat tidak valid, program menampilkan pesan dan meminta input ulang.

```python
break
```
Jika input berat sudah benar, perulangan dihentikan.

```python
except ValueError:
```
Bagian ini menangani kesalahan jika pengguna memasukkan huruf atau teks pada input berat.

```python
print("Input berat harus berupa angka!")
```
Pesan ini muncul jika input berat bukan angka.

```python
jenis_layanan = input("Masukkan jenis layanan (Cuci / Setrika / Cuci Setrika): ")
```
Baris ini meminta jenis layanan laundry.

```python
return f"{nama} - {berat} kg - {jenis_layanan}"
```
Baris ini menggabungkan nama, berat, dan jenis layanan menjadi satu data.

---

### 10. Fungsi utama program

```python
def main():
```
Baris ini membuat fungsi utama program.

```python
antrian_laundry = QueueArray()
```
Baris ini membuat objek Queue untuk menyimpan data antrian laundry.

```python
pilihan = 0
```
Variabel ini dipakai untuk menyimpan pilihan menu dari pengguna.

```python
while pilihan != 5:
```
Selama pengguna belum memilih menu 5, program akan terus menampilkan menu.

```python
print("\n=== Sistem Antrian Laundry ===")
```
Baris ini menampilkan judul program.

```python
print("1. Tambah pelanggan ke antrian")
print("2. Proses laundry paling depan")
print("3. Lihat pelanggan berikutnya")
print("4. Tampilkan semua antrian")
print("5. Keluar")
```
Baris-baris ini menampilkan pilihan menu yang bisa dipilih pengguna.

```python
pilihan = int(input("Pilih menu: "))
```
Baris ini meminta pengguna memilih menu, lalu mengubah input menjadi integer.

```python
except ValueError:
```
Bagian ini menangani input menu jika pengguna memasukkan selain angka.

```python
if pilihan == 1:
```
Jika pengguna memilih menu 1, program akan menambahkan data pelanggan ke antrian.

```python
data_laundry = input_laundry()
```
Program memanggil fungsi `input_laundry()` untuk mengambil data pelanggan.

```python
if antrian_laundry.enqueue(data_laundry):
```
Data pelanggan dimasukkan ke Queue menggunakan `enqueue()`.

```python
elif pilihan == 2:
```
Jika pengguna memilih menu 2, program memproses laundry paling depan.

```python
data_laundry = antrian_laundry.dequeue()
```
Program mengambil data paling depan menggunakan `dequeue()`.

```python
elif pilihan == 3:
```
Jika pengguna memilih menu 3, program melihat pelanggan berikutnya.

```python
data_laundry = antrian_laundry.peek()
```
Program mengambil data paling depan dengan `peek()`, tetapi data tidak dihapus.

```python
elif pilihan == 4:
```
Jika pengguna memilih menu 4, program menampilkan semua antrian.

```python
antrian_laundry.display()
```
Baris ini memanggil method `display()`.

```python
elif pilihan == 5:
```
Jika pengguna memilih menu 5, program akan berhenti.

```python
if __name__ == "__main__":
    main()
```
Baris ini membuat fungsi `main()` langsung dijalankan ketika file Python dieksekusi.

---

## Output Program dan Penjelasan Per Baris

> Tambahkan screenshot output program di bagian ini setelah program dijalankan.

```html
<img width="790" height="226" alt="Output Queue Antrian Laundry" src="LINK_GAMBAR_OUTPUT" />
```

### Contoh Output 1: Menambah Data Laundry

```text
=== Sistem Antrian Laundry ===
1. Tambah pelanggan ke antrian
2. Proses laundry paling depan
3. Lihat pelanggan berikutnya
4. Tampilkan semua antrian
5. Keluar
Pilih menu: 1
Masukkan nama pelanggan: Andi
Masukkan berat laundry (kg): 3
Masukkan jenis layanan (Cuci / Setrika / Cuci Setrika): Cuci Setrika
Data laundry berhasil masuk ke antrian.
```

Penjelasan per baris:

```text
=== Sistem Antrian Laundry ===
```
Baris ini adalah judul program yang muncul saat menu ditampilkan.

```text
1. Tambah pelanggan ke antrian
```
Menu ini dipakai untuk menambahkan data laundry baru ke antrian.

```text
2. Proses laundry paling depan
```
Menu ini dipakai untuk memproses data laundry yang berada paling depan.

```text
3. Lihat pelanggan berikutnya
```
Menu ini dipakai untuk melihat data pelanggan paling depan tanpa menghapusnya.

```text
4. Tampilkan semua antrian
```
Menu ini dipakai untuk menampilkan semua data laundry yang sedang mengantre.

```text
5. Keluar
```
Menu ini dipakai untuk mengakhiri program.

```text
Pilih menu: 1
```
Pengguna memilih menu 1, berarti ingin memasukkan data laundry baru.

```text
Masukkan nama pelanggan: Andi
```
Pengguna memasukkan nama pelanggan, yaitu Andi.

```text
Masukkan berat laundry (kg): 3
```
Pengguna memasukkan berat laundry sebesar 3 kg.

```text
Masukkan jenis layanan (Cuci / Setrika / Cuci Setrika): Cuci Setrika
```
Pengguna memilih jenis layanan Cuci Setrika.

```text
Data laundry berhasil masuk ke antrian.
```
Data Andi berhasil masuk ke Queue menggunakan operasi `enqueue()`.

---

### Contoh Output 2: Menampilkan Semua Antrian

```text
Pilih menu: 4
Daftar antrian laundry dari depan ke belakang:
1. Andi - 3.0 kg - Cuci Setrika
2. Budi - 2.0 kg - Cuci
```

Penjelasan per baris:

```text
Pilih menu: 4
```
Pengguna memilih menu 4 untuk menampilkan semua antrian laundry.

```text
Daftar antrian laundry dari depan ke belakang:
```
Program memberi keterangan bahwa data ditampilkan dari posisi paling depan sampai paling belakang.

```text
1. Andi - 3.0 kg - Cuci Setrika
```
Data Andi berada pada urutan pertama, jadi Andi akan diproses lebih dulu.

```text
2. Budi - 2.0 kg - Cuci
```
Data Budi berada pada urutan kedua, jadi Budi diproses setelah Andi.

---

### Contoh Output 3: Memproses Laundry

```text
Pilih menu: 2
Data laundry sedang diproses: Andi - 3.0 kg - Cuci Setrika
```

Penjelasan per baris:

```text
Pilih menu: 2
```
Pengguna memilih menu 2 untuk memproses data paling depan.

```text
Data laundry sedang diproses: Andi - 3.0 kg - Cuci Setrika
```
Data Andi keluar dari antrian menggunakan `dequeue()`. Ini sesuai prinsip FIFO, karena Andi masuk lebih dulu dan diproses lebih dulu.

---

### Contoh Output 4: Input Tidak Valid

```text
Pilih menu: dua
Input tidak valid, silakan masukkan angka!
```

Penjelasan per baris:

```text
Pilih menu: dua
```
Pengguna memasukkan teks, padahal pilihan menu harus berupa angka.

```text
Input tidak valid, silakan masukkan angka!
```
Program menampilkan pesan error karena input tidak bisa diubah menjadi integer.

Contoh lain:

```text
Masukkan berat laundry (kg): -1
Berat laundry harus lebih dari 0 kg.
```

Penjelasan per baris:

```text
Masukkan berat laundry (kg): -1
```
Pengguna memasukkan angka `-1` sebagai berat laundry.

```text
Berat laundry harus lebih dari 0 kg.
```
Program menolak input tersebut karena berat laundry tidak boleh nol atau negatif.

---

## Link YouTube

[Masukkan link YouTube di sini setelah video di-upload]
