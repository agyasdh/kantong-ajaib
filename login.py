# procedure login
# I.S. ...
# F.S. ...

def login():

    # KAMUS LOKAL
    # ...
    global auth

    # ALGORITMA

    # [1] Input
    username = input("Masukkan username: ")
    password = ...

    # [2] Validasi input
    # Jika username kosong
    if username == ... :
        # tampilkan pesan error "Masukkan username !"
        # dan kembali lagi ke login
        print("...")
        login()
    
    # Jika password kosong
    elif password == ... :
        # tampilkan pesan error "Masukkan password !"
        # dan kembali lagi ke login
        print("...")
        login()
    
    # Input valid
    else:
        # [3] Cocokkan input dengan data user pada database
        # iterasi data user
        for user in data["user"]:
            # jika input dengan data sama
            # gunakan fungsi hash128() untuk mencocokkan password
            if user["username"] == ... and user["password"] == hash128(...):

                # [4] Update autentikasi user dan kembali ke menu
                auth["id"] = user["id"]
                auth["role"] = user["role"]
                menu()
        
        # [5] Data user tidak ditemukan
        # tampilkan pesan error "Username belum terdaftar atau password salah !"
        # dan kembali ke menu
        print(...)
        menu()

# CATATAN : Hint dapat dihapus jika coding fungsi/prosedur telah selesai dan lolos testing