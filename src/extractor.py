from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def extract_data(url):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(url)
    time.sleep(5)  # Wait for the page to load
    # Add your extraction logic here
    print("Extracted data from:", driver.title)
    driver.quit()

if __name__ == "__main__":
    extract_data("http://www.example.com")  # Change to the appropriate URL
