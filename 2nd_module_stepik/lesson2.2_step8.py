from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time
import os

try:
    fake = Faker()
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/file_input.html"
    browser.get(link)

    with open('hewwo.txt', "w") as file:
        content = file.write("chtoto")

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys(fake.first_name())
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys(fake.last_name())
    email1 = browser.find_element(By.NAME, "email")
    email1.send_keys(fake.ascii_free_email())

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "hewwo.txt"
    file_path = os.path.join(current_dir, file_name)
    upload_btn = browser.find_element(By.NAME, "file")
    upload_btn.send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[@type = 'submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()