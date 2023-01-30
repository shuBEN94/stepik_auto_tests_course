from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import math



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 5).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), '$100'))

    book = browser.find_element(By.ID, "book")
    book.click()

    number_find = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = number_find.text
    y = calc(x)

    text_area = browser.find_element(By.CSS_SELECTOR, "#answer")
    text_area.send_keys(y)

    submit_btn = browser.find_element(By.ID, "solve")
    submit_btn.click()

finally:
    time.sleep(5)
    browser.quit()