try:
    file=open("d:/anyfiles.txt")
    print(file.read())
except FileNotFoundError:
    print("File tidak ditemukan")
