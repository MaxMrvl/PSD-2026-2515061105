# Tugas Akhir Percobaan 3

## Judul Program

**Pencarian Nomor Kursi Bioskop Menggunakan Sequential Search Sentinel**

---

## Deskripsi Singkat

Program ini dibuat untuk mengecek apakah sebuah nomor kursi bioskop sudah dipesan atau masih tersedia. Data kursi yang sudah dipesan disimpan di dalam sebuah list, kemudian pengguna dapat memasukkan nomor kursi yang ingin dicek.

Nomor kursi yang dicari berbentuk **integer**, sehingga sesuai dengan konsep pada Percobaan III tentang Searching. Jika nomor kursi yang dimasukkan pengguna terdapat di dalam list, maka kursi tersebut dinyatakan sudah dipesan. Namun, jika nomor kursi tidak ditemukan di dalam list, maka kursi tersebut masih tersedia.

Algoritma yang digunakan adalah **Sequential Search Sentinel**. Sequential Search Sentinel bekerja dengan cara menambahkan data yang dicari ke bagian akhir list sebagai penanda sementara atau sentinel. Dengan adanya sentinel, proses pencarian dapat berhenti saat data ditemukan tanpa perlu menambahkan pengecekan batas list di dalam perulangan.

---

## Source Code

> Tambahkan screenshot source code di bagian ini setelah file di-upload ke GitHub.  
> Contoh format:
>
> ```html
> <img width="1320" height="2337" alt="Sequential Search Sentinel Kursi Bioskop" src="LINK_GAMBAR_SOURCE_CODE" />
> ```

### Penjelasan Kode

#### 1. Fungsi `sequential_search_sentinel(data, n, target)`

```python
def sequential_search_sentinel(data, n, target):
```

Fungsi `sequential_search_sentinel()` dibuat untuk mencari nomor kursi yang dimasukkan pengguna. Fungsi ini memiliki tiga parameter, yaitu `data`, `n`, dan `target`.

Parameter `data` berisi list nomor kursi yang sudah dipesan. Parameter `n` berisi jumlah data asli sebelum sentinel ditambahkan. Parameter `target` adalah nomor kursi yang ingin dicari oleh pengguna.

```python
data.append(target)
```

Baris ini digunakan untuk menambahkan nilai `target` ke bagian akhir list sebagai sentinel atau penanda sementara. Tujuannya agar proses pencarian pasti berhenti ketika menemukan nilai yang sama dengan target.

```python
i = 0
```

Variabel `i` digunakan sebagai indeks awal untuk melakukan pencarian. Karena indeks list pada Python dimulai dari 0, maka nilai awal `i` juga dibuat 0.

```python
while data[i] != target:
```

Perulangan `while` digunakan untuk memeriksa data satu per satu. Selama data pada indeks ke-`i` belum sama dengan target, maka pencarian akan terus dilanjutkan.

```python
i += 1
```

Jika data pada indeks saat ini belum sama dengan target, maka nilai `i` ditambah 1 agar program berpindah ke indeks berikutnya.

```python
data.pop()
```

Setelah proses pencarian selesai, sentinel yang sebelumnya ditambahkan di akhir list dihapus kembali menggunakan `pop()`. Hal ini dilakukan agar data asli tidak berubah secara permanen.

```python
if i < n:
```

Kondisi ini digunakan untuk mengecek apakah data ditemukan pada bagian data asli atau hanya ditemukan pada sentinel tambahan. Jika `i < n`, berarti target ditemukan di dalam data asli.

```python
return True, i
```

Jika target ditemukan di dalam data asli, fungsi mengembalikan nilai `True` dan indeks tempat data ditemukan.

```python
else:
    return False, -1
```

Jika target hanya ditemukan pada sentinel tambahan, berarti target tidak ada di dalam data asli. Dalam kondisi ini, fungsi mengembalikan nilai `False` dan indeks `-1`.

---

#### 2. Fungsi `main()`

```python
def main():
```

Fungsi `main()` adalah fungsi utama yang menjalankan alur program dari awal sampai akhir.

```python
kursi_terpesan = [3, 7, 10, 12, 18, 21, 25, 30, 33, 40]
```

List `kursi_terpesan` berisi data nomor kursi bioskop yang sudah dipesan. Data inilah yang akan digunakan sebagai tempat pencarian nomor kursi.

```python
n = len(kursi_terpesan)
```

Baris ini digunakan untuk menghitung jumlah data asli yang ada di dalam list `kursi_terpesan`. Nilai tersebut disimpan ke dalam variabel `n`.

```python
print("=== Sistem Pencarian Nomor Kursi Bioskop ===")
```

Baris ini digunakan untuk menampilkan judul program agar pengguna mengetahui bahwa program yang dijalankan adalah sistem pencarian nomor kursi bioskop.

```python
print(f"Data kursi yang sudah dipesan: {kursi_terpesan}")
```

Baris ini menampilkan daftar nomor kursi yang sudah dipesan.

```python
print("Nomor kursi tersedia dari 1 sampai 40")
```

Baris ini memberikan informasi bahwa nomor kursi yang valid berada pada rentang 1 sampai 40.

```python
while True:
```

Perulangan `while True` digunakan agar program terus meminta input sampai pengguna memasukkan nomor kursi yang valid.

```python
target = int(input("Masukkan nomor kursi yang ingin dicek: "))
```

Baris ini meminta pengguna memasukkan nomor kursi yang ingin dicari. Input diubah menjadi integer karena nomor kursi berupa angka.

```python
if target < 1 or target > 40:
```

Kondisi ini digunakan untuk mengecek apakah nomor kursi berada di luar rentang yang tersedia. Pada program ini, nomor kursi yang valid hanya dari 1 sampai 40.

```python
print("Nomor kursi tidak valid. Pilih nomor kursi dari 1 sampai 40.")
continue
```

Jika pengguna memasukkan nomor kursi kurang dari 1 atau lebih dari 40, maka program akan menampilkan pesan bahwa nomor kursi tidak valid. Perintah `continue` digunakan agar program kembali meminta input nomor kursi.

```python
break
```

Perintah `break` digunakan untuk keluar dari perulangan jika input yang dimasukkan sudah valid.

```python
except ValueError:
    print("Input tidak valid, silakan masukkan angka!")
```

Bagian ini digunakan untuk menangani kesalahan jika pengguna memasukkan input selain angka, misalnya huruf atau kata. Dengan adanya `except ValueError`, program tidak langsung berhenti, tetapi menampilkan pesan kesalahan dan meminta input ulang.

```python
found, index = sequential_search_sentinel(kursi_terpesan, n, target)
```

Baris ini memanggil fungsi `sequential_search_sentinel()` untuk mencari nomor kursi yang dimasukkan pengguna di dalam list `kursi_terpesan`.

Variabel `found` digunakan untuk menyimpan status apakah data ditemukan atau tidak. Variabel `index` digunakan untuk menyimpan posisi nomor kursi jika data ditemukan.

```python
if found:
```

Kondisi ini mengecek apakah nomor kursi ditemukan atau tidak. Jika `found` bernilai `True`, berarti nomor kursi ditemukan di dalam list.

```python
print(f"Kursi nomor {target} sudah dipesan.")
```

Jika nomor kursi ditemukan, program akan menampilkan bahwa kursi tersebut sudah dipesan.

```python
print(f"Data ditemukan pada indeks ke-{index}.")
```

Baris ini menampilkan indeks tempat nomor kursi ditemukan di dalam list.

```python
else:
    print(f"Kursi nomor {target} masih tersedia.")
```

Jika `found` bernilai `False`, berarti nomor kursi tidak ditemukan di dalam list. Oleh karena itu, program menampilkan bahwa kursi tersebut masih tersedia.

```python
if __name__ == "__main__":
    main()
```

Baris ini memastikan bahwa fungsi `main()` dijalankan ketika file Python dieksekusi secara langsung.

---

## Output Program

> Tambahkan screenshot output program di bagian ini setelah program dijalankan.  
> Contoh format:
>
> ```html
> <img width="790" height="226" alt="Output Program Kursi Bioskop" src="LINK_GAMBAR_OUTPUT" />
> ```

### Penjelasan Output Jika Kursi Sudah Dipesan

Pada awal program, sistem menampilkan daftar kursi yang sudah dipesan dan rentang nomor kursi yang tersedia, yaitu dari 1 sampai 40. Setelah itu, pengguna diminta memasukkan nomor kursi yang ingin dicek.

Contoh input yang dimasukkan adalah:

```text
12
```

Data kursi yang sudah dipesan adalah:

```text
[3, 7, 10, 12, 18, 21, 25, 30, 33, 40]
```

Program kemudian menjalankan algoritma Sequential Search Sentinel. Pertama, program menambahkan target ke akhir list sebagai sentinel. Karena target yang dicari adalah `12`, maka nilai `12` ditambahkan sementara ke akhir list.

Setelah itu, program memeriksa data dari indeks pertama sampai menemukan angka `12`.

Urutan pengecekannya dapat dijelaskan sebagai berikut:

```text
Indeks 0 = 3, bukan 12
Indeks 1 = 7, bukan 12
Indeks 2 = 10, bukan 12
Indeks 3 = 12, ditemukan
```

Karena angka `12` ditemukan sebelum indeks mencapai `n`, maka data ditemukan di dalam list asli. Program kemudian menampilkan:

```text
Kursi nomor 12 sudah dipesan.
Data ditemukan pada indeks ke-3.
```

Artinya, kursi nomor 12 tidak tersedia lagi karena sudah masuk ke dalam daftar kursi yang dipesan.

---

### Penjelasan Output Jika Kursi Masih Tersedia

Contoh input lain yang dimasukkan pengguna adalah:

```text
15
```

Program akan mencari angka `15` di dalam list kursi yang sudah dipesan.

Data kursi yang sudah dipesan adalah:

```text
[3, 7, 10, 12, 18, 21, 25, 30, 33, 40]
```

Karena menggunakan sentinel, angka `15` akan ditambahkan sementara ke akhir list. Program kemudian mencari angka `15` dari indeks pertama.

Karena angka `15` tidak ditemukan pada data asli, pencarian baru berhenti saat mencapai sentinel yang berada di akhir list. Setelah itu, sentinel dihapus kembali menggunakan `pop()`.

Karena posisi ditemukannya target tidak lebih kecil dari `n`, maka data dianggap tidak ditemukan dalam data asli. Program kemudian menampilkan:

```text
Kursi nomor 15 masih tersedia.
```

Artinya, kursi nomor 15 belum dipesan dan masih bisa dipilih oleh penonton.

---

### Penjelasan Output Jika Input Tidak Valid

Selain menampilkan hasil pencarian, program juga memiliki validasi input agar program tidak langsung error ketika pengguna memasukkan data yang salah.

#### 1. Input bukan angka

Contoh input tidak valid:

```text
dua belas
```

Padahal program meminta input berupa angka untuk nomor kursi. Karena input tersebut tidak bisa diubah menjadi tipe data integer, maka program menampilkan pesan:

```text
Input tidak valid, silakan masukkan angka!
```

Bagian kode yang menangani hal ini adalah:

```python
try:
    target = int(input("Masukkan nomor kursi yang ingin dicek: "))
except ValueError:
    print("Input tidak valid, silakan masukkan angka!")
```

`try` digunakan untuk mencoba menjalankan input dan mengubahnya menjadi integer. Jika input berupa teks seperti `dua belas`, maka akan terjadi `ValueError`. Kesalahan tersebut ditangani oleh `except ValueError`, sehingga program tidak berhenti secara tiba-tiba.

---

#### 2. Input angka di luar rentang kursi

Contoh input tidak valid:

```text
50
```

Walaupun `50` adalah angka, nilai tersebut tetap dianggap tidak valid karena nomor kursi hanya tersedia dari 1 sampai 40.

Program akan menampilkan pesan:

```text
Nomor kursi tidak valid. Pilih nomor kursi dari 1 sampai 40.
```

Bagian kode yang menangani validasi rentang kursi adalah:

```python
if target < 1 or target > 40:
    print("Nomor kursi tidak valid. Pilih nomor kursi dari 1 sampai 40.")
    continue
```

Kondisi `if target < 1 or target > 40` digunakan untuk memastikan bahwa nomor kursi yang dimasukkan pengguna masih berada dalam rentang kursi yang tersedia. Jika pengguna memasukkan angka kurang dari 1 atau lebih dari 40, maka program menampilkan pesan kesalahan dan menjalankan `continue`.

Perintah `continue` membuat program kembali meminta input nomor kursi yang benar. Dengan begitu, program hanya akan melanjutkan pencarian jika input sudah valid.

---

## Link YouTube

[]
