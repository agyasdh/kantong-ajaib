# Panduan

## Panduan Coder

### Melengkapi code
Source code yang dapat diakses pada repository ini telah diberi hint pada bagian algoritma-nya. Coder dapat melengkapi **spesifikasi** fungsi/prosedur dan **kamus**, sedangkan **pada bagian algoritma, coder cukup mengisi ellipsis** (`...`) sesuai dengan hint yang diberikan.
Sebagian fungsi/prosedur yang diimplementasi di sini memanfaatkan struktur data dictionary yang cukup kompleks, terutama pada global variable `data`. Akan tetapi jangan khawatir, pada bagian struktur data di bawah akan dijelaskan secara lengkap bagaimana struktur data yang digunakan terutama pada global variable `data`.
Good luck !

## Panduan Tester
Work in progress ...

# Struktur data

## Global variable

### Data
Global variable data menyimpan **semua** data yang digunakan pada program. `data` bertype dictionary dengan 6 keys (atribut) berikut.
```
1. user
Akses dengan memanggil data["user"]. Atribut ini merupakan sebuah Array yang berisi data user.
2. gadget
Akses dengan memanggil data["gadget"]. Atribut ini merupakan sebuah Array yang berisi data gadget.
3. consumable
Akses dengan memanggil data["consumable"]. Atribut ini merupakan sebuah Array yang berisi data consumable.
4. gadget_borrow_history
Akses dengan memanggil data["gadget_borrow_history"]. Atribut ini merupakan sebuah Array yang berisi data riwayat peminjaman gadget.
5. gadget_return_history
Akses dengan memanggil data["gadget_return_history"]. Atribut ini merupakan sebuah Array yang berisi data riwayat pengembalian gadget.
6. consumable_history
Akses dengan memanggil data["consumable_history"]. Atribut ini merupakan sebuah Array yang berisi data riwayat pengambilan consumable.
```
Setiap elemen keenam Array di atas merupakan sebuah dictionary dengan struktur yang berbeda.

#### user
`user` merupakan elemen dari Array `data["user"]`. Setiap `user` dapat diakses dengan memanggil `data["user"][<index>]`. Untuk mempermudah, kita buat `index` sesuai dengan `id` (lihat atribut `id` di bawah), yaitu `id = index + 1`. Artinya, `data["user"][0]` adalah `user` dengan `id` 1, dan seterusnya.
`user` bertype dictionary dengan 6 keys (atribut) berikut.
```
1. id
Akses dengan memanggil user["id"]. Atribut ini bertype integer > 0.
2. username
Akses dengan memanggil user["username"]. Atribut ini bertype string unique.
3. name
Akses dengan memanggil user["name"]. Atribut ini bertype string, tidak pernah kosong, dan alphabetic.
4. address
Akses dengan memanggil user["address"]. Atribut ini bertype string.
5. password
Akses dengan memanggil user["password"]. Atribut ini bertype string dengan panjang 32.
6. role
Akses dengan memanggil user["role"]. Atribut ini bertype string dengan value "Admin" atau "User".
```

#### gadget
Work in progress ...

#### consumable
Work in progress ...

#### gadget_borrow_history
Work in progress ...

#### gadget_return_history
Work in progress ...

#### consumable_history
Work in progress ...

## Constants
Work in progress ...