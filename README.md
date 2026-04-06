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
