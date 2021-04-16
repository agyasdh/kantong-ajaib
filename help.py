# procedure editItemAmount
# I.S. ...
# F.S. ...

def help():

    # KAMUS LOKAL
    # ...

    # ALGORITMA

    # [1] Cek role user
    # jika role user adalah Admin
    if auth["role"] == ... :
        # tampilkan semua command Admin dengan kegunaannya
        print("...")

    # jika role user adalah User
    elif auth["role"] == ... :
        # tampilkan semua command User dengan kegunaannya
        print("...")
    
    # jika user belum login
    else:
        # tampilkan semua command unregistered user dengan kegunaannya
        print("...")

    # [2] Kembali ke menu
    menu()