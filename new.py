import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Set up Selenium webdriver
service = Service('chromedriver_win32\chromedriver.exe')  # Replace with the path to your chromedriver executable
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# Open the URL
driver.get('https://sis.punjab.gov.pk/dashboard')
time.sleep(5)

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

# Get the page source after all the interactions
page_source = driver.page_source

# Close the browser
# driver.quit()

# Process the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find the table by class name
table = soup.find('table', class_='table table-striped table-bordered table-hover table-highlight table-checkable sanctioned-post-table mt-10')

table_header = [cell.get_text(strip=True) for cell in table.find_all('th')]

# Extract table data into a list of lists
table_data = []
for row in table.find_all('tr'):
    row_data = [cell.get_text(strip=True) for cell in row.find_all('td')]
    table_data.append(row_data)

table_data[0] = table_header

# Create a DataFrame from the table data
df = pd.DataFrame(table_data[1:], columns=table_data[0])

col_name = list(df.iloc[:, 1])
col_name = col_name[:-1]

VP_col = []
for col in col_name:
    VP_col.extend([col + '_total', col + '_vacant', col + '_filled'])

vacancy = pd.read_csv('Vacancy.csv',low_memory=False, index_col=0)


# Check column names and match with VP_col list
for col in vacancy.columns:
    if col not in VP_col:
        VP_col.append(col)

# Filter out columns present in VP_col
# vacancy = vacancy[VP_col]



# Save EMIS column values in emis list
# emis = vacancy['EMIS'].tolist()

# Print the updated DataFrame and the emis list

# print(emis)


def add_column_if_not_exists(df, column_name, default_value=None):
    if column_name not in df.columns:
        df[column_name] = default_value


for i in VP_col:
    add_column_if_not_exists(vacancy, i, default_value=0)
print(vacancy)
vacancy.to_csv('Vacancy.csv',mode='w', index=True, header=True)
print(vacancy)