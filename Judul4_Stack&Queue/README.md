# Tugas Akhir Percobaan 4

## Judul Program

**Sistem Antrian Laundry Menggunakan Queue**

---

## Deskripsi Singkat

Program ini dibuat untuk menerapkan struktur data **Queue** pada sistem antrian laundry. Dalam kasus ini, data pelanggan yang datang lebih dulu akan masuk ke antrian lebih dulu dan diproses lebih dulu.

Program menggunakan konsep **First In First Out (FIFO)**. Artinya, data yang pertama masuk ke dalam queue akan menjadi data pertama yang keluar saat diproses.

Contoh data yang digunakan pada output program adalah:

```text
Nabil - 3.0 kg
Raffi - 2.5 kg
Fathir - 4.0 kg
```

Karena Nabil masuk pertama, maka data Nabil akan berada di bagian depan antrian dan diproses lebih dulu.

---

## Source Code

> Tambahkan screenshot source code di bagian ini setelah file di-upload ke GitHub.

```html
<img width="1320" height="2337" alt="Queue Antrian Laundry" src="LINK_GAMBAR_SOURCE_CODE" />
```

---

## Penjelasan Kode Per Baris

### 1. Membuat Class QueueArray

```python
class QueueArray:
```

Baris ini membuat class bernama `QueueArray`. Class ini digunakan untuk membuat struktur data queue.

```python
def __init__(self, max_size=100):
```

Baris ini adalah constructor. Bagian ini akan otomatis dijalankan ketika objek queue dibuat. Nilai `max_size=100` berarti kapasitas maksimal antrian adalah 100 data.

```python
self.MAXN = max_size
```

Baris ini menyimpan nilai kapasitas maksimal queue ke dalam variabel `MAXN`.

```python
self.q = [None] * self.MAXN
```

Baris ini membuat list kosong dengan ukuran sesuai `MAXN`. Isi awalnya adalah `None` karena belum ada data laundry yang masuk.

```python
self.front_idx = -1
```

Baris ini membuat penanda posisi depan queue. Nilai awal `-1` menunjukkan bahwa antrian masih kosong.

```python
self.rear_idx = -1
```

Baris ini membuat penanda posisi belakang queue. Nilai awalnya juga `-1` karena belum ada data yang masuk.

---

### 2. Mengecek Queue Kosong

```python
def is_empty(self):
```

Baris ini membuat method untuk mengecek apakah queue masih kosong.

```python
return self.front_idx == -1
```

Baris ini mengembalikan nilai `True` jika `front_idx` masih bernilai `-1`. Jika nilainya bukan `-1`, berarti sudah ada data di dalam antrian.

---

### 3. Mengecek Queue Penuh

```python
def is_full(self):
```

Baris ini membuat method untuk mengecek apakah queue sudah penuh.

```python
return (self.rear_idx + 1) % self.MAXN == self.front_idx
```

Baris ini mengecek apakah posisi setelah `rear_idx` sudah kembali ke `front_idx`. Jika iya, berarti antrian sudah penuh. Rumus ini dipakai karena queue dibuat dengan konsep circular queue.

---

### 4. Menambahkan Data ke Queue

```python
def enqueue(self, x):
```

Baris ini membuat method `enqueue`. Method ini digunakan untuk menambahkan data laundry baru ke antrian.

```python
if self.is_full():
```

Baris ini mengecek apakah antrian sudah penuh sebelum data baru dimasukkan.

```python
print("Antrian laundry penuh")
```

Baris ini menampilkan pesan jika antrian sudah penuh.

```python
return
```

Baris ini menghentikan proses `enqueue` jika antrian penuh.

```python
if self.is_empty():
```

Baris ini mengecek apakah antrian masih kosong.

```python
self.front_idx = 0
self.rear_idx = 0
```

Jika antrian masih kosong, data pertama akan ditempatkan pada indeks 0. Karena baru ada satu data, posisi depan dan belakang sama-sama berada di indeks 0.

```python
else:
```

Bagian ini dijalankan jika queue sudah berisi data.

```python
self.rear_idx = (self.rear_idx + 1) % self.MAXN
```

Baris ini menggeser posisi belakang queue ke indeks berikutnya.

```python
self.q[self.rear_idx] = x
```

Baris ini memasukkan data laundry ke posisi belakang queue.

```python
print(f"Data laundry {x} berhasil masuk antrian")
```

Baris ini menampilkan pesan bahwa data laundry berhasil masuk ke antrian.

---

### 5. Memproses Data dari Queue

```python
def dequeue(self):
```

Baris ini membuat method `dequeue`. Method ini digunakan untuk mengambil dan menghapus data paling depan dari antrian.

```python
if self.is_empty():
```

Baris ini mengecek apakah antrian kosong sebelum proses dilakukan.

```python
print("Antrian laundry kosong")
```

Baris ini menampilkan pesan jika tidak ada data laundry yang bisa diproses.

```python
return
```

Baris ini menghentikan proses `dequeue` jika antrian kosong.

```python
print(f"Data laundry {self.q[self.front_idx]} sedang diproses")
```

Baris ini menampilkan data laundry yang berada di posisi paling depan. Data inilah yang sedang diproses.

```python
self.q[self.front_idx] = None
```

Baris ini menghapus data paling depan dengan menggantinya menjadi `None`.

```python
if self.front_idx == self.rear_idx:
```

Baris ini mengecek apakah data yang dihapus adalah satu-satunya data di dalam queue.

```python
self.front_idx = -1
self.rear_idx = -1
```

Jika data yang dihapus adalah satu-satunya data, maka queue dikembalikan ke kondisi kosong.

```python
else:
```

Bagian ini dijalankan jika setelah data depan dihapus masih ada data lain di dalam queue.

```python
self.front_idx = (self.front_idx + 1) % self.MAXN
```

Baris ini menggeser posisi depan queue ke indeks berikutnya.

---

### 6. Melihat Data Paling Depan

```python
def peek(self):
```

Baris ini membuat method `peek`. Method ini digunakan untuk melihat data paling depan tanpa menghapusnya.

```python
if self.is_empty():
```

Baris ini mengecek apakah antrian kosong.

```python
print("Antrian laundry kosong")
```

Baris ini menampilkan pesan jika belum ada data laundry dalam antrian.

```python
return
```

Baris ini menghentikan method jika antrian kosong.

```python
print(f"Data laundry paling depan: {self.q[self.front_idx]}")
```

Baris ini menampilkan data laundry yang berada pada posisi paling depan.

---

### 7. Menampilkan Semua Isi Queue

```python
def display(self):
```

Baris ini membuat method `display`. Method ini digunakan untuk menampilkan seluruh isi antrian laundry.

```python
if self.is_empty():
```

Baris ini mengecek apakah antrian masih kosong.

```python
print("Antrian laundry kosong")
```

Baris ini menampilkan pesan jika belum ada data laundry.

```python
return
```

Baris ini menghentikan method jika queue kosong.

```python
print("Isi antrian laundry (depan ke belakang): ", end="")
```

Baris ini menampilkan teks pembuka sebelum isi antrian dicetak.

```python
i = self.front_idx
```

Baris ini membuat variabel `i` yang dimulai dari posisi depan queue.

```python
while True:
```

Baris ini membuat perulangan untuk menampilkan data dari depan sampai belakang.

```python
print(self.q[i], end=" ; ")
```

Baris ini mencetak data pada indeks ke-`i`.

```python
if i == self.rear_idx:
```

Baris ini mengecek apakah data yang dicetak sudah sampai ke posisi belakang queue.

```python
break
```

Jika sudah sampai belakang, perulangan dihentikan.

```python
i = (i + 1) % self.MAXN
```

Jika belum sampai belakang, indeks `i` digeser ke data berikutnya.

```python
print()
```

Baris ini digunakan agar output berikutnya pindah ke baris baru.

---

### 8. Fungsi Input Data Laundry

```python
def input_data_laundry():
```

Baris ini membuat fungsi untuk memasukkan data laundry.

```python
nama = input("Nama pelanggan: ")
```

Baris ini meminta pengguna memasukkan nama pelanggan.

```python
while True:
```

Baris ini membuat perulangan agar program terus meminta input berat sampai data yang dimasukkan benar.

```python
try:
```

Baris ini digunakan untuk mencoba menjalankan input berat laundry.

```python
berat = float(input("Berat laundry (kg): "))
```

Baris ini meminta pengguna memasukkan berat laundry. Input diubah menjadi `float` agar bisa menerima angka desimal seperti `2.5`.

```python
if berat <= 0:
```

Baris ini mengecek apakah berat laundry bernilai nol atau negatif.

```python
print("Berat laundry harus lebih dari 0 kg")
```

Baris ini menampilkan pesan jika berat yang dimasukkan tidak valid.

```python
continue
```

Baris ini membuat program kembali meminta input berat laundry.

```python
return f"{nama} - {berat} kg"
```

Jika data sudah benar, baris ini mengembalikan data laundry dalam format nama pelanggan dan berat laundry.

```python
except ValueError:
```

Baris ini menangani kesalahan jika pengguna memasukkan berat bukan angka.

```python
print("Input berat tidak valid")
```

Baris ini menampilkan pesan jika input berat tidak valid.

---

### 9. Fungsi Main

```python
def main():
```

Baris ini membuat fungsi utama program.

```python
queue = QueueArray()
```

Baris ini membuat objek queue dari class `QueueArray`.

```python
pilih = 0
```

Baris ini membuat variabel `pilih` dengan nilai awal 0.

```python
while pilih != 5:
```

Baris ini membuat menu terus berjalan selama pengguna belum memilih menu 5.

```python
print("\n=== SISTEM ANTRIAN LAUNDRY ===")
```

Baris ini menampilkan judul program.

```python
print("1. Tambah laundry")
print("2. Proses laundry")
print("3. Lihat laundry paling depan")
print("4. Tampilkan antrian")
print("5. Keluar")
```

Baris-baris ini menampilkan menu yang bisa dipilih pengguna.

```python
pilih = int(input("Pilih: "))
```

Baris ini meminta pengguna memasukkan pilihan menu, lalu mengubahnya menjadi integer.

```python
except ValueError:
```

Baris ini menangani kesalahan jika input menu bukan angka.

```python
print("Input tidak valid")
continue
```

Jika input menu tidak valid, program menampilkan pesan error dan kembali ke menu awal.

```python
if pilih == 1:
```

Jika pengguna memilih menu 1, program akan menambahkan data laundry ke antrian.

```python
data_laundry = input_data_laundry()
```

Baris ini memanggil fungsi input data laundry.

```python
queue.enqueue(data_laundry)
```

Baris ini memasukkan data laundry ke queue menggunakan method `enqueue`.

```python
elif pilih == 2:
```

Jika pengguna memilih menu 2, program akan memproses data laundry paling depan.

```python
queue.dequeue()
```

Baris ini memproses data paling depan menggunakan method `dequeue`.

```python
elif pilih == 3:
```

Jika pengguna memilih menu 3, program akan menampilkan data laundry paling depan.

```python
queue.peek()
```

Baris ini melihat data paling depan menggunakan method `peek`.

```python
elif pilih == 4:
```

Jika pengguna memilih menu 4, program akan menampilkan seluruh antrian laundry.

```python
queue.display()
```

Baris ini menampilkan seluruh isi queue menggunakan method `display`.

```python
elif pilih == 5:
```

Jika pengguna memilih menu 5, program akan keluar.

```python
print("Program selesai.")
```

Baris ini menampilkan pesan bahwa program selesai.

```python
else:
    print("Pilihan tidak valid!")
```

Bagian ini dijalankan jika pengguna memasukkan angka menu selain 1 sampai 5.

```python
if __name__ == "__main__":
    main()
```

Baris ini memastikan fungsi `main()` dijalankan saat file Python dieksekusi langsung.

---

## Output Program

> Tambahkan screenshot output program di bagian ini setelah program dijalankan.

```html
<img width="790" height="226" alt="Output Queue Antrian Laundry" src="LINK_GAMBAR_OUTPUT" />
```

### Contoh Output Menambahkan Data Nabil

```text
=== SISTEM ANTRIAN LAUNDRY ===
1. Tambah laundry
2. Proses laundry
3. Lihat laundry paling depan
4. Tampilkan antrian
5. Keluar
Pilih: 1
Nama pelanggan: Nabil
Berat laundry (kg): 3
Data laundry Nabil - 3.0 kg berhasil masuk antrian
```

Penjelasan per baris:

```text
=== SISTEM ANTRIAN LAUNDRY ===
```

Baris ini adalah judul program.

```text
1. Tambah laundry
2. Proses laundry
3. Lihat laundry paling depan
4. Tampilkan antrian
5. Keluar
```

Bagian ini menampilkan pilihan menu.

```text
Pilih: 1
```

Pengguna memilih menu 1 untuk menambahkan data laundry.

```text
Nama pelanggan: Nabil
```

Pengguna memasukkan nama pelanggan, yaitu Nabil.

```text
Berat laundry (kg): 3
```

Pengguna memasukkan berat laundry Nabil sebesar 3 kg.

```text
Data laundry Nabil - 3.0 kg berhasil masuk antrian
```

Program menampilkan bahwa data laundry Nabil berhasil masuk ke antrian.

---

### Contoh Output Menambahkan Data Raffi dan Fathir

```text
Pilih: 1
Nama pelanggan: Raffi
Berat laundry (kg): 2.5
Data laundry Raffi - 2.5 kg berhasil masuk antrian

Pilih: 1
Nama pelanggan: Fathir
Berat laundry (kg): 4
Data laundry Fathir - 4.0 kg berhasil masuk antrian
```

Penjelasan singkatnya, Raffi dan Fathir juga dimasukkan ke antrian menggunakan menu 1. Karena Raffi dimasukkan setelah Nabil, posisi Raffi berada di belakang Nabil. Fathir berada di belakang Raffi karena dimasukkan setelah Raffi.

---

### Contoh Output Menampilkan Antrian

```text
Pilih: 4
Isi antrian laundry (depan ke belakang): Nabil - 3.0 kg ; Raffi - 2.5 kg ; Fathir - 4.0 kg ;
```

Penjelasan per baris:

```text
Pilih: 4
```

Pengguna memilih menu 4 untuk menampilkan seluruh isi antrian.

```text
Isi antrian laundry (depan ke belakang): Nabil - 3.0 kg ; Raffi - 2.5 kg ; Fathir - 4.0 kg ;
```

Program menampilkan data dari depan ke belakang. Nabil berada paling depan karena data Nabil masuk pertama. Raffi berada setelah Nabil, lalu Fathir berada paling belakang.

---

### Contoh Output Melihat Data Paling Depan

```text
Pilih: 3
Data laundry paling depan: Nabil - 3.0 kg
```

Penjelasan per baris:

```text
Pilih: 3
```

Pengguna memilih menu 3 untuk melihat data laundry yang berada paling depan.

```text
Data laundry paling depan: Nabil - 3.0 kg
```

Program menampilkan data Nabil karena Nabil adalah pelanggan yang pertama masuk ke antrian.

---

### Contoh Output Memproses Laundry

```text
Pilih: 2
Data laundry Nabil - 3.0 kg sedang diproses
```

Penjelasan per baris:

```text
Pilih: 2
```

Pengguna memilih menu 2 untuk memproses laundry paling depan.

```text
Data laundry Nabil - 3.0 kg sedang diproses
```

Program memproses data Nabil karena Nabil berada di posisi paling depan. Setelah diproses, data Nabil keluar dari antrian.

Jika antrian ditampilkan lagi, hasilnya menjadi:

```text
Pilih: 4
Isi antrian laundry (depan ke belakang): Raffi - 2.5 kg ; Fathir - 4.0 kg ;
```

Raffi sekarang menjadi data paling depan karena Nabil sudah diproses.

---

### Contoh Output Jika Input Tidak Valid

#### 1. Input menu bukan angka

```text
Pilih: dua
Input tidak valid
```

Program menampilkan pesan tersebut karena menu harus dimasukkan dalam bentuk angka.

#### 2. Berat laundry bukan angka

```text
Nama pelanggan: Nabil
Berat laundry (kg): tiga
Input berat tidak valid
```

Program menampilkan pesan tersebut karena berat laundry harus berupa angka.

#### 3. Berat laundry nol atau negatif

```text
Nama pelanggan: Raffi
Berat laundry (kg): 0
Berat laundry harus lebih dari 0 kg
```

Program menampilkan pesan tersebut karena berat laundry harus lebih dari 0 kg.

---

## Link YouTube

[Masukkan link YouTube di sini setelah video di-upload]
