import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

# Open the webpage
driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/")
driver.maximize_window()
yy = "1996"
mm = "7"
num_day = "1"  # day of birth in the month

# Navigating to the booking page
driver.find_element(By.XPATH, "//span[text()='BUY TICKET']/parent::a").click()


# Accessing the input box
driver.find_element(By.XPATH, '//*[@id="dob"]').click()


# Accessing the date picker and the dropdown option for the month and year selection for the depar
# Choose through yy and mm


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
elements = wait.until(
    EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")))

for date in elements:
    if date.get_attribute("data-date") == num_day:
        date.click()
        print(f"Date {num_day} selected for year {yy} and month number {mm}, where the months start with index 0")
        break

driver.quit()
