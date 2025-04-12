from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and PATH is set correctly
driver.maximize_window()

# Open the login page
driver.get("http://127.0.0.1:8000/adminmain")  # Update the login URL if necessary

try:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "email"))  # Use NAME if no ID is present
    )

    email_input = driver.find_element(By.NAME, "email")  # Use By.NAME if IDs are not present
    email_input.send_keys("admin@gmail.com")
    password_input = driver.find_element(By.NAME, "password")  # Ensure the selector is correct
    password_input.send_keys("admin123")
    password_input.send_keys(Keys.RETURN)
   
    WebDriverWait(driver, 10).until(
        EC.url_to_be("http://127.0.0.1:8000/adminmain")  # Ensure the URL is correct
    )

    if driver.current_url == "http://127.0.0.1:8000/adminmain":
        print("Login successful, reached the admin page!")
    else:
        print("Login failed or redirection error.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(3)
    driver.quit()
