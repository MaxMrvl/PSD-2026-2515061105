class Node:
    def __init__(self, judul):
        self.judul = judul
        self.next = None

class Watchlist:
    def __init__(self):
        self.head = None

    def tambah(self, judul):
        node_baru = Node(judul)

        if self.head is None:
            self.head = node_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru

        print(f"{judul} ditambahkan.")

    def tampil(self):
        if self.head is None:
            print("Watchlist kosong.")
            return

        current = self.head
        no = 1

        while current:
            print(f"{no}. {current.judul}")
            current = current.next
            no += 1

    def hapus_depan(self):
        if self.head is None:
            print("Tidak ada anime.")
            return

        print(f"{self.head.judul} sudah ditonton.")
        self.head = self.head.next


def main():
    wl = Watchlist()

    while True:
        print("\n1. Tambah Anime")
        print("2. Tampilkan")
        print("3. Tonton Anime Pertama")
        print("4. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            judul = input("Judul: ")
            wl.tambah(judul)

        elif pilih == "2":
            wl.tampil()

        elif pilih == "3":
            wl.hapus_depan()

        elif pilih == "4":
            break


if __name__ == "__main__":
    main()