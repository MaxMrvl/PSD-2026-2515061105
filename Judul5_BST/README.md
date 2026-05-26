# Tugas Akhir Percobaan 5

## Judul Program

**Sistem Penyimpanan Level Monster Game Menggunakan Binary Search Tree**

---

## Deskripsi Singkat

Program ini dibuat untuk mengimplementasikan konsep **Binary Search Tree (BST)** pada contoh game, yaitu sistem penyimpanan level monster. Dalam game, monster biasanya memiliki level berbeda-beda. Level yang lebih kecil dapat dianggap sebagai monster yang lebih mudah, sedangkan level yang lebih besar dapat dianggap sebagai monster yang lebih sulit.

Data yang digunakan pada program ini berupa **integer**, yaitu level monster. Data level monster disimpan ke dalam BST agar bisa ditambahkan, dicari, ditampilkan secara terurut, dan dicari nilai paling rendah maupun paling tinggi.

Aturan penyimpanan pada BST adalah nilai yang lebih kecil dari node utama akan masuk ke bagian kiri, sedangkan nilai yang lebih besar akan masuk ke bagian kanan.

---

## Source Code

> Tambahkan screenshot source code di bagian ini setelah file di-upload ke GitHub.

```html
<img width="1320" height="2337" alt="BST Level Monster Game" src="LINK_GAMBAR_SOURCE_CODE" />
```

---

## Penjelasan Kode

```python
class Node:
```

Class `Node` digunakan untuk membuat satu simpul pada Binary Search Tree.

```python
def __init__(self, key):
```

Constructor di Python, yaitu fungsi khusus yang otomatis dijalankan saat objek baru dibuat dari sebuah class. Constructor ini menerima parameter `key`. Pada program ini, `key` berisi level monster.

```python
self.key = key
```

Baris ini menyimpan level monster ke dalam node.

```python
self.left = None
self.right = None
```

`self.left` digunakan untuk menyimpan alamat node anak kiri. `self.right` digunakan untuk menyimpan alamat node anak kanan. Nilai awalnya `None` karena node baru belum memiliki anak.

---

```python
class BinarySearchTree:
```

Class ini digunakan untuk membuat struktur Binary Search Tree.

```python
def __init__(self):
    self.root = None
```

Baris tersebut membuat root dengan nilai awal `None`. Artinya, saat program pertama dijalankan, BST masih kosong.

---

```python
def insert_node(self, root, key):
```

Method ini digunakan untuk menambahkan level monster ke dalam BST.

```python
if root is None:
    return Node(key)
```

Jika posisi node masih kosong, program akan membuat node baru berisi level monster.

```python
if key < root.key:
    root.left = self.insert_node(root.left, key)
```

Jika level yang dimasukkan lebih kecil dari level pada root, data masuk ke bagian kiri.

```python
elif key > root.key:
    root.right = self.insert_node(root.right, key)
```

Jika level yang dimasukkan lebih besar dari level pada root, data masuk ke bagian kanan.

```python
return root
```

Root dikembalikan setelah proses penambahan data selesai.

---

```python
def insert(self, key):
    self.root = self.insert_node(self.root, key)
```

Method ini digunakan untuk memulai proses insert dari root utama.

---

```python
def search_node(self, root, key):
```

Method ini digunakan untuk mencari level monster di dalam BST.

```python
if root is None:
    return False
```

Jika root kosong, berarti level monster tidak ditemukan.

```python
if root.key == key:
    return True
```

Jika nilai root sama dengan level yang dicari, maka data ditemukan.

```python
if key < root.key:
    return self.search_node(root.left, key)
```

Jika level yang dicari lebih kecil dari root, pencarian dilanjutkan ke kiri.

```python
return self.search_node(root.right, key)
```

Jika level yang dicari lebih besar dari root, pencarian dilanjutkan ke kanan.

---

```python
def search(self, key):
    return self.search_node(self.root, key)
```

Method ini digunakan untuk memanggil pencarian mulai dari root utama.

---

```python
def inorder(self, root):
```

Method `inorder()` digunakan untuk menampilkan level monster dari nilai terkecil sampai terbesar.

```python
self.inorder(root.left)
print(root.key, end=" ")
self.inorder(root.right)
```

Urutan inorder adalah kiri, root, lalu kanan. Karena BST menyimpan nilai kecil di kiri dan nilai besar di kanan, hasil inorder akan tampil terurut.

---

```python
def preorder(self, root):
```

Method `preorder()` digunakan untuk menampilkan data dari root terlebih dahulu.

Urutannya adalah root, kiri, lalu kanan.

---

```python
def postorder(self, root):
```

Method `postorder()` digunakan untuk menampilkan data dari anak terlebih dahulu, lalu root.

Urutannya adalah kiri, kanan, lalu root.

---

```python
def find_min(self, root):
```

Method ini digunakan untuk mencari level monster paling rendah.

```python
current = root
while current.left is not None:
    current = current.left
```

Karena nilai paling kecil dalam BST berada di bagian paling kiri, program bergerak terus ke kiri sampai tidak ada node kiri lagi.

```python
return current.key
```

Nilai node paling kiri dikembalikan sebagai level monster terendah.

---

```python
def find_max(self, root):
```

Method ini digunakan untuk mencari level monster paling tinggi.

```python
current = root
while current.right is not None:
    current = current.right
```

Karena nilai paling besar dalam BST berada di bagian paling kanan, program bergerak terus ke kanan sampai tidak ada node kanan lagi.

```python
return current.key
```

Nilai node paling kanan dikembalikan sebagai level monster tertinggi.

---

```python
def count_nodes(self, root):
```

Method ini digunakan untuk menghitung jumlah level monster yang tersimpan.

```python
if root is None:
    return 0
```

Jika node kosong, jumlahnya dihitung 0.

```python
return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
```

Program menghitung node saat ini, lalu menambahkan jumlah node dari bagian kiri dan kanan.

---

```python
def input_level():
```

Fungsi ini digunakan untuk menerima input level monster dari pengguna dan juga agar input level tidak harus ditulis berulang kali di dalam menu.

```python
level = int(input("Masukkan level monster: "))
```

Input diubah menjadi integer karena level monster berupa angka.

```python
if level <= 0:
```

Kondisi ini digunakan untuk memastikan level monster lebih dari 0.

```python
return level
```

Jika input valid, level dikembalikan ke fungsi utama.

---

```python
def main():
```

Fungsi utama digunakan untuk menjalankan menu program.

Menu yang tersedia:

```text
1. Tambah level monster
2. Cari level monster
3. Tampilkan level monster terurut
4. Tampilkan preorder
5. Tampilkan postorder
6. Lihat level monster terendah
7. Lihat level monster tertinggi
8. Hitung jumlah level monster
9. Keluar
```

Menu 1 menggunakan insert(), menu 2 menggunakan search(), menu 3 menggunakan inorder(), menu 4 menggunakan preorder(), menu 5 menggunakan postorder(), menu 6 menggunakan find_min(), menu 7 menggunakan find_max(), dan menu 8 menggunakan count_nodes().

---

## Output Program

> Tambahkan screenshot output program di bagian ini setelah program dijalankan.

```html
<img width="790" height="226" alt="Output BST Level Monster Game" src="LINK_GAMBAR_OUTPUT" />
```

### Contoh Output Menambahkan Level Monster

```text
=== SISTEM LEVEL MONSTER GAME ===
1. Tambah level monster
2. Cari level monster
3. Tampilkan level monster terurut
4. Tampilkan preorder
5. Tampilkan postorder
6. Lihat level monster terendah
7. Lihat level monster tertinggi
8. Hitung jumlah level monster
9. Keluar
Pilih: 1
Masukkan level monster: 50
Level monster 50 berhasil ditambahkan.
```

Pada output tersebut, pengguna memilih menu 1, sehingga program memanggil method insert(). Karena BST masih kosong, level monster 50 menjadi root.

---

### Contoh Output Menambahkan Beberapa Level Monster

```text
Pilih: 1
Masukkan level monster: 30
Level monster 30 berhasil ditambahkan.

Pilih: 1
Masukkan level monster: 70
Level monster 70 berhasil ditambahkan.

Pilih: 1
Masukkan level monster: 20
Level monster 20 berhasil ditambahkan.

Pilih: 1
Masukkan level monster: 40
Level monster 40 berhasil ditambahkan.
```

Pada contoh tersebut, setiap menu 1 dijalankan, program memanggil method insert(). Level 30 masuk ke kiri 50, level 70 masuk ke kanan 50, level 20 masuk ke kiri 30, dan level 40 masuk ke kanan 30.

---

### Contoh Output Mencari Level Monster

```text
Pilih: 2
Masukkan level monster: 40
Level monster 40 ditemukan.
```

Pada output tersebut, pengguna memilih menu 2, sehingga program memanggil method search(). Karena level 40 sudah tersimpan dalam BST, program menampilkan bahwa data ditemukan.

---

### Contoh Output Menampilkan Level Terurut

```text
Pilih: 3
Level monster terurut: 20 30 40 50 70
```

Menu 3 memanggil method inorder(). Inorder menampilkan data dari nilai terkecil sampai terbesar.

---

### Contoh Output Preorder

```text
Pilih: 4
Preorder level monster: 50 30 20 40 70
```

Menu 4 memanggil method preorder(). Preorder menampilkan data mulai dari root terlebih dahulu.

---

### Contoh Output Postorder

```text
Pilih: 5
Postorder level monster: 20 40 30 70 50
```

Menu 5 memanggil method postorder(). Postorder menampilkan node anak terlebih dahulu, lalu root.

---

### Contoh Output Level Terendah dan Tertinggi

```text
Pilih: 6
Level monster terendah adalah 20.
```

Menu 6 memanggil method find_min(). Nilai paling kecil pada BST berada di bagian paling kiri.

```text
Pilih: 7
Level monster tertinggi adalah 70.
```

Menu 7 memanggil method find_max(). Nilai paling besar pada BST berada di bagian paling kanan.

---

### Contoh Output Menghitung Jumlah Level Monster

```text
Pilih: 8
Jumlah level monster yang tersimpan: 5
```

Menu 8 memanggil method count_nodes(). Program menghitung semua node yang tersimpan di dalam BST.

---

## Link YouTube

