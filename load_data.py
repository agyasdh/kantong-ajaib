# TESTED 17/04/2021 - 12:54:42

# Code ini sudah work, tinggal diberi dokumentasi

import argparse, os

data = {
    "user" : [],
    "gadget" : [],
    "consumable" : [],
    "gadget_borrow_history" : [],
    "gadget_return_history" : [],
    "consumable_history" : []
}

dataTypes = {
    "user" : [int, str, str, str, str, str],
    "gadget" : [str, str, str, int, str, int],
    "consumable" : [str, str, str, int, str],
    "gadget_borrow_history" : [int, int, str, str, int],
    "gadget_return_history" : [int, int, str, str, int],
    "consumable_history" : [int, int, str, str, int]
}

dataKeysCustom = {
    "user" : ["id", "username", "name", "address", "password", "role"],
    "gadget" : ["id", "name", "description", "amount", "rarity", "year"],
    "consumable" : ["id", "name", "description", "amount", "rarity"],
    "gadget_borrow_history" : ["id", "uid", "gid", "date", "amount"],
    "gadget_return_history" : ["id", "uid", "gid", "date", "amount"],
    "consumable_history" : ["id", "uid", "cid", "date", "amount"]
}

dataKeys = {
    "user" : ["id", "username", "name", "address", "password", "role"],
    "gadget" : ["id", "name", "description", "amount", "rarity", "year"],
    "consumable" : ["id", "name", "description", "amount", "rarity"],
    "gadget_borrow_history" : ["id", "uid", "gid", "date", "amount"],
    "gadget_return_history" : ["id", "uid", "gid", "date", "amount"],
    "consumable_history" : ["id", "uid", "cid", "date", "amount"]
}

def loadData():
    global data
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", nargs="?", default="")
    args = parser.parse_args()
    print(args)
    if args.dir == "":
        print("Tidak ada nama folder yang diberikan !")
        print("Usage : python kantongajaib.py <nama_folder>")
    else:
        dirPath = args.dir
        if (os.path.isdir(dirPath)):
            print("\nLoading...")
            for key in data:
                data[key] = loadCSV(dirPath + "/" + key + ".csv", key)
        else:
            print("Folder tidak ditemukan !")

def loadCSV(path, key):
    f = open(path)
    csvString = f.read()
    return parseCSV(csvString, key)

def parseCSV(csvString, key):
    arr = []
    lines = explode(csvString, "\n")
    if len(lines) > 1:
        for line in lines[1:]:
            data = {}
            values = explode(line, ";")
            for i in range(len(values)):
                currentKey = dataKeysCustom[key][i]
                castValue = dataTypes[key][i](values[i])
                data.update({currentKey : castValue})
            arr.append(data)
    return arr

def explode(string, separator):
    arr = []
    el  = ""
    for char in string:
        if char != separator:
            el += char
        else:
            arr.append(el)
            el = ""
    arr.append(el)
    return arr
