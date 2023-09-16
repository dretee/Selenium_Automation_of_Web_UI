from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the webpage
driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Navigating to the booking page
driver.find_element(By.XPATH, "//span[text()='BUY TICKET']/parent::a").click()

# Wait for the visibility of all radio buttons
rd_buttons = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//input[@name='add_to_cart']")))

for count, rd_button in enumerate(rd_buttons, start=1):
    rd_button.click()

    # Find all the text elements inside the selected radio button
    rd_texts = driver.find_elements(By.XPATH, '//ul[@id="checkout-products"]//span[@class="woocommerce-Price-amount amount"]')

    checkout_price = driver.find_element(By.XPATH, "//tr[@class='order-total']//span[@class='woocommerce-Price-amount amount']").text
    match_found = False

    for rd_text in rd_texts:
        if rd_text.text == checkout_price:
            match_found = True
            print(f"The checkout price {checkout_price} corresponds to the {rd_text.text} for radio button {count}")
            break

    if not match_found:
        print(f"Price mismatch for radio button {count}")

driver.quit()
