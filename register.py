# procedure register
# I.S. ...
# F.S. ...

def register():
    
    # KAMUS LOKAL
    # ...
    global data

    # ALGORITMA
    
    # [1] Cek apakah role user saat ini adalah Admin
    # gunakan global variable auth
    if auth["role"] == ... :

        # [2] Input
        name = input("Masukkan nama: ")
        username = ...
        password = ...
        address = ...

        # [3] Validasi input
        # Jika username kosong
        if username == ... :
            # Tampilkan pesan error "Username tidak boleh kosong !"
            print("...")

        # Jika username telah terdaftar
        # gunakan fungsi isRegistered()
        elif ... :
            # Tampilkan pesan error "Username telah digunakan oleh pengguna lain !"
            print("...")
        
        # Jika password kosong
        elif password == ... :
            # Tampilkan pesan error "Password tidak boleh kosong !"
            print("...")

        # Jika nama kosong
        elif name == ... :
            # Tampilkan pesan error "Nama tidak boleh kosong !"
            print("...")
        
        # Jika nama tidak alphabet
        # gunakan metode .isalpha()
        elif not(...):
            # Tampilkan pesan error "Nama tidak valid !"
            print("...")

        # Semua input valid
        else:
            # [4] Kapitalisasi nama
            # gunakan metode .capitalize() pada setiap kata pada nama
            # pecah nama menjadi Array, gunakan fungsi explode() (lihat explode.py)
            nameArray = explode(..., " ")
            capitalizedNameArray = []
            # iterasi Array nama
            for nameString in nameArray:
                # jadikan huruf pertama kapital dan huruf lainnya non-kapital
                capilatizedNameString = nameString.capitalize()
                # append capilatizedNameString ke capitalizedNameArray
                capitalizedNameArray.append(...)
            # gabungkan nama yang telah dikapitalisasi, gunakan metode .join()
            capitalizedName = " ".join(...)

            # [5] Append nama baru ke temporary database
            # gunakan global variable data
            # password dihash terlebih dahulu
            newUserID = len(data["user"]) + 1
            newUserdata = {
                "id" : newUserID,
                "username" : ...,
                "name" : ...,
                "address" : ...,
                "password" : hash128(...),
                "role" : "User",
            }
            data["user"].append(...)

            # [6] Tampilkan pesan sukses "User <user> telah berhasil register ke dalam Kantong Ajaib."
            # gunakan metode .format()
            print("...")

    # Jika role user adalah User
    elif auth["role"] == ... :
        # Tampilkan pesan error "Hanya Admin yang dapat menggunakan perintah ini !"
        print("...")
    
    # Jika user belum login
    else:
        # Tampilkan pesan error "Silakan login terlebih dahulu !"
        print("...")
    
    # kembali ke menu
    menu()

# function isRegistered(username: str) -> bool
# return True jika username telah terdaftar, False jika tidak
def isRegistered(username):
    
    # KAMUS LOKAL
    # ...

    # ALGORITMA

    # [1] Iterasi setiap user yang terdaftar pada user data
    for user in data["user"]:
        
        # [2] Return true jika username terdaftar
        if user["username"] == ...:
            return ...
    
    # [3] Di blok ini, iterasi telah selesai dan tidak ditemukan user
    #     dengan username yang sama. Return false
    return ...


# CATATAN : Hint dapat dihapus jika coding fungsi/prosedur telah selesai dan lolos testing