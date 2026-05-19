# Tugas Akhir Percobaan 4

## Judul Program

**Sistem Antrian Laundry Menggunakan Queue**

---

## Deskripsi Singkat

Program ini dibuat untuk mengimplementasikan konsep Queue pada studi kasus kehidupan sehari-hari, yaitu sistem antrian laundry. Dalam proses laundry, data pelanggan yang masuk lebih dulu sebaiknya diproses lebih dulu agar urutan pelayanan tetap adil dan teratur.

Pada program ini, setiap pelanggan memasukkan data berupa nama dan berat laundry dalam satuan kilogram. Data tersebut kemudian dimasukkan ke dalam antrian menggunakan operasi enqueue(). Ketika laundry mulai diproses, data pelanggan yang berada di bagian paling depan akan dikeluarkan menggunakan operasi dequeue().

Struktur data yang digunakan adalah Queue, karena sistem antrian laundry sesuai dengan prinsip First In First Out (FIFO). Artinya, data pertama yang masuk ke dalam antrian akan menjadi data pertama yang diproses.

---

## Source Code

<img width="1258" height="4438" alt="Laundry fix" src="https://github.com/user-attachments/assets/17c41fb5-9516-41d6-9c49-aa6a4e9beb5e" />

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

Baris ini adalah metode inisialisasi dalam pemrograman Python. Bagian ini akan otomatis dijalankan ketika objek queue dibuat. Nilai `max_size=100` berarti kapasitas maksimal antrian adalah 100 data.

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

<img width="496" height="718" alt="Screenshot 2026-05-19 212552" src="https://github.com/user-attachments/assets/fbce6186-f1ac-4d98-8ee2-3b8f479102dd" />

Contoh Output Menambahkan Data Laundry

<img width="483" height="240" alt="Screenshot 2026-05-19 212419" src="https://github.com/user-attachments/assets/af2c35d0-e097-4a4b-bcbd-70f1a99fc0aa" />

Pada contoh output tersebut, pengguna memilih menu 1 untuk menambahkan data laundry. Data yang dimasukkan adalah pelanggan bernama Nabil dengan berat laundry 3 kg.

Saat menu ini dijalankan, program memanggil method `enqueue()`. Method ini berfungsi untuk memasukkan data baru ke bagian belakang antrian. Karena sebelumnya antrian masih kosong, data Nabil menjadi data pertama sekaligus berada di posisi paling depan.

Contoh Output Menambahkan Beberapa Data Laundry

<img width="480" height="101" alt="Screenshot 2026-05-19 212602" src="https://github.com/user-attachments/assets/727a83d9-20e1-429e-9faf-26fd79def613" />
<img width="491" height="97" alt="Screenshot 2026-05-19 212610" src="https://github.com/user-attachments/assets/b92c33e0-8c25-4df6-ae81-162b4041849c" />

Pada contoh di atas, pengguna kembali memilih menu 1 untuk menambahkan data Raffi dan Fathir. Setiap kali menu ini dipilih, program akan memanggil method `enqueue()`.

Karena Queue menggunakan prinsip FIFO, data yang masuk lebih dulu akan berada di depan. Urutan antriannya menjadi Nabil, Raffi, lalu Fathir.

Contoh Output Menampilkan Antrian

<img width="862" height="197" alt="Screenshot 2026-05-19 212850" src="https://github.com/user-attachments/assets/f7c7ad2c-bdbd-418f-82b0-7b77840b2d2c" />

Pada output tersebut, pengguna memilih menu 4 untuk menampilkan seluruh isi antrian laundry. Menu ini memanggil method `display()`.

Method `display()` menampilkan data dari posisi depan sampai belakang. Karena Nabil masuk pertama, maka Nabil berada di depan. Raffi berada setelah Nabil, dan Fathir berada di posisi paling belakang.

Contoh Output Melihat Laundry Paling Depan

<img width="392" height="186" alt="Screenshot 2026-05-19 212903" src="https://github.com/user-attachments/assets/68bcae63-510d-4dc0-817c-c14e7c0b0c4c" />

Pada output tersebut, pengguna memilih menu 3 untuk melihat data laundry yang berada di posisi paling depan. Menu ini memanggil method `peek()`.

Method `peek()` hanya menampilkan data paling depan tanpa menghapus data tersebut dari antrian. Jadi, data Nabil masih tetap berada di dalam antrian setelah menu ini dijalankan.

Contoh Output Memproses Laundry

<img width="416" height="186" alt="Screenshot 2026-05-19 212921" src="https://github.com/user-attachments/assets/08f3e858-d82c-4a0c-9a18-0d99864f99ad" />

Pada output tersebut, pengguna memilih menu 2 untuk memproses data laundry paling depan. Menu ini memanggil method `dequeue()`.

Method `dequeue()` mengambil data yang berada di bagian paling depan, kemudian menghapus data tersebut dari antrian. Karena Nabil adalah data pertama yang masuk, maka Nabil juga menjadi data pertama yang diproses.

Setelah Nabil diproses, jika antrian ditampilkan lagi maka hasilnya menjadi:

<img width="695" height="195" alt="Screenshot 2026-05-19 212933" src="https://github.com/user-attachments/assets/460b8920-138e-4ac9-bf4e-99d28889da09" />

Output tersebut menunjukkan bahwa data Nabil sudah keluar dari antrian. Setelah Nabil diproses, posisi paling depan berpindah ke Raffi.

Contoh Output Jika Antrian Kosong

<img width="307" height="180" alt="Screenshot 2026-05-19 213021" src="https://github.com/user-attachments/assets/beec9e6f-331b-4560-8a10-5ffd654e0059" />

Output tersebut muncul ketika pengguna memilih menu 2, tetapi belum ada data laundry di dalam antrian. Pada kondisi ini, method dequeue() tetap dipanggil, tetapi program mengecek terlebih dahulu apakah Queue kosong menggunakan method `is_empty()`.

Karena antrian kosong, program menampilkan pesan bahwa antrian laundry kosong.

<img width="298" height="192" alt="Screenshot 2026-05-19 213005" src="https://github.com/user-attachments/assets/beaa7deb-3f93-4198-b22f-592ee2448979" />

Output tersebut muncul ketika pengguna memilih menu 3, tetapi antrian masih kosong. Method peek() dipanggil, lalu program mengecek kondisi antrian menggunakan `is_empty()`.

Karena tidak ada data paling depan yang bisa ditampilkan, program menampilkan pesan bahwa antrian laundry kosong.

<img width="303" height="193" alt="Screenshot 2026-05-19 213039" src="https://github.com/user-attachments/assets/0cf1293d-b1f7-48fc-965b-5b06b76b7e7c" />

Output tersebut muncul ketika pengguna memilih menu 4, tetapi belum ada data yang tersimpan dalam antrian. Method `display()` dipanggil, tetapi karena Queue kosong, program hanya menampilkan pesan bahwa antrian laundry kosong.

---

### Contoh Output Jika Input Tidak Valid

#### 1. Input menu bukan angka

<img width="287" height="177" alt="Screenshot 2026-05-19 213051" src="https://github.com/user-attachments/assets/4a3e8752-a862-4311-aa6d-364301118173" />

Program menampilkan pesan tersebut karena menu harus dimasukkan dalam bentuk angka.

#### 2. Berat laundry bukan angka

<img width="307" height="251" alt="Screenshot 2026-05-19 213118" src="https://github.com/user-attachments/assets/54ec5974-9d52-4dc6-9e7d-bdfb4b0376a5" />


Program menampilkan pesan tersebut karena berat laundry harus berupa angka.

#### 3. Berat laundry nol atau negatif

<img width="363" height="252" alt="Screenshot 2026-05-19 213147" src="https://github.com/user-attachments/assets/b61bdfff-0c29-420e-91cf-4f779d41155d" />

Program menampilkan pesan tersebut karena berat laundry harus lebih dari 0 kg.

---

## Link YouTube


