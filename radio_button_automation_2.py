import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

# Open the webpage
driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/")
driver.maximize_window()
num_day = "1"  # day of birth in the month

# Navigating to the booking page
driver.find_element(By.XPATH, "//span[text()='BUY TICKET']/parent::a").click()  # click on the BUY NOW button


# Function to test gender radio buttons
def test_gender_radio_buttons():
    male_rd = driver.find_element(By.XPATH, "//input[@id='sex_1']")
    female_rd = driver.find_element(By.XPATH, "//input[@id='sex_2']")

    if male_rd.is_enabled() and female_rd.is_enabled():
        print("The male radio button is enabled")
        print("The female radio button is enabled")
    else:
        print("They are not enabled")

    male_rd.click()

    if male_rd.is_selected():
        print("The male radio button is selected, and the female should be false")
        print(f"The female button should be, {female_rd.is_selected()}")
    else:
        print("Something is wrong")

    female_rd.click()

    if female_rd.is_selected():
        print("The female radio button is selected, and the male should be false")
        print(f"The male button should be, {male_rd.is_selected()}")
    else:
        print("Something is wrong")


# Function to test trip type radio buttons
def test_trip_type_radio_buttons():
    one_way_trip_rd = driver.find_element(By.XPATH, "//input[@id='traveltype_1']")
    round_trip_rd = driver.find_element(By.XPATH, "//input[@id='traveltype_2']")

    if one_way_trip_rd.is_enabled() and round_trip_rd.is_enabled():
        print("The one-way trip radio button is enabled")
        print("The round trip radio button is enabled")
    else:
        print("They are not enabled")

    one_way_trip_rd.click()

    if one_way_trip_rd.is_selected():
        print("The one-way trip radio button is selected, and the round trip should be false")
        print(f"The round trip radio should be, {round_trip_rd.is_selected()}")
    else:
        print("Something is wrong")

    round_trip_rd.click()

    if round_trip_rd.is_selected():
        print("The round trip radio button is selected, and the one-way trip should be false")
        print(f"The one-way trip radio should be, {one_way_trip_rd.is_selected()}")
    else:
        print("Something is wrong")


if __name__ == "__main__":
    # Rest of your code

    # Call the gender radio button test function
    test_gender_radio_buttons()

    # Call the trip type radio button test function
    test_trip_type_radio_buttons()

    

