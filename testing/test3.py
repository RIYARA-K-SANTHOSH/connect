from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and PATH is set correctly
driver.maximize_window()
driver.get("http://127.0.0.1:8000/create-notification/")  # Updated to the actual URL of the notification page

try:
   
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "notificationForm"))
    )
    title_input = driver.find_element(By.ID, "title")
    title_input.send_keys("New Notification Title")
    message_input = driver.find_element(By.ID, "message")
    message_input.send_keys("This is a test notification message.")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//table/tbody/tr[1]/td[1]"))
    )
    added_notification_title = driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[1]").text
    if added_notification_title == "New Notification Title":
        print("Notification added successfully!")
    else:
        print("Notification was not added.")   
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    time.sleep(3)
    driver.quit()
