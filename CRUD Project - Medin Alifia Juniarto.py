# Capstone Project - Medina Alifia Juniarto

shop_data = [
    {"ItemID": "JPN001", "Nama": "Yukata", "Kategori": "Pakaian", "Harga": 7500, "Stok": 3, "Asal": "Osaka"},
    {"ItemID": "JPN002", "Nama": "CD One Piece", "Kategori": "Media", "Harga": 3200, "Stok": 10, "Asal": "Kobe"},
    {"ItemID": "JPN003", "Nama": "Vakum Panasonic", "Kategori": "Peralatan Rumah", "Harga": 9800, "Stok": 2, "Asal": "Kyoto"},
    {"ItemID": "JPN004", "Nama": "Muji Sling Bag", "Kategori": "Tas", "Harga": 5300, "Stok": 3, "Asal": "Nara"}
    
]

# Mencari Barang dalam Second-Hand Store
def find_item(item_id):
    for item in shop_data:
        if item["ItemID"] == item_id:
            return item
    return None

# Menambahkan Barang ke dalam Keranjang 
def add_item(new_item):
    shop_data.append(new_item)

# Mengubah Salah Satu Kolom data Barang
def edit_item(item, column, new_value):
    if item and column in item:
        item[column] = new_value
        print(f"Item {item['ItemID']} kolom {column} sudah diperbaharui.")

# Mengubah Keseluruhan Data Barang per Baris
def edit_item_all(item, new_values):
    if item:
        if new_values.get("new_id"):
            item["ItemID"] = new_values["new_id"]
        for key in item.keys():
            if key in new_values and key != "new_id":
                item[key] = new_values[key]
    
# Menghapus Data Item Secara Menyeluruh
def remove_item(item):
    shop_data.remove(item)

# Penggunaan Fungsi Table 

from prettytable import PrettyTable

def display_table(data, title="Data Barang Second Hand Store Jepang"):
        # Menampilkan data dalam bentuk table secara keseluruhan
    if not data:
        print("\n Data tidak tersedia. Daftar Barang tidak bisa ditampilkan.")
        return
    
    if type(data) == dict:
        data = [data] 
        # Kalau single dict akan diubah menjadi bentuk list 
    
    print(f"\n=== {title} ===")
    table = PrettyTable()
    headers = [key.title() for key in data [0].keys()]
    table.field_names = headers

    for row in data:
        table.add_row([row.get(i, "") for i in data[0].keys()])
   
    print(table)

# Display Data Secara Spesifik

def display_item_detail(item, title="Detail Barang Spesifik"):
    # Menampilkan detail 1 ItemID dengan semua kolom kebawah
    if not item:
        print("❌ Data barang tidak ditemukan.")
        return
    
    print(f"\n=== {title} ===")
    for key, value in item.items():
        print(f"{key:<10}: {value}")

# MELAKUKAN VALIDASI INPUT #

# Validasi Item ID Barang 
def ItemID_validation(text):
    while True:
        item_id = input(text).upper()
        if item_id == "KEMBALI":
            return None
        if len(item_id) == 6 and item_id.startswith("JPN") and item_id[3:].isdigit():
            if find_item(item_id): 
                print("❌ ID sudah terdaftar dalam list, masukkan ID lain.")
                continue
            return item_id
        else:
            print("❌ Format ID harus berupa JPN + 3 angka (contoh: JPN005).")

# Validasi Nama, Kategori, dan Asal Barang
def string_validation(text):
    while True:
        value = input(text).strip()
        if value.replace(" ", "").isalpha():
            return value.title()
        print("❌ Masukkan keterangan berupa huruf.")
        
# Validasi Harga dan Stok Barang (Angka >= 0)
def number_validation(text):
    while True:
        try:
            num = int(input(text))
            if num >= 0:
                return num
            print("❌ Harus berupa angka positif.")
        except:
            print("❌ Keterangan tidak valid. Masukkan angka.")

# MENU 

## CRUD : CREATE ## 
# Menambahkan Barang Baru ke Keranjang
def create_item():
    print("\n=== Tambah Barang Baru ===")
    new_id = ItemID_validation("Masukkan ItemID (JPNXXX) atau 'KEMBALI': ")
    if new_id is None:
        return
    nama = string_validation("Masukkan Nama Barang: ")
    kategori = string_validation("Masukkan Kategori Barang: ")
    harga = number_validation("Masukkan Harga Barang: ")
    stok = number_validation("Masukkan Stok Barang: ")
    asal = string_validation("Masukkan Asal Barang: ")

    confirm = input("Tambahkan barang ini? (Yes/No): ").lower()
    if confirm == "yes":
        add_item({
            "ItemID": new_id,
            "Nama": nama,
            "Kategori": kategori,
            "Harga": harga,
            "Stok": stok,
            "Asal": asal
        })
        print("✅ Barang berhasil ditambahkan.")
        display_table(shop_data)
    else:
        print("❌ Penambahan dibatalkan.")


## CRUD : READ ## 

def display_all_data():
    display_table(shop_data)

def display_specific_item():
    while True:
        print("\n1. Format tabel")
        print("2. Format detail")
        choice = input("Pilih (1/2) atau 'kembali': ").strip()
        if choice.lower() == "kembali":
            return
        item_id = input("Masukkan ItemID: ").upper()
        item = find_item(item_id)
        if not item:
            print("❌ Barang tidak ditemukan.")
            continue
        if choice == "1":
            display_table(item)
        elif choice == "2":
            display_item_detail(item)
        else:
            print("❌ Pilihan tidak valid.")

# Melakukan Perubahan Data Barang secara Parsial atau Menyeluruh
## CRUD : UPDATE ## 
def update_specific_data():
    print("\nMenu - Melakukan Update Data Barang")
    while True:
        item_id = input("Masukkan ItemID yang ingin diubah atau 'kembali': ").upper()
        if item_id == "KEMBALI":
            return
        item = find_item(item_id)
        if not item:
            print("❌ Barang tidak ditemukan dalam daftar.")
            continue
        display_table(item, "Data Barang")

        column = input("Masukkan kolom yang ingin diubah (Nama/Kategori/Harga/Stok/Asal) atau 'batal': ").capitalize()
        if column == "Batal":
            return
        if column in item:
            if column in ["Harga", "Stok"]:
                new_value = number_validation(f"Masukkan {column} baru: ")
            else:
                new_value = string_validation(f"Masukkan {column} baru: ")
            edit_item(item, column, new_value)
            print("✅ Data berhasil diubah.")
            display_table(shop_data)
            return
        else:
            print("❌ Kolom tidak valid.")

def update_row_data():
    print("\nMenu - Update Salah Satu Baris Data Barang.")
    while True:
        item_id = input("Masukkan ItemID yang ingin diubah atau 'kembali': ").upper()
        if item_id == "KEMBALI":
            return
        item = find_item(item_id)
        if not item:
            print("❌ Barang tidak ditemukan dalam daftar.")
            continue
        display_table(item, "Data Barang")

        while True:
            new_id = input("Masukkan Kode Baru (kosong jika tidak diganti): ").upper()
            if new_id == "":
                new_id = None
                break
            valid_id = (new_id)
            if valid_id:
                new_id = valid_id
                break

        # Nama
        nama = input("Masukkan Nama baru (kosong jika tidak diganti): ")
        if nama:
            nama = string_validation(f"Masukkan Nama baru: ")  # validasi user input langsung

        kategori = input("Masukkan Kategori baru (kosong jika tidak diganti): ")
        if kategori:
            kategori = string_validation(f"Masukkan Kategori baru: ")

        # Harga 
        while True:
            harga = input("Masukkan Harga baru (kosong jika tidak diganti): ")
            if harga == "":
                harga = None
                break
            try:
                harga = int(harga)
                if harga < 0:
                    print("❌ Harus angka >=0")
                    continue
                break
            except:
                print("❌ Harus angka.")

        # Stok
        while True:
            stok = input("Masukkan Stok baru (kosong jika tidak diganti): ")
            if stok == "":
                stok = None
                break
            try:
                stok = int(stok)
                if stok < 0:
                    print("❌ Harus angka >=0")
                    continue
                break
            except:
                print("❌ Harus angka.")

        # Asal
        asal = input("Masukkan Asal baru (kosong jika tidak diganti): ")
        if asal:
            asal = string_validation(f"Masukkan Asal baru: ")

# Mengubah menjadi bentuk Value yang Baru

        new_values = {
            "new_id": new_id if new_id else None,
            "Nama": nama if nama else None,
            "Kategori": kategori if kategori else None,
            "Harga": int(harga) if harga else None,
            "Stok": int(stok) if stok else None,
            "Asal": asal if asal else None
        }

        edit_item_all(item, new_values)
        print("✅ Data berhasil diperbaharui dalam daftar.")
        display_table(shop_data)
        return

# Penghapusan Data Secara Parsial atau Menyeluruh
## CRUD : DELETE ## 
def delete_specific_data():
    print("\nMenu - Hapus Data Barang dalam daftar.")
    while True:
        item_id = input("Masukkan ItemID yang ingin dihapus atau 'kembali': ").upper()
        if item_id == "KEMBALI":
            return
        item = find_item(item_id)
        if not item:
            print("❌ Barang tidak dapat ditemukan dalam daftar.")
            continue
        display_table(item, "Data Barang")
        confirmation = input("Apakah yakin ingin menghapus barang ini? (Yes/No): ").lower()
        if confirmation == "yes":
            remove_item(item)
            print("✅ Data telah berhasil dihapus dalam daftar.")
            display_table(shop_data)
            return
        else:
            print("Penghapusan telah dibatalkan.")
            return

def delete_all_data():
    print("\nMenu - Hapus Semua Data dalam daftar.")
    confirmation = input("Apakah yakin ingin menghapus semua data? (Yes/No): ").lower()
    if confirmation == "yes":
        shop_data.clear()
        print("✅ Semua data berhasil dihapus dalam daftar.")
    else:
        print("Penghapusan telah dibatalkan.")

def main():
    while True:
        print("\nCapstone Project - CRUD Second Hand Store Jepang")
        print("1. Read Data (Tampilkan Data)")
        print("2. Create Data (Buat Data Baru)")
        print("3. Update Data (Ubah Data)")
        print("4. Delete Data (Hapus Data)")
        print("5. Exit Program (Keluar Program)")

        choice = input("Pilih menu (1-5): ").strip()
        if choice == "1":
            print("\nMenu Read")
            print("1. Tampilkan semua data")
            print("2. Tampilkan data berdasarkan ItemID")
            sub_choice = input("Pilih menu (1/2): ")
            if sub_choice == "1":
                display_table(shop_data)
            elif sub_choice == "2":
                display_specific_item()
        elif choice == "2":
            create_item()
        elif choice == "3":
            print("\nMenu Update")
            print("1. Ubah kolom secara spesifik")
            print("2. Ubah data secara keseluruhan")
            sub_choice = input("Pilih menu (1/2): ")
            if sub_choice == "1":
                update_specific_data()
            elif sub_choice == "2":
                update_row_data()
        elif choice == "4":
            print("\nMenu Delete")
            print("1. Hapus data secara spesifik dalam daftar")
            print("2. Hapus semua data secara keseluruhan")
            sub_choice = input("Pilih menu (1/2): ")
            if sub_choice == "1":
                delete_specific_data()
            elif sub_choice == "2":
                delete_all_data()
        elif choice == "5":
            print("Terima kasih, daftar toko telah selesai dijalankan.")
            break
        else:
            print("❌ Pilihan tidak valid. Masukkan Angka 1-5.")

if __name__ == "__main__":
    main()

