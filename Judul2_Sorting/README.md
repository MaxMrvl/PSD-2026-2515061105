# Tugas Akhir Percobaan 2

## Judul Program

**Pengurutan Tingkat Kesulitan Monster Game Berdasarkan HP (Health Point) Menggunakan Selection Sort**

---

## Deskripsi Singkat

Program ini dibuat untuk mengurutkan tingkat kesulitan monster dalam sebuah game berdasarkan nilai HP atau Health Point. Monster dengan HP yang lebih kecil dianggap lebih mudah dikalahkan, sedangkan monster dengan HP yang lebih besar dianggap lebih sulit dikalahkan. Oleh karena itu, program ini mengurutkan data HP monster dari nilai terkecil sampai nilai terbesar.

Algoritma yang digunakan adalah **Selection Sort**. Selection Sort bekerja dengan cara mencari nilai terkecil dari kumpulan data, kemudian menempatkan nilai tersebut ke posisi paling depan. Proses ini dilakukan berulang sampai seluruh data tersusun secara terurut. Studi kasus ini tetap mengikuti konsep Percobaan II, yaitu memasukkan elemen array, melakukan sorting, dan menampilkan hasil sorting.

---

## Source Code

<img width="1320" height="2337" alt="Selection Sort " src="https://github.com/user-attachments/assets/fe6fa3c4-d45f-4c45-ba54-66a5341d8116" />

### Penjelasan Kode

#### 1. Fungsi `tukar(arr, i, j)`

```python
def tukar(arr, i, j):
```

Fungsi `tukar()` dibuat untuk menukar posisi dua data di dalam list. Pada program ini, data yang ditukar adalah HP monster.

```python
temp = arr[i]
```

Nilai pada indeks `i` disimpan sementara ke dalam variabel `temp` (temporary). Hal ini dilakukan agar nilai tersebut tidak hilang saat proses pertukaran.

```python
arr[i] = arr[j]
```

Nilai pada indeks `j` dipindahkan ke indeks `i`.

```python
arr[j] = temp
```

Nilai awal dari indeks `i` yang tadi disimpan di `temp` dipindahkan ke indeks `j`. Dengan tiga langkah ini, dua data HP monster berhasil ditukar.

---

#### 2. Fungsi `selection_sort(arr, n)`

```python
def selection_sort(arr, n):
```

Fungsi ini berisi algoritma Selection Sort. Parameter `arr` adalah list yang berisi data HP monster, sedangkan `n` adalah jumlah monster yang datanya akan diurutkan.

```python
for i in range(n - 1):
```

Perulangan ini digunakan untuk menentukan posisi yang akan diisi oleh nilai terkecil. Perulangan dilakukan dari indeks pertama sampai sebelum indeks terakhir.

```python
pos = i
```

Variabel `pos` (position) digunakan untuk menyimpan posisi nilai terkecil sementara. Pada awal perulangan, program menganggap nilai terkecil berada pada indeks `i`.

```python
for j in range(i + 1, n):
```

Perulangan kedua digunakan untuk mencari nilai yang lebih kecil dari nilai pada indeks `pos`. Pencarian dimulai dari elemen setelah indeks `i`.

```python
if arr[j] < arr[pos]:
```

Kondisi ini membandingkan HP monster pada indeks `j` dengan HP monster pada indeks `pos`. Jika HP pada indeks `j` lebih kecil, berarti ditemukan monster yang lebih mudah dikalahkan.

```python
pos = j
```

Jika ditemukan nilai yang lebih kecil, posisi nilai terkecil diperbarui menjadi indeks `j`.

```python
if pos != i:
```

Bagian ini mengecek apakah posisi nilai terkecil berubah atau tidak. Jika berubah, berarti perlu dilakukan pertukaran data.

```python
tukar(arr, i, pos)
```

Fungsi `tukar()` dipanggil untuk menukar data pada indeks `i` dengan data pada indeks `pos`. Setelah proses ini, HP monster paling kecil pada bagian yang belum terurut akan diletakkan di posisi depan.

---

#### 3. Fungsi `main()`

```python
def main():
```

Fungsi `main()` adalah fungsi utama yang menjalankan alur program.

```python
n = int(input("Masukkan jumlah monster: "))
```

Baris ini meminta pengguna memasukkan jumlah monster yang akan diurutkan. Input diubah menjadi integer karena digunakan sebagai batas perulangan.

```python
hp_monster = []
```

List `hp_monster` digunakan untuk menyimpan seluruh data HP monster yang dimasukkan pengguna.

```python
for i in range(n):
```

Perulangan ini digunakan agar pengguna dapat memasukkan HP monster sebanyak jumlah monster yang sudah ditentukan.

```python
hp = int(input(f"HP monster ke-{i + 1}: "))
```

Baris ini meminta pengguna memasukkan HP untuk monster ke-1, ke-2, dan seterusnya. Input diubah menjadi integer karena HP berupa angka.

```python
if hp <= 0:
```

Bagian ini digunakan untuk memastikan HP monster tidak bernilai nol atau negatif. Karena dalam game, monster seharusnya memiliki HP lebih dari 0.

```python
hp_monster.append(hp)
```

Jika input valid, nilai HP monster dimasukkan ke dalam list `hp_monster`.

```python
print(f"HP monster sebelum diurutkan: {hp_monster}")
```

Baris ini menampilkan data HP monster sebelum proses sorting dilakukan.

```python
selection_sort(hp_monster, n)
```

Baris ini memanggil fungsi `selection_sort()` untuk mengurutkan HP monster dari nilai terkecil sampai terbesar.

```python
for i in range(n):
    print(hp_monster[i], end=" ")
```

Bagian ini menampilkan hasil akhir setelah data selesai diurutkan. Data ditampilkan satu per satu menggunakan perulangan.

```python
if __name__ == "__main__":
    main()
```

Baris ini memastikan bahwa fungsi `main()` dijalankan ketika file Python dieksekusi secara langsung.

---

## Output Program

<img width="790" height="226" alt="Screenshot 2026-05-04 014426" src="https://github.com/user-attachments/assets/ac801ec3-cd7d-47a7-ab9a-9dc97efead3c" />

### Penjelasan Output

Pada awal program, pengguna diminta memasukkan jumlah monster yang akan diurutkan. Setelah itu, program meminta pengguna memasukkan HP atau Health Point dari masing-masing monster.

Contoh data yang dimasukkan adalah:

```text
10, 9999999, 2000, 5000, 345678
```

Sebelum proses sorting dilakukan, data masih berada pada urutan sesuai input pengguna:

```text
[10, 9999999, 2000, 5000, 345678]
```

Kemudian program menjalankan algoritma Selection Sort. Program mencari HP terkecil terlebih dahulu, yaitu `10`, lalu menempatkannya di posisi pertama. Setelah itu, program mencari HP terkecil berikutnya dari sisa data, yaitu `2000`, lalu menempatkannya di posisi kedua. Proses ini terus dilakukan sampai semua data selesai diurutkan.

Hasil akhir setelah diurutkan adalah:

```text
10 2000 5000 345678 9999999
```

### Penjelasan Output Jika Input Tidak Valid

Selain menampilkan hasil pengurutan data, program juga memiliki validasi input agar program tidak langsung error ketika pengguna memasukkan data yang salah.

#### 1. Input jumlah monster tidak valid

<img width="446" height="84" alt="Screenshot 2026-05-04 011132" src="https://github.com/user-attachments/assets/ceef473c-e584-447f-8578-800eecceac39" />

Pada contoh output di atas, pengguna memasukkan kata:

```text
lima
```
Padahal program meminta input berupa angka untuk jumlah monster.

Bagian kode yang menangani hal ini adalah:

```python
try:
    n = int(input("Masukkan jumlah monster: "))
except ValueError:

    print("Input tidak valid!")
    return
```
Kemudian program menampilkan pesan:
```text
Input tidak valid!
```
2. Input HP monster tidak valid
<img width="427" height="157" alt="Screenshot 2026-05-04 012934" src="https://github.com/user-attachments/assets/bfef9b82-6dc2-428b-92e9-9537e8a8e88e" />

Pada contoh output kedua, pengguna sudah memasukkan jumlah monster dengan benar, yaitu:
```text
5
```
Program meminta HP monster ke-1. Namun pengguna memasukkan kata:
```text
sepuluh
```
Karena program mengharapkan angka, maka input tersebut tidak bisa dikonversi ke tipe data integer. Akibatnya, program menampilkan pesan:
```text
Input tidak valid, silakan masukkan angka!
```
Program akan meminta pengguna mengisi ulang HP monster yang sama.

Contoh kondisi kedua terjadi saat pengguna memasukkan angka seperti:
```text
-1
```
Walaupun -1 adalah angka, nilai tersebut tetap dianggap tidak valid karena HP monster harus lebih dari 0. Dalam kondisi ini, program menampilkan pesan:
```text
HP monster harus lebih dari 0.
```
Lalu program kembali meminta input HP monster yang sama sampai pengguna memasukkan nilai yang benar.

Bagian kode yang menangani validasi ini adalah:
```python
while True:
    try:
        hp = int(input(f"HP monster ke-{i + 1}: "))

        if hp <= 0:
            print("HP monster harus lebih dari 0.")
            continue

        hp_monster.append(hp)
        break
    except ValueError:
        print("Input tidak valid, silakan masukkan angka!")
```
Perulangan `while True` digunakan agar program terus meminta input sampai pengguna memasukkan data yang benar. Pada bagian `int(input(...))`, program membaca input HP monster dari pengguna, lalu mencoba mengubahnya menjadi tipe data integer.

Jika pengguna memasukkan teks seperti `sepuluh`, maka input tersebut tidak bisa diubah menjadi integer dan akan menyebabkan `ValueError`. Kesalahan ini ditangani oleh bagian `except ValueError`, sehingga program tidak langsung berhenti, tetapi menampilkan pesan `Input tidak valid, silakan masukkan angka!`.

Jika pengguna memasukkan angka, program akan lanjut memeriksa kondisi `if hp <= 0`. Kondisi ini digunakan untuk memastikan bahwa HP monster harus lebih dari 0. Jika pengguna memasukkan angka seperti `0` atau `-1`, maka nilai tersebut dianggap tidak valid karena monster dalam game seharusnya memiliki HP positif. Program kemudian menampilkan pesan `HP monster harus lebih dari 0.` dan menjalankan `continue` agar kembali meminta input HP monster yang sama.

Apabila input yang dimasukkan sudah berupa angka dan nilainya lebih dari 0, maka data HP tersebut akan disimpan ke dalam list menggunakan `hp_monster.append(hp)`. Setelah data berhasil disimpan, perintah `break` dijalankan agar program keluar dari perulangan input HP monster tersebut dan lanjut meminta data untuk monster berikutnya.

---
## Link YouTube

[https://youtu.be/js2slwNe-U4?si=Yv-lmIk_RHgNMa9x]
