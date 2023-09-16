from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Microsoft Edge WebDriver
driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/")
driver.maximize_window()

# Navigating to the booking page
driver.find_element(By.XPATH, "//span[text()='BUY TICKET']/parent::a").click()

# Define XPaths for the radio buttons
radio_button_xpath = [
    "//input[@id='product_549']",  # Dummy_ticket_for_Visa_Application
    "//input[@id='product_550']",  # Dummy_return_ticket
    "//input[@id='product_551']",  # Dummy_hotel_booking
    "//input[@id='product_3186']",  # Dummy_ticket_and_hotel
    "//input[@id='product_7441']"  # Past_dated_ticket
]

radio_button_xpaths = {
    'Dummy_ticket_for_Visa_Application': "//input[@id='product_549']",
    'Dummy_return_ticket': "//input[@id='product_550']",
    'Dummy_hotel_booking': "//input[@id='product_551']",
    'Dummy_ticket_and_hotel': "//input[@id='product_3186']",
    'Past_dated_ticket': "//input[@id='product_7441']"
}
# Check and print the selected status of each radio button
print('The radio button will be true if enabled')
print('')
for name, xpath in radio_button_xpaths.items():
    radio_button = driver.find_element(By.XPATH, xpath)
    is_enabled = radio_button.is_enabled()
    print(f"{name} radio button : {is_enabled}")

print('')
print("")
count = 0
for x_path in radio_button_xpath:
    driver.find_element(By.XPATH, x_path).click()
    count += 1
    print("")
    print(f"{count})", "The radio button will be true if selected and the others should be false")
    print("")
    for name, xpath in radio_button_xpaths.items():
        radio_button = driver.find_element(By.XPATH, xpath)
        is_selected = radio_button.is_selected()
        print(f"{name} radio button : {is_selected}")

# Close the webdriver
driver.quit()
