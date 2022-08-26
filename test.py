import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

site_url = "https://siddhantwadhwani.com"

# Remote Selenium Grid URL
selenium_grid_url = f"<SELENIUM-GRID-URL>"

try:
    # Browser Instantiation on Selenium Grid 4.4.0
    options = ChromeOptions()
    options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-full-screen")
    options.add_argument("--incognito")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Remote(
        command_executor=selenium_grid_url,
        options=options
    )
    driver.implicitly_wait(20)
    driver.maximize_window()

    # Visit the Website URL
    driver.get(site_url)
    print("Navigating to page: " + site_url)

    # Fetch Title of the Webpage
    get_title = driver.title
    print("Title of webpage: " + get_title)

    # Fetch Web Links count
    links = driver.find_elements(By.XPATH, "//a")
    print("Total number of links on page: " + str(len(links)))

finally:
    driver.quit()
