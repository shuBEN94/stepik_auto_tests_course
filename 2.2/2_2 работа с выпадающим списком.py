from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(number1, number2):
    return str(int(number1) + int(number2))  # находим сумму чисел и переводим в текстовый формат


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/selects1.html")

    num1 = browser.find_element(By.ID, "num1")  # находим 1 число
    num2 = browser.find_element(By.ID, "num2")  # находим 2 число

    n1 = num1.text
    n2 = num2.text

    summa = calc(n1, n2)  # считаем сумму чисел

    select = Select(browser.find_element(By.ID, "dropdown"))  # находим список
    select.select_by_visible_text(summa)  # выбираем значение соответствующее полученной сумме

    submit_btn = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    submit_btn.click()

finally:
    time.sleep(5)

    browser.quit()
