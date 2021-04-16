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
            print("...")

        # jika id telah digunakan
        # gunakan fungsi isItemExist()
        elif ... :
            # tampilkan pesan error "Gagal menambahkan item karena ID sudah ada."
            print("...")
        
        # ID valid
        else:

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
            
            # jika jumlah >= 0 (valid)
            else:
            
                # [6] Input rarity
                rarity = ...

                # [7] Validasi rarity
                # jika rarity bukan C, B, A, atau S
                if not (rarity in "CBAS"):
                    # tampilkan pesan error "Input rarity tidak valid !"
                    print("...")
                else:
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
                                "amount" : ...,
                                "rarity" : ...,
                                "year" : ...
                            }
                            data["gadget"].append(...)
                            # Tampilkan pesan sukses "Item telah berhasil ditambahkan ke database."
                            print("...")

                    # jika item adalah consumable
                    else:
                        # [9] Append consumable ke data consumable
                        # buat consumable ke dalam sebuah dictionary
                        consumable = {
                            "id" : ...,
                            "name" : ...,
                            "description" : ...,
                            "amount" : ...,
                            "rarity" : ...
                        }
                        data["consumable"].append(...)
                        # Tampilkan pesan sukses "Item telah berhasil ditambahkan ke database."
                        print("...")

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
