from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tabulate import tabulate
import pandas as pd
import time

options = webdriver.ChromeOptions()
service = Service()
driver = webdriver.Chrome(options=options, service=service)
url = 'https://www.kabum.com.br/hardware/placa-de-video-vga'
driver.get(url)
driver.maximize_window()
time.sleep(3)

productsList = []
pricesList = []

wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)
while True:
    try:
        wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'productCard'))
        )

        names = driver.find_elements(By.CSS_SELECTOR, 'span.nameCard')
        name = [name.text.strip() for name in names]

        prices = driver.find_elements(By.CSS_SELECTOR, 'span.priceCard')
        price = [price.text.strip() for price in prices]

        productsList.extend(name)
        pricesList.extend(price)

        li_next = driver.find_element(By.CLASS_NAME, 'next')
        if 'disabled' in li_next.get_attribute('class'): break
        
        next_link = li_next.find_element(By.CLASS_NAME, 'nextLink')

        scroll_origin = ScrollOrigin.from_element(li_next)

        actions.scroll_to_element(li_next).scroll_from_origin(scroll_origin, 0, 100).move_to_element(next_link).click().perform()

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
