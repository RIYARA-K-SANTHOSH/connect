from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time

# Path to chromedriver (optional if already in PATH)
driver = webdriver.Chrome()

try:
    # Open your Django Advanced Search page (adjust URL as needed)
    driver.get("http://127.0.0.1:8000/advanced-search/")  # Update with your actual URL

    # Wait for page to load
    time.sleep(2)

    # Fill in the age filter
    age_input = driver.find_element(By.NAME, "age")
    age_input.clear()
    age_input.send_keys("25")

    # Select Family Status
    family_status_select = Select(driver.find_element(By.NAME, "family_status"))
    family_status_select.select_by_visible_text("Middle Class")

    # Select Family Values
    family_values_select = Select(driver.find_element(By.NAME, "family_values"))
    family_values_select.select_by_visible_text("Traditional")

    time.sleep(1)

    # Click the search button
    search_button = driver.find_element(By.CSS_SELECTOR, "button.search-button")
    search_button.click()

    # Wait for results to load
    time.sleep(3)

    # Check if results are found
    profiles = driver.find_elements(By.CLASS_NAME, "profile-card")
    if profiles:
        print(f"{len(profiles)} profile(s) found matching criteria.")
        for profile in profiles:
            print("-----")
            print(profile.text)
    else:
        no_result = driver.find_element(By.TAG_NAME, "p")
        print("No profiles found message:", no_result.text)

except Exception as e:
    print("Test failed:", str(e))

finally:
    driver.quit()
