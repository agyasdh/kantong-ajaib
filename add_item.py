# procedure addItem
# I.S. ...
# F.S. ...

def addItem():

    # KAMUS LOKAL
    # ...
    global data
    
    # [1] Cek apakah role user adalah Admin
    # gunakan global variable auth
    if auth["role"] == ... :

        # [2] Input ID
        identifier = ...
        
        # [3] Validasi ID
        # jika id invalid (tidak diawali huruf G atau C)
        # TIPS : (a == "x" or a == "y") dapat disederhanakan menjadi (a in "xy")
        if not(identifier[0] == ... or ...):
            # tampilkan pesan error "Gagal menambahkan item karena ID tidak valid."
            # dan kembali ke menu
            print("...")
            menu()

        # jika id telah digunakan
        # gunakan fungsi isItemExist()  ((lihat di bawah))
        elif ... :
            # tampilkan pesan error "Gagal menambahkan item karena ID sudah ada."
            # dan kembali ke menu
            print("...")
            menu()
        
        # [4] Input nama, deskripsi, jumlah
        name = ...
        description = ...
        count = ...

        # [5] Validasi jumlah
        # jika jumlah < 0
        if count < 0:
            # tampilkan pesan error "Jumlah item tidak valid !"
            # dan kembali ke menu
            print("...")
            menu()
        
        # [6] Input rarity
        rarity = ...

        # [7] Validasi rarity
        # jika rarity bukan C, B, A, atau S
        if not (rarity in "CBAS"):
            # tampilkan pesan error "Input rarity tidak valid !"
            # dan kembali ke menu
            print("...")
            menu()

        # [8] Update temporary database
        # jika item adalah gadget (id diawali G)
        if ... :
            # input tambahan : tahun ditemukan
            year = ...

            # [8a] Validasi year
            # jika year < 0
            if ... :
                # tampilkan pesan error "Tahun ditemukan tidak valid !"
                print("...")
            
            # jika year >= 0 (valid)
            else:
                # [9] Append gadget ke data gadget
                # buat gadget ke dalam sebuah dictionary
                gadget = {
                    "id" : ...,
                    "name" : ...,
                    "description" : ...,
                    "count" : ...,
                    "rarity" : ...,
                    "year" : ...
                }
                data["gadget"].append(...)

        # jika item adalah consumable
        else:
            # [9] Append consumable ke data consumable
            # buat consumable ke dalam sebuah dictionary
            consumable = {
                "id" : ...,
                "name" : ...,
                "description" : ...,
                "count" : ...,
                "rarity" : ...
            }
            data["consumable"].append(...)
        
        # [10] Tampilkan pesan sukses "Item telah berhasil ditambahkan ke database."
        # dan kembali ke menu
        print("...")
        menu()

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

# function isItemExists(identifier: str) -> bool
# ... tulis spesifikasi di sini ...
def isItemExist(identifier):
    
    # KAMUS LOKAL
    # ...

    # ALGORITMA

    # [1] Cek apakah tipe item gadget atau consumable
    # simpan ke variabel itemType
    # jika gadget
    if identifier[0] == ... :
        itemType = "gadget"
    else:
        itemType = ...
    
    # [2] Cari ID pada data itemType (gadget/consumable)
    # iterasi data
    for item in data[itemType]:
        # jika ID sama, return true
        if item["id"] == ... :
            return ...
    # tidak ada item dengan ID yang sama
    return ...
    
# CATATAN : Hint dapat dihapus jika coding fungsi/prosedur telah selesai dan lolos testing