def harga_bayaran(jenis_buku, kuantiti):
    if jenis_buku == 1:
        harga_seunit = 6.00
        diskaun = 10 / 100
    elif jenis_buku == 2:
        harga_seunit = 7.50
        diskaun = 8 / 100
    elif jenis_buku == 3:
        harga_seunit = 8.90
        diskaun = 5 / 100
    else:
        return None, None # Jika jenis buku tidak sah
        
    harga_tanpa_diskaun = harga_seunit * kuantiti
    potongan_harga = harga_tanpa_diskaun * diskaun
    harga_selepas_potongan = harga_tanpa_diskaun - potongan_harga
        
    return potongan_harga, harga_selepas_potongan

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
