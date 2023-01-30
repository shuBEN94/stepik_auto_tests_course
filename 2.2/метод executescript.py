import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()


def function(n):
    return str(math.log(abs(12 * math.sin(int(n)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x_value = browser.find_element(By.ID, "input_value")
    x = x_value.text
    answer = function(x)

    answer_field = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
    answer_field.send_keys(answer)

    checkbox_robot = browser.find_element(By.ID, "robotCheckbox")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox_robot)
    checkbox_robot.click()

    radio_robots = browser.find_element(By.ID, "robotsRule")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", radio_robots)
    radio_robots.click()

    submit_btn = browser.find_element(By.XPATH, "/html/body/div[1]/form/button")
    browser.execute_script("window.scrollBy(0, 150);")
    submit_btn.click()

finally:
    time.sleep(5)
    browser.quit()



