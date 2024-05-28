from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    numb1 = browser.find_element(By.ID, "num1")
    x = numb1.text
    z = int(x)
    numb2 = browser.find_element(By.ID, "num2")
    y = numb2.text
    v = int(y)

    sum_value = str(z + v)

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(sum_value))

    button = browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()