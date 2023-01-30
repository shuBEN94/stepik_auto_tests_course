from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()

try:
    driver.get("https://suninjuly.github.io/math.html")

    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    text_area = driver.find_element(By.CSS_SELECTOR, "#answer")
    text_area.send_keys(y)

    checkbox_robot = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox_robot.click()

    radiobutton_robot = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton_robot.click()

    submit_btn = driver.find_element(By.XPATH, "/html/body/div/form/button")
    submit_btn.click()

finally:
    time.sleep(5)

    driver.quit()
