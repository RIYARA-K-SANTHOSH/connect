from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the blog create page
driver.get("http://127.0.0.1:8000/blogs/create/")  # Adjust URL as needed

try:
    # Wait for the form to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "form"))
    )

    # Fill out the blog form (without image)
    title_input = driver.find_element(By.ID, "id_title")
    title_input.send_keys("Test Blog Title")

    content_input = driver.find_element(By.ID, "id_content")
    content_input.send_keys("This is the content of the test blog post created using Selenium.")

    # Submit the form
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Wait until the new blog post appears in the blog list
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "blog-card"))
    )

    # Verify the newly created blog title
    blog_titles = driver.find_elements(By.CSS_SELECTOR, ".blog-card .blog-content h3")
    titles = [title.text for title in blog_titles]

    if "Test Blog Title" in titles:
        print("✅ Blog created successfully!")
    else:
        print("❌ Blog creation failed.")

except Exception as e:
    print(f"⚠️ An error occurred: {e}")

finally:
    time.sleep(3)
    driver.quit()
