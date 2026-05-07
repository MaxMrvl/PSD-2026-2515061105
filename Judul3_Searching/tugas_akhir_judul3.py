def sequential_search_sentinel(data, n, target):
    data.append(target)
    i = 0
    while data[i] != target:
        i += 1
    data.pop()
    if i < n:
        return True, i
    else:
        return False, -1


def main():
    kursi_terpesan = [3, 7, 10, 12, 18, 21, 25, 30, 33, 40]
    n = len(kursi_terpesan)

    print("=== Sistem Pencarian Nomor Kursi Bioskop ===")
    print(f"Data kursi yang sudah dipesan: {kursi_terpesan}")
    print("Nomor kursi tersedia dari 1 sampai 40")

    while True:
        try:
            target = int(input("Masukkan nomor kursi yang ingin dicek: "))

            if target < 1 or target > 40:
                print("Nomor kursi tidak valid. Pilih nomor kursi dari 1 sampai 40.")
                continue

            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")

    found, index = sequential_search_sentinel(kursi_terpesan, n, target)

    if found:
        print(f"Kursi nomor {target} sudah dipesan.")
        print(f"Data ditemukan pada indeks ke-{index}.")
    else:
        print(f"Kursi nomor {target} masih tersedia.")


if __name__ == "__main__":
    main()
