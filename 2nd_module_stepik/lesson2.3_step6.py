from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element(By.XPATH, "//button[@type = 'submit']")
    button.click()

    new_window = browser.window_handles[1]
    window = browser.switch_to.window(new_window)

    x1 = browser.find_element(By.ID, "input_value")
    x = x1.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button2 = browser.find_element(By.XPATH, "//button[@type = 'submit']")
    button2.click()


finally:
    time.sleep(3)

    print(browser.switch_to.alert.text)

    browser.quit()