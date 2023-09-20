# Selenium_Automation_of_Web_UI
# Dummy Ticket Automation Scripts

This repository contains a collection of Python scripts that automate various tasks on the Dummy Ticket website using Selenium WebDriver. Dummy Ticket is a fictitious website for generating dummy flight tickets for purposes such as visa applications and travel planning.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Scripts](#scripts)
  - [Script 1: Booking a Ticket](#script-1-booking-a-ticket)
  - [Script 2: Filling Billing Details](#script-2-filling-billing-details)
  - [Script 3: Testing Gender and Trip Type Radio Buttons](#script-3-testing-gender-and-trip-type-radio-buttons)
  - [Script 4: Selecting Dates for Multiple Years](#script-4-selecting-dates-for-multiple-years)
  - [Script 5: Matching Prices for Radio Buttons](#script-5-matching-prices-for-radio-buttons)
- [Usage](#usage)
- [License](#license)

## Overview

These automation scripts are designed to streamline the process of interacting with the Dummy Ticket website. Each script targets specific functionality and can be used individually or in combination as needed.

## Requirements

To run the scripts in this repository, you need the following:

- Python (3.x recommended)
- Selenium WebDriver
- Chrome WebDriver (for Chrome browser automation)
- Chrome browser installed

## Scripts

### Script 1: Booking a Ticket

- Script File: [book_ticket.py](book_ticket.py)
- Description: This script automates the process of booking a ticket on the Dummy Ticket website. It navigates to the booking page, selects a departure date using a date picker, and handles exceptions.

### Script 2: Filling Billing Details

- Script File: [fill_billing_details.py](fill_billing_details.py)
- Description: This script automates the process of filling in billing details when booking a ticket on the Dummy Ticket website. It selects a country and state, enters phone and email information, and verifies the selections.

### Script 3: Testing Gender and Trip Type Radio Buttons

- Script File: [test_radio_buttons.py](test_radio_buttons.py)
- Description: This script tests the functionality of gender and trip type radio buttons on the Dummy Ticket website. It verifies if the buttons are enabled, selects them, and checks their states.

### Script 4: Selecting Dates for Multiple Years

- Script File: [select_dates_for_multiple_years.py](select_dates_for_multiple_years.py)
- Description: This script demonstrates how to select departure dates for multiple years using the Dummy Ticket website's date picker.

### Script 5: Matching Prices for Radio Buttons

- Script File: [match_radio_button_prices.py](match_radio_button_prices.py)
- Description: This script verifies if the prices associated with radio buttons on the Dummy Ticket website match the total checkout price.

## Usage

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/your-username/dummy-ticket-automation.git
   ```

2. Install Python if not already installed. You can download it from the [official Python website](https://www.python.org/downloads/).

3. Install Selenium WebDriver:

   ```shell
   pip install selenium
   ```

4. Download the Chrome WebDriver from the [official website](https://sites.google.com/chromium.org/driver/). Ensure that the WebDriver version matches your Chrome browser version.

5. Place the Chrome WebDriver executable in a directory included in your system's PATH.

6. Open the desired Python script(s) and modify any necessary variables, such as departure date, month, year, etc.

7. Run the Python script(s) to automate the corresponding tasks:

   ```shell
   python script_name.py
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Note:** This project is for educational and testing purposes only. Ensure that you comply with the terms and conditions of any website you interact with using automation tools.
