try:
    nama=str(input(print("Masukan nama file: ")))
    file=open(nama,"a")

    tulis=str(input(print("Data file yang mau ditambahkan: ")))
    file.write(tulis)

    while True:
        tanya=str(input(print("Mau lagi (y/n): ")))
        if tanya=="n":
            file.close()
            break
        tulis=str(input(print("Data file yang mau ditambahkan: ")))
        file.write(tulis)
except FileNotFoundError:
    print("File tidak ditemukan")

