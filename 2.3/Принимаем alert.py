from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    button_1 = browser.find_element(By.CSS_SELECTOR, "button")
    button_1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    number_find = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = number_find.text
    y = calc(x)

    text_area = browser.find_element(By.CSS_SELECTOR, "#answer")
    text_area.send_keys(y)

    submit_btn = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_btn.click()

finally:
    time.sleep(5)
    browser.quit()







