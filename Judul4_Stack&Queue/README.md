# Tugas Akhir Percobaan 4

## Judul Program

**Sistem Antrian Laundry Menggunakan Queue**

---

## Deskripsi Singkat

Program ini dibuat untuk menerapkan struktur data **Queue** pada contoh yang dekat dengan kegiatan sehari-hari, yaitu antrian laundry. Pada tempat laundry, pakaian pelanggan biasanya diproses berdasarkan urutan kedatangan. Pelanggan yang datang lebih dulu akan diproses lebih dulu.

Karena itu, struktur data **Queue** cocok dipakai pada program ini. Queue menggunakan prinsip **First In First Out (FIFO)**, yaitu data yang pertama masuk akan menjadi data pertama yang keluar atau diproses.

---

## Source Code

<img width="1242" height="4457" alt="Laundry" src="https://github.com/user-attachments/assets/d398e9bd-a2f1-468c-b935-19bb413303e1" />

## Penjelasan Kode

### 1. Membuat class QueueArray

```python
class QueueArray:
```

Baris ini digunakan untuk membuat class bernama `QueueArray`.

Class ini menjadi tempat untuk menyimpan semua method yang berhubungan dengan Queue.

Pada program ini, Queue digunakan untuk menyimpan data antrian laundry.

---

### 2. Constructor QueueArray

```python
def __init__(self, max_size=100):
```

Baris ini adalah constructor.

Constructor akan dijalankan otomatis saat objek Queue dibuat.

Parameter `max_size=100` berarti kapasitas maksimal antrian adalah 100 data.

```python
self.MAXN = max_size
```

Baris ini menyimpan nilai kapasitas maksimal Queue ke dalam variabel `MAXN`.

```python
self.q = [None] * self.MAXN
```

Baris ini membuat list kosong dengan panjang sesuai kapasitas maksimal.

Isi awalnya adalah `None` karena belum ada data laundry yang masuk.

```python
self.front_idx = -1
```

Baris ini membuat penanda posisi data paling depan.

Nilai awalnya `-1` karena antrian masih kosong.

```python
self.rear_idx = -1
```

Baris ini membuat penanda posisi data paling belakang.

Nilai awalnya juga `-1` karena belum ada data dalam antrian.

---

### 3. Method is_empty

```python
def is_empty(self):
```

Baris ini membuat method untuk mengecek apakah Queue kosong.

```python
return self.front_idx == -1
```

Jika `front_idx` bernilai `-1`, berarti belum ada data laundry dalam antrian.

Method ini akan mengembalikan nilai `True` jika Queue kosong.

---

### 4. Method is_full

```python
def is_full(self):
```

Baris ini membuat method untuk mengecek apakah Queue sudah penuh.

```python
return (self.rear_idx + 1) % self.MAXN == self.front_idx
```

Baris ini memakai rumus circular queue.

Jika posisi setelah `rear_idx` sama dengan `front_idx`, maka antrian dianggap penuh.

---

### 5. Method enqueue

```python
def enqueue(self, x):
```

Method ini digunakan untuk menambahkan data baru ke antrian.

Pada program ini, data yang masuk adalah nama pelanggan dan berat laundry.

```python
if self.is_full():
```

Baris ini mengecek apakah antrian sudah penuh.

```python
print("Antrian laundry penuh")
```

Jika penuh, program menampilkan pesan bahwa antrian laundry penuh.

```python
return
```

Baris ini menghentikan proses agar data baru tidak dimasukkan.

```python
if self.is_empty():
```

Baris ini mengecek apakah antrian masih kosong.

```python
self.front_idx = 0
self.rear_idx = 0
```

Jika antrian kosong, maka data pertama akan diletakkan pada indeks 0.

Karena baru ada satu data, posisi depan dan belakang sama-sama berada di indeks 0.

```python
else:
```

Bagian ini dijalankan jika antrian sudah memiliki data sebelumnya.

```python
self.rear_idx = (self.rear_idx + 1) % self.MAXN
```

Baris ini menggeser posisi belakang ke indeks berikutnya.

```python
self.q[self.rear_idx] = x
```

Baris ini memasukkan data laundry ke posisi belakang antrian.

```python
print(f"Data laundry {x} berhasil masuk antrian")
```

Baris ini menampilkan pesan bahwa data berhasil ditambahkan.

---

### 6. Method dequeue

```python
def dequeue(self):
```

Method ini digunakan untuk mengeluarkan data dari bagian depan Queue.

Pada program ini, data yang keluar adalah laundry yang sedang diproses.

```python
if self.is_empty():
```

Baris ini mengecek apakah antrian masih kosong.

```python
print("Antrian laundry kosong")
```

Jika kosong, program menampilkan pesan bahwa antrian laundry kosong.

```python
return
```

Baris ini menghentikan proses karena tidak ada data yang bisa diproses.

```python
print(f"Data laundry {self.q[self.front_idx]} sedang diproses")
```

Baris ini menampilkan data laundry yang berada di posisi paling depan.

Data inilah yang akan diproses lebih dulu.

```python
self.q[self.front_idx] = None
```

Baris ini menghapus data pada posisi depan dengan menggantinya menjadi `None`.

```python
if self.front_idx == self.rear_idx:
```

Baris ini mengecek apakah data yang dihapus adalah satu-satunya data dalam antrian.

```python
self.front_idx = -1
self.rear_idx = -1
```

Jika hanya ada satu data, maka setelah data diproses antrian menjadi kosong.

Karena itu, `front_idx` dan `rear_idx` dikembalikan ke `-1`.

```python
else:
```

Bagian ini dijalankan jika masih ada data lain dalam antrian.

```python
self.front_idx = (self.front_idx + 1) % self.MAXN
```

Baris ini menggeser posisi depan ke data berikutnya.

---

### 7. Method peek

```python
def peek(self):
```

Method ini digunakan untuk melihat data paling depan tanpa menghapusnya.

```python
if self.is_empty():
```

Baris ini mengecek apakah antrian kosong.

```python
print("Antrian laundry kosong")
```

Jika kosong, program menampilkan pesan bahwa tidak ada data dalam antrian.

```python
return
```

Baris ini menghentikan proses `peek`.

```python
print(f"Data laundry paling depan: {self.q[self.front_idx]}")
```

Jika antrian tidak kosong, program menampilkan data paling depan.

Data tersebut hanya dilihat, bukan dihapus.

---

### 8. Method display

```python
def display(self):
```

Method ini digunakan untuk menampilkan seluruh isi antrian laundry.

```python
if self.is_empty():
```

Baris ini mengecek apakah antrian kosong.

```python
print("Antrian laundry kosong")
```

Jika kosong, program menampilkan pesan bahwa antrian laundry kosong.

```python
return
```

Baris ini menghentikan proses tampilan.

```python
print("Isi antrian laundry (depan ke belakang): ", end="")
```

Baris ini menampilkan teks awal sebelum isi antrian dicetak.

```python
i = self.front_idx
```

Variabel `i` diisi dengan posisi data paling depan.

Pencetakan data dimulai dari bagian depan Queue.

```python
while True:
```

Perulangan ini digunakan untuk menampilkan data satu per satu.

```python
print(self.q[i], end=" | ")
```

Baris ini mencetak data pada indeks `i`.

```python
if i == self.rear_idx:
```

Baris ini mengecek apakah data yang dicetak sudah mencapai bagian belakang antrian.

```python
break
```

Jika sudah sampai data belakang, perulangan dihentikan.

```python
i = (i + 1) % self.MAXN
```

Jika belum sampai belakang, indeks digeser ke data berikutnya.

---

### 9. Fungsi input_data_laundry

```python
def input_data_laundry():
```

Fungsi ini digunakan untuk menerima input data laundry dari pengguna.

```python
nama = input("Nama pelanggan: ")
```

Baris ini meminta pengguna memasukkan nama pelanggan.

```python
while True:
```

Perulangan ini digunakan agar program terus meminta input berat sampai data yang dimasukkan benar.

```python
berat = float(input("Berat laundry (kg): "))
```

Baris ini meminta pengguna memasukkan berat laundry.

Tipe data yang digunakan adalah `float` karena berat laundry bisa berupa angka desimal.

```python
if berat <= 0:
```

Baris ini mengecek apakah berat laundry bernilai nol atau negatif.

```python
print("Berat laundry harus lebih dari 0 kg")
```

Jika berat tidak valid, program menampilkan pesan kesalahan.

```python
continue
```

Baris ini membuat program kembali meminta input berat.

```python
return f"{nama} - {berat} kg"
```

Jika input sudah benar, data nama dan berat digabungkan menjadi satu teks.

Teks inilah yang akan dimasukkan ke dalam Queue.

```python
except ValueError:
```

Bagian ini menangani kesalahan jika pengguna memasukkan teks pada input berat.

```python
print("Input berat tidak valid")
```

Program menampilkan pesan bahwa input berat salah.

---

### 10. Fungsi main

```python
def main():
```

Fungsi ini menjadi alur utama program.

```python
queue = QueueArray()
```

Baris ini membuat objek Queue bernama `queue`.

Objek ini digunakan untuk menyimpan data antrian laundry.

```python
pilih = 0
```

Variabel `pilih` digunakan untuk menyimpan pilihan menu dari pengguna.

```python
while pilih != 5:
```

Perulangan ini membuat menu terus tampil selama pengguna belum memilih keluar.

```python
pilih = int(input("Pilih: "))
```

Baris ini meminta pengguna memilih menu.

Input diubah menjadi integer karena menu berupa angka.

```python
except ValueError:
```

Bagian ini menangani input menu yang bukan angka.

```python
if pilih == 1:
```

Jika pengguna memilih menu 1, program akan menambahkan data laundry baru.

```python
data_laundry = input_data_laundry()
```

Baris ini memanggil fungsi input data laundry.

```python
queue.enqueue(data_laundry)
```

Baris ini memasukkan data laundry ke dalam Queue.

```python
elif pilih == 2:
```

Jika pengguna memilih menu 2, program akan memproses laundry paling depan.

```python
queue.dequeue()
```

Baris ini mengeluarkan data paling depan dari Queue.

```python
elif pilih == 3:
```

Jika pengguna memilih menu 3, program akan melihat data paling depan.

```python
queue.peek()
```

Baris ini menampilkan data paling depan tanpa menghapusnya.

```python
elif pilih == 4:
```

Jika pengguna memilih menu 4, program akan menampilkan semua antrian laundry.

```python
queue.display()
```

Baris ini mencetak semua isi Queue dari depan ke belakang.

```python
elif pilih == 5:
```

Jika pengguna memilih menu 5, program berhenti.

```python
print("Program selesai.")
```

Baris ini menampilkan pesan bahwa program selesai dijalankan.

---

## Output Program

> Tambahkan screenshot output program di bagian ini setelah program dijalankan.

```html
<img width="790" height="226" alt="Output Queue Antrian Laundry" src="LINK_GAMBAR_OUTPUT" />
```

### Contoh Output dan Penjelasan Per Baris

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

Bagian ini menampilkan daftar menu yang bisa dipilih pengguna.

```text
Pilih: 1
```

Pengguna memilih menu 1 untuk menambahkan data laundry.

```text
Nama pelanggan: Andi
```

Pengguna memasukkan nama pelanggan, yaitu Andi.

```text
Berat laundry (kg): 3
```

Pengguna memasukkan berat laundry sebesar 3 kg.

```text
Data laundry Andi - 3.0 kg berhasil masuk antrian
```

Program memberi tahu bahwa data Andi sudah masuk ke antrian.

```text
Pilih: 1
Nama pelanggan: Budi
Berat laundry (kg): 2
Data laundry Budi - 2.0 kg berhasil masuk antrian
```

Pada bagian ini, data pelanggan kedua juga dimasukkan ke antrian.

```text
Pilih: 4
```

Pengguna memilih menu 4 untuk menampilkan isi antrian.

```text
Isi antrian laundry (depan ke belakang): Andi - 3.0 kg | Budi - 2.0 kg |
```

Output ini menunjukkan bahwa Andi berada di depan, lalu Budi berada setelahnya.

```text
Pilih: 2
```

Pengguna memilih menu 2 untuk memproses laundry paling depan.

```text
Data laundry Andi - 3.0 kg sedang diproses
```

Program memproses data Andi terlebih dahulu.

Hal ini sesuai dengan prinsip Queue, karena Andi masuk lebih dulu daripada Budi.

---

## Penjelasan Output Jika Input Tidak Valid

### 1. Input menu bukan angka

```text
Pilih: dua
```

Input ini salah karena menu harus berupa angka.

Program akan menampilkan:

```text
Input tidak valid
```

### 2. Berat laundry bukan angka

```text
Berat laundry (kg): tiga
```

Input ini salah karena berat laundry harus berupa angka.

Program akan menampilkan:

```text
Input berat tidak valid
```

### 3. Berat laundry nol atau negatif

```text
Berat laundry (kg): 0
```

Input ini salah karena berat laundry harus lebih dari 0 kg.

Program akan menampilkan:

```text
Berat laundry harus lebih dari 0 kg
```

---

## Link YouTube

[Masukkan link YouTube di sini setelah video di-upload]
