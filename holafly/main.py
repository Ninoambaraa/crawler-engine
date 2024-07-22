from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get('https://esim.holafly.com/esim-germany/')

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'days-selector')))

    while True:
        try:
            dropdown_trigger = driver.find_element(By.CLASS_NAME, 'dinamicNumber')
            driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_trigger)

            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'dinamicNumber')))
            dropdown_trigger.click()

            dropdown_items = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.dropDownDinamicNumber li'))
            )

            for item in dropdown_items:
                try:
                    day = item.get_attribute('data-day-number')
                    print(f'Selecting {day} days option')

                    driver.execute_script("arguments[0].click();", item)

                    harga_element = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, '.custom-plan_price_number .woocommerce-Price-amount'))
                    )
                    harga = harga_element.text

                    print(f'Harga untuk {day} days: {harga}')

                    dropdown_trigger.click()
                    time.sleep(0.2)  

                except Exception as e:
                    print(f"Error handling item: {e}")

        except Exception as e:
            print(f"Dropdown no longer available or error: {e}")
            break

finally:
    # Tutup browser
    driver.quit()
