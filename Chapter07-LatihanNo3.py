print("---------------------------")
print("PROGRAM HITUNG RATA-RATA")
print("---------------------------")
try:
    hitung=[]
    i=0
    while True:    
        print(("Masukan bilangan bulat: "),end="")
        a=int(input())
        hitung=hitung+[a]
        i=i+1
        print(("Lagi? (y/n): "),end="")
        tanya=str(input())
        if tanya=="n":
            break
        elif tanya!="y":
            print("Input Salah")

    sum=0
    for i in range(len(hitung)):
        sum=sum+hitung[i]
        
    ratarata=sum/len(hitung)
    print("Rata-ratanya adalah: ", ratarata)
except ValueError:
    next
