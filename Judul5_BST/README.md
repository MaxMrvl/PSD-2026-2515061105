# Tugas Akhir Percobaan 5

## Judul Program

**Sistem Pencarian Level Monster Game Menggunakan Binary Search Tree**

---

## Deskripsi Singkat

Program ini dibuat untuk mengimplementasikan konsep **Binary Search Tree (BST)** pada contoh game, yaitu sistem pencarian level monster. Dalam game, monster biasanya memiliki level berbeda-beda. Level yang lebih kecil dapat dianggap sebagai monster yang mudah, sedangkan level yang lebih besar dapat dianggap sebagai monster yang sulit dilawan.

Data yang digunakan pada program ini berupa **integer**, yaitu level monster. Data level monster disimpan ke dalam BST agar bisa ditambahkan, dicari, ditampilkan secara terurut, dan dicari nilai paling rendah maupun paling tinggi.

---

## Source Code

<img width="1331" height="6479" alt="BSTMONSTER" src="https://github.com/user-attachments/assets/e3f03bb9-363a-4281-bc19-6a6bb81f84d6" />

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

<img width="413" height="267" alt="Screenshot 2026-05-26 205603" src="https://github.com/user-attachments/assets/0190af27-fd64-4a36-a0bd-5f752262b620" />

### Contoh Output Menambahkan Level Monster

<img width="391" height="307" alt="Screenshot 2026-05-26 205647" src="https://github.com/user-attachments/assets/7910f7be-6670-44b3-914e-3a84e9dd95d2" />

Pada output tersebut, pengguna memilih menu 1, sehingga program memanggil method insert(). Karena BST masih kosong, level monster 50 menjadi root.

---

### Contoh Output Menambahkan Beberapa Level Monster

<img width="390" height="915" alt="Screenshot 2026-05-26 205918" src="https://github.com/user-attachments/assets/a9da48d6-387a-4c4f-ad8a-af0b6d80e757" />

<img width="375" height="311" alt="Screenshot 2026-05-26 210019" src="https://github.com/user-attachments/assets/00302995-a930-4b46-aa6d-8c06400df1a3" />

Pada contoh tersebut, setiap menu 1 dijalankan, program memanggil method insert(). Level 30 masuk ke kiri 50, level 70 masuk ke kanan 50, level 20 masuk ke kiri 30, dan level 40 masuk ke kanan 30.

---

### Contoh Output Mencari Level Monster

<img width="331" height="311" alt="Screenshot 2026-05-26 210100" src="https://github.com/user-attachments/assets/e26adddc-fc9c-4211-b18a-d64db0ff6621" />

Pada output tersebut, pengguna memilih menu 2, sehingga program memanggil method search(). Karena level 20 sudah tersimpan dalam BST, program menampilkan bahwa data ditemukan.

---

### Contoh Output Menampilkan Level Terurut

<img width="379" height="285" alt="Screenshot 2026-05-26 210134" src="https://github.com/user-attachments/assets/63c9ff2c-6fb1-4d70-9ba1-6414d23a993f" />

Menu 3 memanggil method inorder(). Inorder menampilkan data dari nilai terkecil sampai terbesar.

---

### Contoh Output Preorder

<img width="371" height="274" alt="Screenshot 2026-05-26 210228" src="https://github.com/user-attachments/assets/a21fc5f9-5513-4b66-8026-d64ea27b8d9d" />

Menu 4 memanggil method preorder(). Preorder menampilkan data mulai dari root terlebih dahulu.

---

### Contoh Output Postorder

<img width="368" height="262" alt="Screenshot 2026-05-26 210300" src="https://github.com/user-attachments/assets/c3bcb3cf-2dae-4bbe-ba17-b5bc436a6ad8" />


Menu 5 memanggil method postorder(). Postorder menampilkan node anak terlebih dahulu, lalu root.

---

### Contoh Output Level Terendah dan Tertinggi

<img width="334" height="279" alt="Screenshot 2026-05-26 210318" src="https://github.com/user-attachments/assets/a4ffe5b5-fe82-448f-bedd-bfd3005fc37b" />

Menu 6 memanggil method find_min(). Nilai paling kecil pada BST berada di bagian paling kiri.

<img width="342" height="270" alt="Screenshot 2026-05-26 210330" src="https://github.com/user-attachments/assets/e374fb30-1d23-42a4-bc45-9ca91daf8ea1" />

Menu 7 memanggil method find_max(). Nilai paling besar pada BST berada di bagian paling kanan.

---

### Contoh Output Menghitung Jumlah Level Monster

<img width="353" height="273" alt="Screenshot 2026-05-26 210508" src="https://github.com/user-attachments/assets/07b3507f-71ab-4973-b2cb-9651e081b909" />


Menu 8 memanggil method count_nodes(). Program menghitung semua node yang tersimpan di dalam BST.

---

## Link YouTube

