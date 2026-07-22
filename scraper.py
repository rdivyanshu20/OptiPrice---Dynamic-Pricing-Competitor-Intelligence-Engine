import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class CompetitorScraper:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") # Runs silently in background
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        
    def get_competitor_price(self, url):
        """Fetches dynamic content and extracts pricing."""
        self.driver.get(url)
        time.sleep(2) # Allow JavaScript to render pricing
        
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        
        # NOTE: You will need to customize this CSS selector per competitor domain
        try:
            price_element = soup.find(class_='price-tag') 
            if price_element:
                # Clean currency formatting
                price_text = price_element.text.replace('$', '').replace(',', '').strip()
                return float(price_text)
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            
        return None

    def close(self):
        self.driver.quit()