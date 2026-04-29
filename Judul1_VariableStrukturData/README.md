# Tugas Akhir Percobaan 1

## Judul Program
Sistem Watchlist Anime Menggunakan Single Linked List

## Deskripsi Singkat
Program ini digunakan untuk mengelola daftar anime yang ingin ditonton (watchlist). Pengguna dapat menambahkan anime, menampilkan daftar anime, serta menghapus anime pertama ketika sudah ditonton.

Struktur data yang digunakan adalah **Single Linked List**, di mana setiap anime disimpan dalam bentuk node yang saling terhubung menggunakan pointer `next`. Linked List dipilih karena data bersifat dinamis dan operasi penghapusan di bagian depan (First In First Out) dapat dilakukan dengan efisien tanpa perlu menggeser elemen lain.

---

## Source Code

<img width="1014" height="2848" alt="code" src="https://github.com/user-attachments/assets/b196dc96-17b9-4a89-8166-724774b16ed7" />

### Penjelasan Kode

#### 1. Class Node
```python
class Node:
    def __init__(self, judul):
        self.judul = judul
        self.next = None
```
Class ini digunakan untuk membuat node yang menyimpan judul anime dan pointer ke node berikutnya.

#### 2. Class Watchlist
```python
class Watchlist:
    def __init__(self):
        self.head = None
```
`head` digunakan untuk menunjuk node pertama dalam linked list.

#### 3. Tambah Anime
```python
def tambah(self, judul):
```
Fungsi ini menambahkan anime ke akhir linked list. Jika kosong, node menjadi head. Jika tidak, node ditambahkan di akhir.

#### 4. Tampilkan Data
```python
def tampil(self):
```
Fungsi ini melakukan traversal dari head sampai akhir dan menampilkan semua anime.

#### 5. Hapus Anime Pertama/Depan
```python
def hapus_depan(self):
    self.head = self.head.next
```
Fungsi ini menghapus node pertama dengan memindahkan pointer head ke node berikutnya.

#### 6. Main Program
Program menggunakan perulangan `while True` untuk menampilkan menu dan menjalankan fungsi sesuai pilihan user.

---

## Output Program

<img width="259" height="139" alt="Screenshot 2026-04-29 205733" src="https://github.com/user-attachments/assets/1e593b86-cee1-4699-bfde-825084a120a7" />
<img width="281" height="363" alt="Screenshot 2026-04-29 205833" src="https://github.com/user-attachments/assets/8f2050ad-ffee-417e-a4f2-524303fc45cf" />
<img width="247" height="184" alt="Screenshot 2026-04-29 205850" src="https://github.com/user-attachments/assets/ee548982-29a0-463c-aa12-f00a04cb44cb" />
<img width="288" height="308" alt="Screenshot 2026-04-29 210003" src="https://github.com/user-attachments/assets/eec17307-6395-49bf-bd9f-d0daa29f2e3f" />
<img width="266" height="308" alt="Screenshot 2026-04-29 210355" src="https://github.com/user-attachments/assets/48cb669c-08ef-44e1-9123-7c9411e2fd00" />
<img width="525" height="157" alt="Screenshot 2026-04-29 210331" src="https://github.com/user-attachments/assets/72170111-2944-442c-aca1-0a345038cdc8" />


### Penjelasan Output

Pada saat program dijalankan, program akan menampilkan menu utama yang berisi beberapa pilihan, yaitu menambahkan anime, menampilkan watchlist, menonton anime pertama, dan keluar dari program. Menu ini akan terus muncul selama pengguna belum memilih menu keluar.

Ketika pengguna memilih menu **1. Tambah Anime**, program meminta input judul anime. Setelah judul dimasukkan, program akan membuat node baru yang berisi judul anime tersebut. Jika watchlist masih kosong, node tersebut akan menjadi `head`. Jika watchlist sudah berisi data, node baru akan disambungkan ke bagian akhir linked list. Setelah proses berhasil, program menampilkan pesan bahwa anime berhasil ditambahkan.

Ketika pengguna memilih menu **2. Tampilkan**, program akan menampilkan seluruh anime yang sudah dimasukkan ke dalam watchlist. Data ditampilkan berdasarkan urutan node dari `head` sampai node terakhir. Hal ini membuktikan bahwa proses traversal pada linked list berjalan dengan benar.

Ketika pengguna memilih menu **3. Tonton Anime Pertama**, program akan menghapus anime yang berada di posisi paling depan. Anime pertama dianggap sebagai anime yang sudah ditonton. Setelah itu, pointer `head` dipindahkan ke node berikutnya. Dengan demikian, data pertama berhasil dihapus tanpa menggeser data lainnya.

Ketika pengguna memilih menu **4. Keluar**, program akan berhenti berjalan. Jika pengguna memasukkan pilihan selain menu yang tersedia, program tidak langsung berhenti, tetapi kembali menampilkan menu agar pengguna dapat memilih ulang.

Berdasarkan output yang ditampilkan, program berhasil menjalankan konsep Single Linked List, yaitu menambahkan data, menampilkan data , dan menghapus data dari bagian depan menggunakan perubahan pointer `head`.
Output menunjukkan bahwa linked list berjalan dengan benar dan data dapat dimanipulasi tanpa error.

---

## Link YouTube

[https://youtu.be/DIa8c0LM9Po?si=sOtLYne6_YXoST3m]

---
