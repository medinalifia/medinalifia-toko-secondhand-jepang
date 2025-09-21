# medinalifia-toko-secondhand-jepang

# Capstone Project - CRUD Second-Hand Store Jepang

**Author:** Medina Alifia Juniarto  
**Date:** October 2025

## Deskripsi Singkat

Project ini adalah **CRUD (Create, Read, Update, Delete)** aplikasi manajemen barang second-hand store Jepang.  

Fitur utama aplikasi:

- Menambahkan item atau barang baru dalam daftar keranjang (Add)
- Melihat semua barang atau spesifik per 'ItemID' menggunakan PrettyTable (Read)
- Mengubah data barang secara parsial atau keseluruhan  (Edit) > Update
- Menghapus barang spesifik atau semua barang  (Delete)

## Fitur Utama

### 1. Create (Tambah Barang)
- Masukkan **ItemID** unik dengan format `JPNXXX`  
- Masukkan **Nama**, **Kategori**, **Harga**, **Stok**, dan **Asal**  
- **Validasi input**:
  - `ItemID`: format JPN + 3 angka, tidak boleh duplikat  
  - `Nama` / `Kategori` / `Asal`: hanya huruf/spasi (bisa juga tanda `- ' .`)  
  - `Harga` / `Stok`: angka ≥ 0  

### 2. Read (Lihat Data)
- Tampilkan semua data dalam **tabel rapi**  
- Tampilkan data spesifik per `ItemID`  
- Format tampilan bisa:
  - **Tabel** (ringkas)  
  - **Detail** (vertikal, satu kolom per atribut)  

### 3. Update (Ubah Data)
- Update kolom tertentu: `Nama`, `Kategori`, `Harga`, `Stok`, `Asal`  
- Update seluruh baris sekaligus, termasuk `ItemID` (jika diizinkan)  
- Validasi input sama seperti saat **Create**  

### 4. Delete (Hapus Data)
- Hapus barang spesifik per `ItemID`  
- Hapus semua data sekaligus  
- Selalu ada **konfirmasi** sebelum penghapusan  

---

## 📦 Struktur Data

Setiap barang disimpan dalam bentuk dictionary:

```python
{
    "ItemID": "JPN001",
    "Nama": "Yukata",
    "Kategori": "Pakaian",
    "Harga": 7500,
    "Stok": 3,
    "Asal": "Osaka"
}

## (Google Drive Folder: https://drive.google.com/file/d/1VIVMkHXDsMjTOyUYqqXeh5kO0NBq5YFu/view?usp=sharing )

