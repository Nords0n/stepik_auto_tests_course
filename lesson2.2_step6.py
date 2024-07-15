from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x1 = browser.find_element(By.ID, "input_value")
    x = x1.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)


    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()
    input3 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);",input3) #Скролим до радио и нажимаем затем
    input3.click()

    button = browser.find_element(By.XPATH, "//button[@type = 'submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) #Скролим до кнопки и нажимаем по кнопке
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()