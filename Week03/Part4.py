from selenium import webdriver 
from bs4 import BeautifulSoup 
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fix the path to Chrome WebDriver
service = Service(executable_path=r'D:/Workspace/3rd Semester/DSA/Driver/chromedriver-win64/chromedriver.exe')

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

products = [] # List to store name of the product 
prices = [] # List to store price of the product 
ratings = [] # List to store rating of the product 

driver.get("https://www.flipkart.com/gaming-laptops-store?otracker=nmenu_sub_Electronics_0_Gaming%20Laptops&otracker=nmenu_sub_E")

# Wait for the products to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_37K3-p')))

content = driver.page_source 
soup = BeautifulSoup(content, 'html.parser') 

for a in soup.findAll('div', attrs={'class':'_37K3-p'}):
    name = a.find('a', attrs={'class':'s1Q9rs'}) 
    price = a.find('div', attrs={'class':'_30jeq3'}) 
    rating = a.find('div', attrs={'class':'_3LWZlK'}) 

    products.append(name.text if name else 'N/A')
    prices.append(price.text if price else 'N/A')
    ratings.append(rating.text if rating else 'N/A') 

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('D:/Workspace/3rd Semester/DSA/products.csv', index=False, encoding='utf-8')
