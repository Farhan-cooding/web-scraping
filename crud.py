import json

def load_data():
    try:
        with open('data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_all(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

# --- FUNGSI CRUD ---

def create_book(title, price, stock):
    data = load_data()
    new_id = data[-1]['id'] + 1 if data else 1
    new_book = {"id": new_id, "title": title, "price": price, "stock": stock}
    data.append(new_book)
    save_all(data)
    print(f"Buku '{title}' berhasil ditambahkan!")

def read_books():
    data = load_data()
    for b in data:
        print(f"[{b['id']}] {b['title']} - {b['price']}")

def update_book(book_id, new_title):
    data = load_data()
    for b in data:
        if b['id'] == book_id:
            b['title'] = new_title
            save_all(data)
            print(f"Buku ID {book_id} berhasil diubah!")
            return
    print("ID tidak ditemukan.")

def delete_book(book_id):
    data = load_data()
    data = [b for b in data if b['id'] != book_id]
    save_all(data)
    print(f"Buku ID {book_id} telah dihapus!")

# Contoh Penggunaan:
if __name__ == "__main__":
    print("--- Daftar Buku Saat Ini ---")
    read_books()
    
    print("\n--- Menambah Buku Baru ---")
    create_book("Belajar Python Scraping", "£25.00", "In Stock")
    
    print("\n--- Menghapus Buku ID 1 ---")
    delete_book(1)