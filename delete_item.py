# procedure deleteItem
# I.S. ...
# F.S. ...

def deleteItem():

    # KAMUS LOKAL
    # ...
    global data

    # [1] Cek apakah role user adalah Admin
    # gunakan global variable auth
    if auth["role"] == ... :

        # [2] Input ID
        identifier = ...
        
        # [3] Validasi ID
        # jika ID tidak valid
        # gunakan fungsi isItemExist()
        if ... :
            # tampilkan pesan error "Tidak ada item dengan ID tersebut."
            print("...")

        # ID valid
        else:
            # [4] Konfirmasi penghapusan item
            # ambil itemType untuk mengambil nama item dari database
            itemType = "gadget" if identifier[0] == ... else ...
            # ambil nama item
            for item in data[itemType]:
                # jika ID item cocok
                if item["id"] == ...:
                    # simpan nama item di variable itemName
                    itemName = ...
            # input konfirmasi
            invalid = True
            while invalid:
                choice = input("Apakah Anda yakin ingin menghapus {} (Y/N)? ".format(...)) 
                # jika input konfirmasi valid
                if choice in "YyNn":
                    invalid = ...
                # jika tidak valid
                else:
                    # tampilkan pesan error "Masukan tidak valid !"
                    print(...)
            
            # [5] Hapus item jika dikonfirmasi
            if choice in "Yy":
                # cari index item yang akan dihapus
                for index in range(len(data[itemType])):
                    # jika ID item cocok
                    if data[itemType][...][...] == ... :
                        # hapus item berdasarkan index
                        data[itemType].pop(...)

    # jika role user adalah User
    elif auth["role"] == ... :
        # tampilkan pesan error "Hanya Admin yang dapat menggunakan perintah ini !"
        print("...")
    
    # jika user belum login
    else:
        # Tampilkan pesan error "Silakan login terlebih dahulu !"
        print("...")
    
    # kembali ke menu
    menu()