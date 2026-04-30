import json

def load_data():
    try:
        # Membuka dengan encoding utf-8 agar simbol mata uang terbaca benar
        with open('data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_all(data):
    # Menyimpan dengan encoding utf-8 dan ensure_ascii=False
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# --- FUNGSI CRUD ---

def create_book(title, price, stock):
    data = load_data()
    # Menentukan ID baru
    new_id = data[-1]['id'] + 1 if data else 1
    new_book = {"id": new_id, "title": title, "price": price, "stock": stock}
    data.append(new_book)
    save_all(data)
    print(f"Berhasil! Buku '{title}' ditambahkan.")

def read_books():
    data = load_data()
    if not data:
        print("Data kosong.")
        return
    print(f"{'ID':<4} | {'Harga':<10} | {'Judul'}")
    print("-" * 50)
    for b in data:
        print(f"{b['id']:<4} | {b['price']:<10} | {b['title']}")

def update_book(book_id, new_title):
    data = load_data()
    for b in data:
        if b['id'] == book_id:
            b['title'] = new_title
            save_all(data)
            print(f"Buku ID {book_id} berhasil diubah menjadi: {new_title}")
            return
    print("ID tidak ditemukan.")

def delete_book(book_id):
    data = load_data()
    original_count = len(data)
    data = [b for b in data if b['id'] != book_id]
    
    if len(data) < original_count:
        save_all(data)
        print(f"Buku ID {book_id} telah dihapus!")
    else:
        print("ID tidak ditemukan.")

# --- CONTOH EKSEKUSI ---
if __name__ == "__main__":
    print("--- MENU CRUD DATA BUKU ---")
    read_books()
    
    # Contoh: Uncomment bagian bawah ini untuk mencoba fungsi
    # create_book("Buku Sakti Informatika UMSIDA", "£30.00", "In Stock")
    # delete_book(1)
