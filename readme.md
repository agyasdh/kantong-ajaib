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
Global variable `data` menyimpan **semua** data yang digunakan pada program. `data` bertype dictionary dengan 6 keys (atribut) berikut.
```
1. user
Akses dengan memanggil data["user"].
Atribut ini merupakan sebuah Array yang berisi data user.

2. gadget
Akses dengan memanggil data["gadget"].
Atribut ini merupakan sebuah Array yang berisi data gadget.

3. consumable
Akses dengan memanggil data["consumable"].
Atribut ini merupakan sebuah Array yang berisi data consumable.

4. gadget_borrow_history
Akses dengan memanggil data["gadget_borrow_history"].
Atribut ini merupakan sebuah Array yang berisi data riwayat peminjaman gadget.

5. gadget_return_history
Akses dengan memanggil data["gadget_return_history"].
Atribut ini merupakan sebuah Array yang berisi data riwayat pengembalian gadget.

6. consumable_history
Akses dengan memanggil data["consumable_history"].
Atribut ini merupakan sebuah Array yang berisi data riwayat pengambilan consumable.
```
Setiap elemen keenam Array di atas merupakan sebuah dictionary dengan struktur yang berbeda.

#### user
`user` merupakan elemen dari Array `data["user"]`. Setiap `user` dapat diakses dengan memanggil `data["user"][<index>]`. Untuk mempermudah, kita buat `index` sesuai dengan `id` (lihat atribut `id` di bawah), yaitu `id = index + 1`. Artinya, `data["user"][0]` adalah `user` dengan `id` 1, dan seterusnya.
`user` bertype dictionary dengan 6 keys (atribut) berikut.
```
1. id
Akses dengan memanggil user["id"].

2. username
Akses dengan memanggil user["username"].

3. name
Akses dengan memanggil user["name"].

4. address
Akses dengan memanggil user["address"].

5. password
Akses dengan memanggil user["password"].

6. role
Akses dengan memanggil user["role"].
```

#### gadget
`gadget` merupakan elemen dari Array `data["gadget"]`. Setiap `gadget` dapat diakses dengan memanggil `data["gadget"][<index>]`.
`gadget` bertype dictionary dengan 6 keys (atribut) berikut.
```
1. id
Akses dengan memanggil gadget["id"].

2. name
Akses dengan memanggil gadget["username"].

3. description
Akses dengan memanggil gadget["description"].

4. amount
Akses dengan memanggil gadget["amount"].

5. rarity
Akses dengan memanggil gadget["rarity"].

6. year
Akses dengan memanggil gadget["year"].
```

#### consumable
`consumable` merupakan elemen dari Array `data["consumable"]`. Setiap `consumable` dapat diakses dengan memanggil `data["consumable"][<index>]`.
`consumable` bertype dictionary dengan 5 keys (atribut) berikut.
```
1. id
Akses dengan memanggil gadget["id"].

2. name
Akses dengan memanggil gadget["username"].

3. description
Akses dengan memanggil gadget["description"].

4. amount
Akses dengan memanggil gadget["amount"].

5. rarity
Akses dengan memanggil gadget["rarity"].
```

#### gadget_borrow_history
`gadget_borrow_history` merupakan elemen dari Array `data["gadget_borrow_history"]`. Setiap `gadget_borrow_history` dapat diakses dengan memanggil `data["gadget_borrow_history"][<index>]`.
`gadget_borrow_history` bertype dictionary dengan 5 keys (atribut) berikut.
```
1. id
Akses dengan memanggil gadget["id"].

2. user id
Akses dengan memanggil gadget["uid"].

3. gadget id
Akses dengan memanggil gadget["gid"].

4. date
Akses dengan memanggil gadget["date"].

5. amount
Akses dengan memanggil gadget["amount"].
```

#### gadget_return_history
`gadget_return_history` merupakan elemen dari Array `data["gadget_return_history"]`. Setiap `gadget_return_history` dapat diakses dengan memanggil `data["gadget_return_history"][<index>]`.
`gadget_return_history` bertype dictionary dengan **5** keys (atribut) berikut.
*Notice bahwa sebenarnya `gadget_return_history` hanya terdiri atas 4 atribut, tetapi karena bonus FB02, total atribut `gadget_return_history` menjadi 5.
```
1. id
Akses dengan memanggil gadget["id"].

2. user id
Akses dengan memanggil gadget["uid"].

3. gadget id
Akses dengan memanggil gadget["gid"].

4. date
Akses dengan memanggil gadget["date"].

5. amount
Akses dengan memanggil gadget["amount"].
```

#### consumable_history
`consumable_history` merupakan elemen dari Array `data["consumable_history"]`. Setiap `consumable_history` dapat diakses dengan memanggil `data["consumable_history"][<index>]`.
`consumable_history` bertype dictionary dengan 5 keys (atribut) berikut.
```
1. id
Akses dengan memanggil gadget["id"].

2. user id
Akses dengan memanggil gadget["uid"].

3. consumable id
Akses dengan memanggil gadget["cid"].

4. date
Akses dengan memanggil gadget["date"].

5. amount
Akses dengan memanggil gadget["amount"].
```

### Auth
Global variable `auth` menyimpan data autentikasi user. `auth` bertype dictionary dengan 2 keys, yaitu `id` dan `role`.
Secara default, nilai `auth["id"]` dan `auth["role"]` jika user belum login adalah `0` dan `""`.
Jika user telah login, nilai `auth["id"]` berubah menjadi id user dan `auth["role"]` berubah menjadi role user.

## Constants
Work in progress ...