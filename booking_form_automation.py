from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Accessing the dummy ticket webpage
driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/")
driver.maximize_window()

# Navigating to the booking page
driver.find_element(By.XPATH, "//span[text()='BUY TICKET']/parent::a").click()

# Initialize the WebDriverWait
wait = WebDriverWait(driver, 10)

# Define the chosen country and state
country_chosen = "Nigeria"
state_chosen = "Niger"

# Function to fill billing details
driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("0813336325")
driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("anthonyandre008@gmail.com")
driver.find_element(By.XPATH, "//input[@id='billname']").send_keys("UyahsHOUSING")
driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("No 1 dosunmu close")
driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("Agbara")
time.sleep(3)

# Click to open the country dropdown
country_dropdown = driver.find_element(By.XPATH, "//span[@aria-label='Country']//b[@role='presentation']")
country_dropdown.click()

# Wait for the country list to be visible
wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='select2-container select2-container--default select2-container--open']//ul/li")))

# Get the list of countries
countries = driver.find_elements(By.XPATH, "//span[@class='select2-container select2-container--default select2-container--open']//ul/li")

# Iterate through the countries and select the chosen one
for country in countries:
    if country.text == country_chosen:
        country.click()
        break
time.sleep(5)

# Get the displayed text for the chosen country
displayed_text_country = driver.find_element(By.XPATH, '//*[@id="select2-billing_country-container"]').text

# Click to open the state dropdown
state_dropdown = driver.find_element(By.XPATH, "(//b[@role='presentation'])[8]")
state_dropdown.click()


# Get the list of states
states = driver.find_elements(By.XPATH, "//span[@class='select2-dropdown select2-dropdown--above']//ul/li")

# Iterate through the states and select the chosen one
for state in states:
    if state.text == state_chosen:
        state.click()
        break

# Get the displayed text for the chosen state
displayed_text_state = driver.find_element(By.XPATH, "//span[@id='select2-billing_state-container']").text

# Check if the chosen country and state correspond to the displayed text
if country_chosen == displayed_text_country and state_chosen == displayed_text_state:
    print(f"The chosen state {state_chosen} corresponds to the displayed text {displayed_text_state}")
    print(f"The chosen country {country_chosen} corresponds to the displayed text {displayed_text_country}")

# Quit the driver
driver.quit()
