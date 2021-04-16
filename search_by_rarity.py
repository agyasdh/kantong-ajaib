# procedure searchByRarity
# I.S. ...
# F.S. ...

def searchByRarity():

    # KAMUS LOKAL
    # ...

    # ALGORITMA

    # [1] Cek apakah user telah login
    if auth["id"] != 0:
        
        # [2] Input
        rarity = ...

        # [3] Cari gadget
        # buat Array untuk menampung hasil pencarian
        result = []
        # iterasi data gadget
        for gadget in data["gadget"]:
            
            # [4] Jika rarity gadget sesuai pencarian
            if gadget["rarity"] == ...:

                # [5] Append gadget ke hasil pencarian
                result.append(...)
        
        # [4] Tampilkan hasil pencarian
        print()
        print("Hasil pencarian:")
        print()
        # jika hasil pencarian tidak ada
        if len(result) == ... :
            # tampilkan pesan feedback "Tidak ada gadget yang ditemukan"
            print("...")
        # jika hasil pencarian ada
        else:
            # iterasi hasil pencarian
            for gadget in result:
                print("Nama            :{}".format(gadget[...]))
                print("Deskripsi       :{}".format(gadget[...]))
                print("Jumlah          :{}".format(gadget[...]))
                print("Rarity          :{}".format(gadget[...]))
                print("Tahun Ditemukan :{}".format(gadget[...]))
                print()
    
    # user belum login
    else:
        # tampilkan pesan error "Silakan login terlebih dahulu !"
        print("...")
    
    # kembali ke menu
    menu()

# CATATAN : Hint dapat dihapus jika coding fungsi/prosedur telah selesai dan lolos testing