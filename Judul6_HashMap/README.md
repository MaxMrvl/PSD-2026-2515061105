# Tugas Akhir Percobaan 6

## Judul Program

**Sistem Data Anime Favorit Menggunakan Hash Map Open Addressing**

---

## Deskripsi Singkat

Program ini dibuat untuk mengimplementasikan konsep Hash Map pada studi kasus sederhana, yaitu sistem data anime favorit. Data anime disimpan menggunakan pasangan key dan value. Pada program ini, key berupa kode anime dalam bentuk integer, sedangkan value berupa judul anime.

Metode yang digunakan adalah Open Addressing dengan teknik Linear Probing. Jika terjadi tabrakan indeks atau collision, program akan mencari slot kosong berikutnya di dalam hash table. Program ini mengikuti pondasi kode Percobaan VI-1 `HashMapOpenAddressing.py`, yang memakai `SlotState`, `Entry`, `HashMapOpenAddressing`, `insert()`, `search()`, `remove_key()`, dan `display()`.

Contoh data:

```text
101 = Naruto
111 = One Piece
121 = Bleach
```

Jika ukuran tabel adalah 10, maka kode 101, 111, dan 121 sama-sama menghasilkan indeks awal 1 karena dihitung menggunakan key % 10. Karena indeks awalnya sama, maka terjadi collision. Di sinilah linear probing dipakai untuk mencari slot kosong berikutnya.

---

## Source Code

---

## Penjelasan Kode

### 1. Class `SlotState`

```python
class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2
```

Class ini digunakan untuk memberi status pada setiap slot di hash table.

`EMPTY` berarti slot masih kosong.

`OCCUPIED` berarti slot sedang berisi data.

`DELETED` berarti slot sebelumnya pernah berisi data, tetapi datanya sudah dihapus.

Status `DELETED` tetap diperlukan karena pada open addressing, pencarian data tidak boleh langsung berhenti di slot bekas hapus.

---

### 2. Class `Entry`

```python
class Entry:
```

Class `Entry` digunakan untuk membuat satu tempat penyimpanan data di dalam hash table.

```python
def __init__(self):
```

Constructor ini dijalankan saat objek `Entry` dibuat.

```python
self.key = None
self.value = None
self.state = SlotState.EMPTY
```

`self.key` digunakan untuk menyimpan kode anime.

`self.value` digunakan untuk menyimpan judul anime.

`self.state` digunakan untuk menyimpan status slot. Nilai awalnya adalah `EMPTY` karena slot belum berisi data.

---

### 3. Class `HashMapOpenAddressing`

```python
class HashMapOpenAddressing:
```

Class ini digunakan untuk membuat struktur hash map dengan metode open addressing.

```python
def __init__(self, size=10):
```

Constructor ini menerima parameter `size`. Nilai default-nya adalah `10`, sehingga hash table memiliki 10 slot.

```python
self.SIZE = size
self.table = [Entry() for _ in range(self.SIZE)]
```

`self.SIZE` menyimpan ukuran hash table.

`self.table` membuat list berisi objek `Entry` sebanyak ukuran tabel.

---

### 4. Method `hash_function(key)`

```python
def hash_function(self, key):
    return (key % self.SIZE + self.SIZE) % self.SIZE
```

Method ini digunakan untuk menentukan indeks awal dari sebuah key.

Misalnya ukuran tabel adalah `10` dan key yang dimasukkan adalah `101`.

```text
101 % 10 = 1
```

Maka data anime dengan kode `101` akan diarahkan ke indeks `1`.

---

### 5. Method `insert(key, value)`

```python
def insert(self, key, value):
```

Method `insert()` digunakan untuk menambahkan data anime ke dalam hash table.

```python
idx = self.hash_function(key)
```

Baris ini memanggil `hash_function()` untuk menentukan indeks awal berdasarkan kode anime.

```python
first_deleted = -1
```

Variabel `first_deleted` digunakan untuk menyimpan posisi slot yang berstatus `DELETED`. Jika nanti tidak ada slot kosong, slot bekas hapus bisa digunakan ulang.

```python
for step in range(self.SIZE):
```

Perulangan ini digunakan untuk melakukan pencarian slot. Jumlah percobaan maksimal sama dengan ukuran hash table.

```python
i = (idx + step) % self.SIZE
```

Baris ini adalah bagian linear probing. Jika slot awal penuh, program akan mencoba slot berikutnya.

```python
if self.table[i].state == SlotState.OCCUPIED:
```

Kondisi ini mengecek apakah slot sedang berisi data.

```python
if self.table[i].key == key:
    self.table[i].value = value
    return True
```

Jika key yang dimasukkan sudah ada, maka value lama akan diganti dengan value baru.

```python
elif self.table[i].state == SlotState.DELETED:
```

Bagian ini dijalankan jika program menemukan slot bekas data yang sudah dihapus.

```python
if first_deleted == -1:
    first_deleted = i
```

Jika belum ada slot `DELETED` yang disimpan, maka indeks tersebut dicatat ke variabel `first_deleted`.

```python
else:
```

Bagian ini dijalankan jika slot yang ditemukan masih kosong atau `EMPTY`.

```python
if first_deleted != -1:
    i = first_deleted
```

Jika sebelumnya ada slot `DELETED`, program akan menggunakan slot tersebut lebih dulu.

```python
self.table[i].key = key
self.table[i].value = value
self.table[i].state = SlotState.OCCUPIED
return True
```

Data anime dimasukkan ke slot yang tersedia. Setelah itu status slot diubah menjadi `OCCUPIED`.

```python
return False
```

Jika tidak ada slot kosong, fungsi mengembalikan `False`.

---

### 6. Method `search(key)`

```python
def search(self, key):
```

Method `search()` digunakan untuk mencari data anime berdasarkan kode anime.

```python
idx = self.hash_function(key)
```

Program menentukan indeks awal menggunakan hash function.

```python
for step in range(self.SIZE):
```

Perulangan digunakan untuk mencari key dari indeks awal sampai slot berikutnya jika terjadi collision.

```python
i = (idx + step) % self.SIZE
```

Baris ini membuat pencarian bergerak secara linear dari slot awal ke slot berikutnya.

```python
if self.table[i].state == SlotState.EMPTY:
    return None
```

Jika program menemukan slot kosong, pencarian dihentikan karena data tidak ditemukan.

```python
if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
    return self.table[i]
```

Jika slot berisi data dan key-nya sama dengan key yang dicari, maka data dikembalikan.

```python
return None
```

Jika seluruh slot sudah diperiksa tetapi data tidak ditemukan, fungsi mengembalikan `None`.

---

### 7. Method `remove_key(key)`

```python
def remove_key(self, key):
```

Method ini digunakan untuk menghapus data anime berdasarkan kode anime.

```python
entry = self.search(key)
```

Program mencari data terlebih dahulu menggunakan method `search()`.

```python
if entry is None:
    return False
```

Jika data tidak ditemukan, proses hapus gagal.

```python
entry.state = SlotState.DELETED
return True
```

Jika data ditemukan, status slot diubah menjadi `DELETED`. Data tidak langsung diubah menjadi `EMPTY` agar proses pencarian dengan linear probing tetap berjalan dengan benar.

---

### 8. Method `display()`

```python
def display(self):
```

Method ini digunakan untuk menampilkan seluruh isi hash table.

```python
for i in range(self.SIZE):
```

Perulangan ini digunakan untuk mengecek semua slot dari indeks pertama sampai indeks terakhir.

```python
if self.table[i].state == SlotState.EMPTY:
    print("EMPTY")
```

Jika slot kosong, program menampilkan `EMPTY`.

```python
elif self.table[i].state == SlotState.DELETED:
    print("DELETED")
```

Jika slot adalah bekas data yang sudah dihapus, program menampilkan `DELETED`.

```python
else:
    print(f"({self.table[i].key}, {self.table[i].value})")
```

Jika slot berisi data, program menampilkan kode anime dan judul anime.

---

### 9. Fungsi `input_kode_anime()`

```python
def input_kode_anime():
```

Fungsi ini digunakan untuk menerima input kode anime dari pengguna.

```python
kode = int(input("Masukkan kode anime: "))
```

Baris ini meminta pengguna memasukkan kode anime. Input diubah menjadi integer karena key pada hash map berupa angka.

```python
if kode <= 0:
    print("Kode anime harus lebih dari 0")
    continue
```

Bagian ini memastikan kode anime tidak bernilai nol atau negatif.

```python
return kode
```

Jika input valid, kode anime dikembalikan ke fungsi utama.

---

### 10. Fungsi `main()`

```python
def main():
```

Fungsi `main()` adalah fungsi utama yang menjalankan menu program.

```python
hashmap = HashMapOpenAddressing()
```

Baris ini membuat objek `hashmap` dari class `HashMapOpenAddressing`.

Menu yang tersedia:

```text
1. Tambah data anime
2. Cari data anime
3. Hapus data anime
4. Tampilkan hash table
5. Keluar
```

Menu `1` memanggil method `insert()` untuk menambahkan data anime.

Menu `2` memanggil method `search()` untuk mencari data anime berdasarkan kode.

Menu `3` memanggil method `remove_key()` untuk menghapus data anime.

Menu `4` memanggil method `display()` untuk menampilkan hash table.

Menu `5` digunakan untuk keluar dari program.

---

## Output Program

### Contoh Output Menambahkan Data Anime

```text
=== SISTEM DATA ANIME FAVORIT ===
1. Tambah data anime
2. Cari data anime
3. Hapus data anime
4. Tampilkan hash table
5. Keluar
Pilih: 1
Masukkan kode anime: 101
Masukkan judul anime: Naruto
Anime Naruto dengan kode 101 berhasil ditambahkan
```

Pada output tersebut, pengguna memilih menu `1`, sehingga program memanggil method `insert()`. Kode `101` diproses oleh `hash_function()` dan diarahkan ke indeks `1`.

---

### Contoh Output Menambahkan Data yang Mengalami Collision

```text
Pilih: 1
Masukkan kode anime: 111
Masukkan judul anime: One Piece
Anime One Piece dengan kode 111 berhasil ditambahkan

Pilih: 1
Masukkan kode anime: 121
Masukkan judul anime: Bleach
Anime Bleach dengan kode 121 berhasil ditambahkan
```

Pada contoh tersebut, kode `111` dan `121` juga menghasilkan indeks awal `1` karena `111 % 10 = 1` dan `121 % 10 = 1`.

Karena indeks `1` sudah ditempati oleh Naruto, maka program menggunakan linear probing untuk mencari slot kosong berikutnya. Data One Piece dan Bleach kemudian ditempatkan pada slot kosong setelahnya.

---

### Contoh Output Menampilkan Hash Table

```text
Pilih: 4

Isi Hash Table Anime:
0: EMPTY
1: (101, Naruto)
2: (111, One Piece)
3: (121, Bleach)
4: EMPTY
5: EMPTY
6: EMPTY
7: EMPTY
8: EMPTY
9: EMPTY
```

Output tersebut muncul ketika pengguna memilih menu `4`. Menu ini memanggil method `display()` untuk menampilkan isi hash table. Data Naruto berada pada indeks `1`, sedangkan One Piece dan Bleach berada di indeks setelahnya karena terjadi collision.

---

### Contoh Output Mencari Data Anime

```text
Pilih: 2
Masukkan kode anime: 111
Kode 111 ditemukan, judul anime: One Piece
```

Pada output tersebut, pengguna memilih menu `2`, sehingga program memanggil method `search()`. Program mencari kode `111` mulai dari indeks hasil hash sampai data ditemukan.

---

### Contoh Output Menghapus Data Anime

```text
Pilih: 3
Masukkan kode anime: 111
Anime dengan kode 111 berhasil dihapus
```

Pada output tersebut, pengguna memilih menu `3`, sehingga program memanggil method `remove_key()`. Data dengan kode `111` tidak langsung diubah menjadi `EMPTY`, tetapi statusnya diubah menjadi `DELETED`.

Jika hash table ditampilkan lagi, hasilnya menjadi:

```text
Pilih: 4

Isi Hash Table Anime:
0: EMPTY
1: (101, Naruto)
2: DELETED
3: (121, Bleach)
4: EMPTY
5: EMPTY
6: EMPTY
7: EMPTY
8: EMPTY
9: EMPTY
```

Slot indeks `2` berubah menjadi `DELETED` karena data One Piece sudah dihapus.

---

### Contoh Output Jika Input Tidak Valid

```text
Pilih: satu
Input tidak valid
```

Output tersebut muncul karena menu harus berupa angka.

```text
Masukkan kode anime: -5
Kode anime harus lebih dari 0
```

Output tersebut muncul karena kode anime tidak boleh nol atau negatif.

---

## Link YouTube
