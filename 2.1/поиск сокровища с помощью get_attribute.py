from selenium import webdriver
from selenium.webdriver.common.by import By

import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()

try:
    driver.get("http://suninjuly.github.io/get_attribute.html")

    treasure = driver.find_element(By.ID, "treasure")
    value_x = treasure.get_attribute("valuex")

    x = value_x
    y = calc(x)

    text_area = driver.find_element(By.ID, "answer")
    text_area.send_keys(y)

    checkbox_robot = driver.find_element(By.ID, "robotCheckbox")
    checkbox_robot.click()

    radiobutton_robot = driver.find_element(By.ID, "robotsRule")
    radiobutton_robot.click()

    submit_btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_btn.click()

finally:
    time.sleep(5)

    driver.quit()

