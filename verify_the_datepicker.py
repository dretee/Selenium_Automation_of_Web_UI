

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Accessing the dummy ticket webpage
driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/")
driver.maximize_window()

# Navigating to the booking page
driver.find_element(By.XPATH, "//span[text()='BUY TICKET']/parent::a").click()


# Accessing the input box
driver.find_element(By.XPATH, '//*[@id="dob"]').click()

yy_and_mm = {"2022": "0", "1990": "8", "2002": "3", "2005": "2"}

# year_list = ["2022", "0000", "1923", "2025"]
# month_list = ["Jan", "Sep", "Jul", "Feb"]
DD = ["12", "30", "26", "14"]


# Accessing the date picker and the dropdown option for the month and year selection for the depar
# Iterate through yy_and_mm
# dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a") #valid XPATH
for yy, mm in yy_and_mm.items():


    # Click on the month dropdown to open it
    driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[1]').click()

    # Select the month using the Select class
    month_options = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
    month_options.select_by_value(mm)
    time.sleep(3)
    # Click on the year dropdown to open it
    driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]').click()

    # Select the year using the Select class
    year_options = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
    year_options.select_by_value(yy)
    time.sleep(3)
    # Picking the date from the list DD
    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")))

    # for day in DD:
    #     for date in elements:
    #         if date.get_attribute("data-date") == day:
    #             date.click()
    #             print(f"Date {day} selected for year {yy} and month {mm}")
    #             driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[1]').clear()
    #             break

    for day in DD:
        date_found = False  # Flag to track if a date is found for the current day
        while not date_found:
            for date in elements:
                if date.get_attribute("data-date") == day:
                    date.click()
                    date_found = True  # Mark that a date has been found
                    print(f"Date {day} selected for year {yy} and month {mm}")
                    break  # Exit the inner loop after selecting a date
# Close the webdriver
driver.quit()
