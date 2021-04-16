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