def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selection_sort(arr, n):
    for i in range(n - 1):
        pos = i

        for j in range(i + 1, n):
            if arr[j] < arr[pos]:
                pos = j

        if pos != i:
            tukar(arr, i, pos)


def main():
    try:
        n = int(input("Masukkan jumlah monster: "))
    except ValueError:
        print("Input tidak valid!")
        return
    hp_monster = []
    print("Masukkan HP (Health Point) setiap monster: ")
    for i in range(n):
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

    print(f"HP monster sebelum diurutkan: {hp_monster}")

    selection_sort(hp_monster, n)

    print("HP monster setelah diurutkan dari termudah ke tersulit:", end=" ")
    for i in range(n):
        print(hp_monster[i], end=" ")
    print()


if __name__ == "__main__":
    main()
