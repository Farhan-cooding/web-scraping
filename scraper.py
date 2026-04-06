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
        
        # Simpan ke JSON
        with open('data.json', 'w') as f:
            json.dump(scraped_data, f, indent=4)
            
        # Simpan ke CSV
        df = pd.DataFrame(scraped_data)
        df.to_csv('data.csv', index=False)
        
        print("Scraping selesai! data.csv dan data.json telah diperbarui.")
    else:
        print("Gagal akses website.")

if __name__ == "__main__":
    run_scraper()