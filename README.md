# Web Scraping Data Buku

Project ini merupakan program Python untuk melakukan web scraping data buku dari website **Books to Scrape**, kemudian menyimpannya ke dalam format JSON dan CSV. Selain itu, project ini dilengkapi dengan fitur CRUD (Create, Read, Update, Delete) untuk mengelola data secara lokal.

## Sumber Data
Data diambil dari:
- [https://books.toscrape.com/](https://books.toscrape.com/)

## Teknologi yang Digunakan
- Python 3.x
- requests (untuk HTTP request)
- BeautifulSoup4 (untuk parsing HTML)
- pandas (untuk manipulasi data/CSV)

## Struktur Folder
```text
Percobaan 1/
├── scraper.py     # Script untuk mengambil data dari web
├── crud.py        # Script untuk pengelolaan data (CRUD)
├── data.json      # Database hasil scraping (JSON)
├── data.csv       # Database hasil scraping (CSV)
└── README.md      # Dokumentasi project
```
## Cara Menjalankan
1. Install dependency

Buka terminal atau command prompt, lalu jalankan perintah berikut untuk menginstal library yang diperlukan:
```text
pip install requests beautifulsoup4 pandas
```

2. Jalankan scraping

Gunakan perintah ini untuk mengambil data terbaru dari website:
```text
python scraper.py
```

3. Jalankan CRUD

Gunakan perintah ini untuk mengelola data (menambah, melihat, atau menghapus) yang ada di file penyimpanan:
```text
python crud.py
```
## Output
Program akan menghasilkan dua jenis file penyimpanan:

* data.json (format JSON)
* data.csv (format CSV)

Contoh struktur data:
```text
{
    "id": 1,
    "title": "A Light in the Attic",
    "price": "£51.77",
    "stock": "In stock"
}
```
👤 Author

Nama: MOHAMMAD FARHAN EFFENDI

Mata Kuliah: PENGEMBANGAN APLIKASI BERBASIS WEB

## Fitur CRUD
* Menambahkan data pekerjaan
* Menampilkan data dalam bentuk tabel
* Mengubah data berdasarkan ID
* Menghapus data

## Catatan
* Data digunakan hanya untuk keperluan pembelajaran
* Website yang digunakan merupakan situs latihan scraping

