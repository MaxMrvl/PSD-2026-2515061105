class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)
        return root

    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def search_node(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        if key < root.key:
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)

    def search(self, key):
        return self.search_node(self.root, key)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root is not None:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    def find_min(self, root):
        if root is None:
            return None
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def find_max(self, root):
        if root is None:
            return None
        current = root
        while current.right is not None:
            current = current.right
        return current.key

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)


def input_level():
    while True:
        try:
            level = int(input("Masukkan level monster: "))
            if level <= 0:
                print("Level monster harus lebih dari 0.")
                continue
            return level
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")


def main():
    bst = BinarySearchTree()
    pilihan = 0
    while pilihan != 9:
        print("\n=== SISTEM LEVEL MONSTER GAME ===")
        print("1. Tambah level monster")
        print("2. Cari level monster")
        print("3. Tampilkan level monster terurut")
        print("4. Tampilkan preorder")
        print("5. Tampilkan postorder")
        print("6. Lihat level monster terendah")
        print("7. Lihat level monster tertinggi")
        print("8. Hitung jumlah level monster")
        print("9. Keluar")
        try:
            pilihan = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid")
            continue
        if pilihan == 1:
            level = input_level()
            bst.insert(level)
            print(f"Level monster {level} berhasil ditambahkan.")
        elif pilihan == 2:
            level = input_level()
            if bst.search(level):
                print(f"Level monster {level} ditemukan.")
            else:
                print(f"Level monster {level} tidak ditemukan.")
        elif pilihan == 3:
            print("Level monster terurut:", end=" ")
            bst.inorder(bst.root)
            print()
        elif pilihan == 4:
            print("Preorder level monster:", end=" ")
            bst.preorder(bst.root)
            print()
        elif pilihan == 5:
            print("Postorder level monster:", end=" ")
            bst.postorder(bst.root)
            print()
        elif pilihan == 6:
            level = bst.find_min(bst.root)
            if level is None:
                print("Data level monster masih kosong.")
            else:
                print(f"Level monster terendah adalah {level}.")
        elif pilihan == 7:
            level = bst.find_max(bst.root)
            if level is None:
                print("Data level monster masih kosong.")
            else:
                print(f"Level monster tertinggi adalah {level}.")
        elif pilihan == 8:
            jumlah = bst.count_nodes(bst.root)
            print(f"Jumlah level monster yang tersimpan: {jumlah}")
        elif pilihan == 9:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()