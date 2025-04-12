from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and PATH is set correctly
driver.maximize_window()
driver.get("http://127.0.0.1:8000/packages/create/")
try:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "form"))
    )
    name_input = driver.find_element(By.ID, "name")
    name_input.send_keys("Test Package")
    price_input = driver.find_element(By.ID, "price")
    price_input.send_keys("99.99")
    description_input = driver.find_element(By.ID, "description")
    description_input.send_keys("This is a test package description.")
    duration_input = driver.find_element(By.ID, "duration_days")
    duration_input.send_keys("30")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    WebDriverWait(driver, 10).until(
        EC.url_to_be("http://127.0.0.1:8000/packages/")
    )
    package_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//table/tbody/tr[1]/td[1]"))
    ).text
    if package_name == "Test Package":
        print("Package created successfully!")
    else:
        print("Package was not created.")
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(3)
    driver.quit()
