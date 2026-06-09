class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]
        return None

    def remove_key(self, key):
        entry = self.search(key)
        if entry is None:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\nIsi Hash Table Anime:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")
            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")
            else:
                print(f"({self.table[i].key}, {self.table[i].value})")


def input_kode_anime():
    while True:
        try:
            kode = int(input("Masukkan kode anime: "))
            if kode <= 0:
                print("Kode anime harus lebih dari 0")
                continue
            return kode
        except ValueError:
            print("Input kode tidak valid")


def main():
    hashmap = HashMapOpenAddressing()
    pilih = 0
    while pilih != 5:
        print("\n=== SISTEM DATA ANIME FAVORIT ===")
        print("1. Tambah data anime")
        print("2. Cari data anime")
        print("3. Hapus data anime")
        print("4. Tampilkan hash table")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid")
            continue
        if pilih == 1:
            kode = input_kode_anime()
            judul = input("Masukkan judul anime: ")
            if hashmap.insert(kode, judul):
                print(f"Anime {judul} dengan kode {kode} berhasil ditambahkan")
            else:
                print("Hash table penuh, data anime gagal ditambahkan")
        elif pilih == 2:
            kode = input_kode_anime()
            hasil = hashmap.search(kode)
            if hasil is not None:
                print(f"Kode {kode} ditemukan, judul anime: {hasil.value}")
            else:
                print(f"Kode {kode} tidak ditemukan")
        elif pilih == 3:
            kode = input_kode_anime()
            if hashmap.remove_key(kode):
                print(f"Anime dengan kode {kode} berhasil dihapus")
            else:
                print(f"Anime dengan kode {kode} tidak ditemukan")
        elif pilih == 4:
            hashmap.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()