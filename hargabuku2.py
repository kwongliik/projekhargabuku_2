def harga_bayaran(jenisbuku, kuantiti):
    # Senarai harga buku
    harga_buku = [6.00, 7.50, 8.90]  # Harga untuk buku 1, 2, dan 3
    potongan = 0  # Inisialisasi potongan

    # Mengira harga asal
    harga_asal = harga_buku[jenisbuku - 1] * kuantiti

    # Mengira potongan harga berdasarkan jenis buku
    if jenisbuku == 1:
        potongan = harga_asal * 0.10  # 10% potongan untuk Tingkatan 1
    elif jenisbuku == 2:
        potongan = harga_asal * 0.08  # 8% potongan untuk Tingkatan 2
    elif jenisbuku == 3:
        potongan = harga_asal * 0.05  # 5% potongan untuk Tingkatan 3

    # Mengira jumlah harga setelah potongan
    harga_selepas_potongan = harga_asal - potongan
    
    return potongan, harga_selepas_potongan

def main():
    print("Senarai belian buku:")
    print("1. Latihan Pasti A, Bahasa Melayu, Tingkatan 1 (RM 6.00, Diskaun 10%)")
    print("2. Latihan Pasti A, Bahasa Melayu, Tingkatan 2 (RM 7.50, Diskaun 8%)")
    print("3. Latihan Pasti A, Bahasa Melayu, Tingkatan 3 (RM 8.90, Diskaun 5%)")
    
    while True:
        jenisbuku = int(input("Masukkan jenis buku yang dibeli (1-3): "))
        if jenisbuku > 3 or jenisbuku < 1:
            print("Sila masukkan nombor 1 hingga 3 sahaja.")
        else:
            break  # Exit the loop if valid input is given

    kuantiti = int(input("Masukkan kuantiti buku yang dibeli: "))
    potongan_harga, harga_total = harga_bayaran(jenisbuku, kuantiti)
    
    print("Potongan harga yang diperoleh ialah RM", round(potongan_harga, 2))
    print("Jumlah harga yang perlu dibayar ialah RM", round(harga_total, 2))

if __name__ == "__main__":
    main()
