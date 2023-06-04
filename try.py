import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

service = Service('chromedriver_win32\chromedriver.exe')  # Replace with the path to your chromedriver executable
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)
# Open the desired URL
driver.get("https://sis.punjab.gov.pk/dashboard#")
time.sleep(10)


# Click on "Sanctioned Posts"
sanctioned_posts = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Sanctioned Posts"]')))
sanctioned_posts.click()
time.sleep(5)

# Wait for the page to load
wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="Non-Teaching"]')))

# Click on "Non-Teaching"
non_teaching = driver.find_element(By.XPATH, '//a[text()="Non-Teaching"]')
non_teaching.click()
time.sleep(5)
# Find the text box by its ID and fill it with the desired value
text_box = driver.find_element(By.ID,'sanctioned_posts_form')
text_box = text_box.find_element(By.ID,'emis_code')
text_box.click()
text_box.clear()
text_box.send_keys("34220014")

# Submit the form (assuming it's triggered by pressing Enter)
text_box.send_keys(Keys.RETURN)
time.sleep(10)
# Close the browser
driver.quit()
