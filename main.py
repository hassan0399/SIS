from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--window-size=1920x1080")

# Path to Chrome WebDriver
webdriver_path = "\chromedriver_win32\chromedriver.exe"  # Replace with the actual path to chromedriver executable

# Start Chrome browser
driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)

# Open the website
driver.get("https://sis.punjab.gov.pk/dashboard")

# Find and click on "Sanctioned Posts" tab
sanctioned_posts_tab = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "sanctioned_post-tab"))
)
sanctioned_posts_tab.click()

# Wait for page load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "non_teaching_sanctioned_summary"))
)

# Find and click on "Non-Teaching" tab
non_teaching_tab = driver.find_element(By.ID, "non_teaching_sanctioned_summary")
non_teaching_tab.click()

# Wait for page load or perform any additional actions
# ...

# Scrape the desired data from the page
# ...

# Close the browser
driver.quit()
