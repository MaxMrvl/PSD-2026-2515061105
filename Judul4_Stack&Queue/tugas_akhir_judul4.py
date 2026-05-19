class QueueArray:
    def __init__(self, max_size=20):
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
            return False

        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN

        self.q[self.rear_idx] = x
        return True

    def dequeue(self):
        if self.is_empty():
            print("Antrian laundry kosong")
            return None

        data = self.q[self.front_idx]
        self.q[self.front_idx] = None

        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.q[self.front_idx]

    def display(self):
        if self.is_empty():
            print("Antrian laundry kosong")
            return

        print("Daftar antrian laundry dari depan ke belakang:")
        i = self.front_idx
        nomor = 1

        while True:
            print(f"{nomor}. {self.q[i]}")

            if i == self.rear_idx:
                break

            i = (i + 1) % self.MAXN
            nomor += 1


def input_laundry():
    nama = input("Masukkan nama pelanggan: ")

    while True:
        try:
            berat = float(input("Masukkan berat laundry (kg): "))

            if berat <= 0:
                print("Berat laundry harus lebih dari 0 kg.")
                continue

            break
        except ValueError:
            print("Input berat harus berupa angka!")

    jenis_layanan = input("Masukkan jenis layanan (Cuci / Setrika / Cuci Setrika): ")
    return f"{nama} - {berat} kg - {jenis_layanan}"


def main():
    antrian_laundry = QueueArray()
    pilihan = 0

    while pilihan != 5:
        print("\n=== Sistem Antrian Laundry ===")
        print("1. Tambah pelanggan ke antrian")
        print("2. Proses laundry paling depan")
        print("3. Lihat pelanggan berikutnya")
        print("4. Tampilkan semua antrian")
        print("5. Keluar")

        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")
            continue

        if pilihan == 1:
            data_laundry = input_laundry()

            if antrian_laundry.enqueue(data_laundry):
                print("Data laundry berhasil masuk ke antrian.")

        elif pilihan == 2:
            data_laundry = antrian_laundry.dequeue()

            if data_laundry is not None:
                print(f"Data laundry sedang diproses: {data_laundry}")

        elif pilihan == 3:
            data_laundry = antrian_laundry.peek()

            if data_laundry is None:
                print("Belum ada pelanggan dalam antrian.")
            else:
                print(f"Pelanggan berikutnya yang akan diproses: {data_laundry}")

        elif pilihan == 4:
            antrian_laundry.display()

        elif pilihan == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
