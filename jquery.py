from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

year = "2020"
month = "August"
day = "23"

driver.switch_to.frame(0)

# driver.find_element(By.XPATH,'//input[@id="datepicker"]').send_keys('05/22/2021') #

driver.find_element(By.XPATH, '//input[@id="datepicker"]').click()
while True:
    month_text = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    year_text = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if month_text == month and int(year_text) == int(year):
        break
    else:
        if int(year_text) <= int(year):
            driver.find_element(By.XPATH, '//span[text()="Next"]').click()
        else:
            driver.find_element(By.XPATH, '//span[text()="Prev"]').click()

dates = driver.find_elements(By.XPATH, '//*[@id="ui-datepicker-div"]//tbody/tr/td')

for date in dates:
    if date.text == day:
        date.click()
time.sleep(5)