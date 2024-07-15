from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    picture = browser.find_element(By.ID, "treasure")
    x = picture.get_attribute("valuex")

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()
    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click()
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()