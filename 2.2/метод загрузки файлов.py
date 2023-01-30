# import os
#
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'test_doc.txt')           # добавляем к этому пути имя файла
# # element.send_keys(file_path)

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    first_name_field = browser.find_element(By.NAME, "firstname")
    first_name_field.send_keys("Alex")

    last_name_field = browser.find_element(By.NAME, "lastname")
    last_name_field.send_keys("Man")

    email_field = browser.find_element(By.NAME, "email")
    email_field.send_keys("AlexMan@ya.ru")

    file_load = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test_doc.txt')     # добавляем к этому пути имя файла
    file_load.send_keys(file_path)  # отправляем файл

    submit_btn = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()

