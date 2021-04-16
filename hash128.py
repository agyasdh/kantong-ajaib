
# JUST ENOUGH HASH
def hash128(password: str) -> str:
    """
        @algorithm
            [1] Convert string ke Byte Array
            [2] Jika panjang Byte Array < 32 DAN panjang mod 16 ! = 0,
                tambahkan padding dengan ketentuan sebagai berikut :
                [a] Jika panjang 0, tambah padding 77
                [b] Jika panjang 1, tambah padding 91
                [c] Selainnya, tambah padding sebagai berikut.
                    [c1] Untuk index 0 (mod 4), tambah padding
                        nilai XOR dari byte awal dan akhir
                    [c2] Untuk index 1 (mod 4), tambah padding
                        nilai XOR dari AND semua index genap 
                        dan AND semua index ganjil
                    [c3] Untuk index 2 (mod 4), tambah padding
                        nilai XOR dari OR semua index genap 
                        dan OR semua index ganjil
                    [c4] Untuk index 3 (mod 4), tambah padding
                        nilai AND dari XOR 1/2 index pertama
                        dan index terakhir
            [3] Bagi Byte Array menjadi Bits Array
            [4] Buat Bits Array baru dengan panjang FIXED 128
            [5] Bagi Bits Array menjadi chunk dengan setiap chunk
                terdiri atas 128 bits
            [6] Untuk setiap chunk hingga panjang Bits Array - 128,
                [a] Lakukan mapping sebagai berikut.
                    [a1] Untuk setiap index 0 (mod 4),
                        bit = b[i] ^ b[i + 128]
                    [a2] Untuk setiap index 1 (mod 4),
                        bit = b[i] | b[i + 128]
                    [a3] Untuk setiap index 2 (mod 4),
                        bit = (o % 2) & (b[i] ^ b[i + 128])
                    [a4] Untuk setiap index 3 (mod 4),
                        bit = (o % 2) & (b[i] | b[i + 128])
                [b] Lakukan rotasi untuk konstanta a, b, c, d
            [7] Convert Bits Array ke Hex String
                         
    """

    """
        @const str hexString
            Berisi karakter hexadecimal sesuai indexnya.
    """
    hexString: str = "0123456789abcdef"
    """
        @description
            Variabel mapper bits untuk hashing.
    """
    (a, b, c, d) = (26, 88, 171, 243)
    """
        LANGKAH [1]
    """
    byteArray: list = list(bytes(password, "utf-8"))
    
    """
        LANGKAH [2]
        @description
            String yang akan di-hash setidaknya memiliki panjang kelipatan
            dari 64 bytes. Jika tidak, tambahkan padding berdasarkan
            penjumlahan 2 byte terakhir hingga menjadi kelipatan 64. 
    """
    if len(byteArray) % 16 != 0 or len(byteArray) < 32:
        # f = open("hash.txt", "a")
        while len(byteArray) % 16 != 0 or len(byteArray) < 32:
            if len(byteArray) == 0:
                byteArray.append(77)
            elif len(byteArray) == 1:
                byteArray.append(91)
            else:
                if len(byteArray) % 4 == 0:
                    padding = 157
                    for byte in byteArray:
                        padding += byte
                        padding %= 256
                    byteArray.append(padding)
                elif len(byteArray) % 4 == 1:
                    byteArray.append((byteArray[-1] + byteArray[-2] + 77) % 256)
                elif len(byteArray) % 4 == 2:
                    byteArray.append((byteArray[-1] * byteArray[1] * byteArray[-2] - 2) % 256)
                elif len(byteArray) % 4 == 3:
                    byteArray.append(((byteArray[-1] * byteArray[2]) % 
                    (byteArray[-3] if byteArray[-3] != 0 else 256)
                    ) % 256)
            # f.writelines(str(byteArray))
            # f.writelines("\n")
    """
        LANGKAH [3]
        @description
            Convert byteArray ke bitsArray.
    """
    bitsArray: list = []
    for byte in byteArray:
        bit = byteToBit(byte)
        bitsArray.extend(bit)


    """
        LANGKAH [4]
    """
    bits: list = [0 for i in range(128)]

    """
        LANGKAH [5] dan [6]
    """

    for chunk in range(0, len(bitsArray) - 128, 128):
        for i in range(chunk, chunk + 128):
            p = bitsArray[i]
            q = bitsArray[i + 128]
            if i % 4 == 0:
                o = (a ^ b) & d
                k = p ^ q
            elif i % 4 == 1:
                o = (c & d) | b
                k = p | q
            elif i % 4 == 2:
                o = b ^ c ^ d
                k = (o % 2) & (p ^ q)
            elif i % 4 == 3:
                o = (a & c) ^ d
                k = (o % 2) & (p | q)
            """
                @description
                    Rotasi mapper variable.
            """
            temp = a
            a = b
            b = d
            c = a ^ b
            d = c & (a | d) ^ temp
            bits[i % 128] = k

    """
        LANGKAH [7]
    """
    
    byte: list[int] = []
    for i in range(0, len(bits), 8):
        bitsTuple = tuple([bits[i + x] for x in range(8)])
        newByte = bitToByte(bitsTuple)
        byte.append(newByte)
    """
        @description
            Convert bits hash menjadi hexadecimal string.
    """
    hexHash: str = ""
    for i in byte:
        x: str = hexString[i // 16]
        y: str = hexString[i % 16]
        hexHash += x + y
    return hexHash

"""
    @description
        Mengconvert 8-bit integer (0 - 255) menjadi 8-tuple bits.
        Contoh : byteToBit(130) -> (0, 1, 0, 0, 0, 0, 1, 0)

    @param b int
        8-bit integer (0 - 255)

    @returns tuple[int]
        8-tuple bits
"""
def byteToBit(b: int) -> tuple[int]:
    return (b // 128, b // 64 % 2, b // 32 % 2, b // 16 % 2, b // 8 % 2, b // 4 % 2, b // 2 % 2, b % 2)

"""
    @description
        Mengconvert 8-tuple bits menjadi 8-bit integer.
        Contoh : (0, 1, 0, 0, 0, 0, 1, 0) -> byteToBit(130)

    @param b tuple[int]
        8-tuple bits

    @returns int
        8-bit integer (0 - 255)
"""
def bitToByte(b: tuple[int]) -> int:
    return b[0] * 128 + b[1] * 64 + b[2] * 32 + b[3] * 16 + b[4] * 8 + b[5] * 4 + b[6] * 2 + b[7]
