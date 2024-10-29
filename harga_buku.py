def harga_bayaran(jenisbuku,kuantiti):
    if jenisbuku == 1:
        potongan_harga = (6.00 * 0.1) * kuantiti
        harga = (6.00 * kuantiti) - potongan_harga
    elif jenisbuku == 2:
        potongan_harga = (7.50 * 0.08) * kuantiti
        harga = (7.50 * kuantiti) - potongan_harga
    else:
        potongan_harga = (8.90 * 0.05) * kuantiti
        harga = (8.90 * kuantiti) - potongan_harga
    return (potongan_harga,harga)

def main():
    print("Senarai belian buku:")
    print("1.Latihan Pasti A,Bahasa Melayu,Tingkatan 1")
    print("2.Latihan Pasti A,Bahasa Melayu,Tingkatan 2")
    print("3.Latihan Pasti A,Bahasa Melayu,Tingkatan 3")
    while True:
        jenisbuku = int(input("Masukkan jenis buku yang dibeli (1-3): "))
        if jenisbuku > 3 or jenisbuku < 1:
            print("Sila masukkan nombor 1 hingga 3 sahaja.")
        else:
            break  # Exit the loop if valid input is given
    kuantiti=int(input("Masukkan kuantiti buku yang dibeli:"))
    potongan_harga1,harga1 = harga_bayaran(jenisbuku,kuantiti)
    print("Potongan harga yang diperoleh ialah RM",potongan_harga1)
    print("Jumlah harga yang perlu dibayar ialah RM",harga1)
    
if __name__ == "__main__":
    main()
