from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tabulate import tabulate
import pandas as pd
import time

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
url = 'https://www.kabum.com.br/hardware/placa-de-video-vga'
driver.get(url)
time.sleep(3)

productsList = []
pricesList = []

while True:
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.nameCard'))
        )

        names = driver.find_elements(By.CSS_SELECTOR, 'span.nameCard')
        name = [name.text.strip() for name in names]

        prices = driver.find_elements(By.CSS_SELECTOR, 'span.priceCard')
        price = [price.text.strip() for price in prices]

        productsList.extend(name)
        pricesList.extend(price)

        next_li = driver.find_element(By.CSS_SELECTOR, 'li.next')
        if 'disabled' in next_li.get_attribute('class'): break

        next_link = next_li.find_element(By.CSS_SELECTOR, 'a.nextLink')

        driver.execute_script('arguments[0].scrollIntoView();', next_link)
        driver.execute_script('arguments[0].click();', next_link)

        time.sleep(3)
    except Exception as e:
        print(f'Ocorreu um erro durante a busca {e}')
        break

df = pd.DataFrame({
    'Produtos': productsList,
    'Preços': pricesList
})

df.drop_duplicates().dropna()
df.to_csv('placas.csv', index=False, sep='|')
print(tabulate(df, tablefmt='grid'))

driver.quit()