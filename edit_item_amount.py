# procedure editItemAmount
# I.S. ...
# F.S. ...

def editItemAmount():

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
            # tampilkan pesan error "Tidak ada item dengan ID tersebut!"
            print("...")

        # ID valid
        else:

            # [4] Input jumlah
            modifier = ...
            
            # [5] Validasi jumlah
            # gunakan fungsi isInt()
            # jika jumlah bukan integer
            if ... :
                # tampilkan pesan kesalahan "Input jumlah tidak valid !"
                print("...")
            else:
                # cast modifier ke integer
                modifier = int(modifier)

                # [6] Ubah jumlah item
                # ambil itemType untuk mengambil nama item dari database
                itemType = "gadget" if identifier[0] == ... else ...
                # cari index item yang akan dihapus
                for index in range(len(data[itemType])):
                    # jika ID item cocok
                    if data[itemType][...][...] == ... :
                        # ambil jumlah item
                        amount = data[itemType][...][...]
                        
                        # [7] Ubah jumlah item berdasarkan input (+/-)
                        # jika ditambah
                        if modifier >= 0:
                            data[itemType][...][...] += ...
                        # jika dikurang
                        else:
                            # jika modifier > jumlah sekarang (invalid)
                            if amount < modifier:
                                # tampilkan pesan kesalahan "<modifier> <nama> gagal dibuang karena stok kurang. Stok sekarang : <amount> (< <modifier>)"
                                print("...")
                            # jika modifier < jumlah sekarang (valid)
                            else:
                                data[itemType][...][...] -= ...
                                
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

# function isInt(string: str) -> bool
def isInt(string):

    # KAMUS LOKAL

    # ALGORITMA
    try:
        string = int(string)
        return True
    except:
        return False