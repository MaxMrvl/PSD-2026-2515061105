class QueueArray:
    def __init__(self, max_size=100):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, x):
        if self.is_full():
            print("Antrian laundry penuh")
            return
        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
        self.q[self.rear_idx] = x
        print(f"Data laundry {x} berhasil masuk antrian")

    def dequeue(self):
        if self.is_empty():
            print("Antrian laundry kosong")
            return
        print(f"Data laundry {self.q[self.front_idx]} sedang diproses")
        self.q[self.front_idx] = None
        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("Antrian laundry kosong")
            return
        print(f"Data laundry paling depan: {self.q[self.front_idx]}")

    def display(self):
        if self.is_empty():
            print("Antrian laundry kosong")
            return
        print("Isi antrian laundry (depan ke belakang): ", end="")
        i = self.front_idx
        while True:
            print(self.q[i], end=" | ")
            if i == self.rear_idx:
                break
            i = (i + 1) % self.MAXN
        print()


def input_data_laundry():
    nama = input("Nama pelanggan: ")

    while True:
        try:
            berat = float(input("Berat laundry (kg): "))
            if berat <= 0:
                print("Berat laundry harus lebih dari 0 kg")
                continue
            return f"{nama} - {berat} kg"
        except ValueError:
            print("Input berat tidak valid")


def main():
    queue = QueueArray()
    pilih = 0
    while pilih != 5:
        print("\n=== SISTEM ANTRIAN LAUNDRY ===")
        print("1. Tambah laundry")
        print("2. Proses laundry")
        print("3. Lihat laundry paling depan")
        print("4. Tampilkan antrian")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid")
            continue
        if pilih == 1:
            data_laundry = input_data_laundry()
            queue.enqueue(data_laundry)
        elif pilih == 2:
            queue.dequeue()
        elif pilih == 3:
            queue.peek()
        elif pilih == 4:
            queue.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
