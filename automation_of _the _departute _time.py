
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Open the webpage using Chrome driver
driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/")
driver.maximize_window()

# Initialize WebDriverWait with a 10-second timeout
wait = WebDriverWait(driver, 10)

try:
    # Navigating to the booking page
    buy_ticket_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='BUY TICKET']/parent::a")))
    buy_ticket_button.click()

    # Function to select departure time
    # Click on the "Depart On" input field to open the date picker
    depart_on_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='departon']")))
    depart_on_field.click()

    # Define the desired day, month, and year for departure
    day_of_departure = "1"
    month_of_departure = "3"
    year_of_departure = "2024"

    # Click on the year dropdown to open it for departure selection
    year_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]')))
    year_element.click()

    # Wait for the year dropdown to be visible and select the desired year
    depart_year_select = Select(driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]'))
    depart_year_select.select_by_value(year_of_departure)

    # Click on the month dropdown to open it for departure selection
    month_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[1]')))
    month_element.click()

    # Select the desired month from the dropdown for departure
    depart_month_select = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
    depart_month_select.select_by_value(month_of_departure)

    # Select the day in the date picker
    day_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
    for day in day_dates:
        if day.text == day_of_departure:
            day.click()
            print(f"Date {day_of_departure} selected for year {year_of_departure} and month {month_of_departure}")
            break
    else:
        print(f"Date {day_of_departure} not found in the date picker.")
except (TimeoutException, NoSuchElementException) as e:
    print(f"An error occurred: {e}")

# Close the webdriver
driver.quit()
