
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)

    y_element = browser.find_element(By.ID, "num2")
    y = int(y_element.text)

    res = x + y

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(res))



    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()