# function explode(string, separator)
# Menghasilkan Array substring dengan memisahkan string oleh separator
# Contoh : explode("a.bc.d.efg.h", ".") -> ["a", "bc", "d", "efg", "h"]
def explode(string, separator):

    # KAMUS LOKAL
    # arr : list
    # el : string
    # char : string (1-character string)

    # ALGORITMA
    arr = []
    el = ""
    for char in string:
        if char != separator:
            el += char
        else:
            arr.append(el)
            el = ""
    arr.append(el)
    return arr