import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def run_scraper():
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')
        
        scraped_data = []
        for index, book in enumerate(books):
            scraped_data.append({
                "id": index + 1,
                "title": book.h3.a['title'],
                "price": book.find('p', class_='price_color').text,
                "stock": "In Stock"
            })
        
        # Simpan ke JSON dengan encoding UTF-8 agar simbol £ aman
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(scraped_data, f, indent=4, ensure_ascii=False)
            
        # Simpan ke CSV dengan encoding UTF-8
        df = pd.DataFrame(scraped_data)
        df.to_csv('data.csv', index=False, encoding='utf-8')
        
        print("Scraping selesai! data.csv dan data.json telah diperbarui dengan format yang benar.")
    else:
        print(f"Gagal akses website. Status: {response.status_code}")

if __name__ == "__main__":
    run_scraper()
