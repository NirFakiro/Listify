
# This section of the code is where the POST request is triggered
# via the UI by interacting with the user interface.
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get(" http://localhost:5173/")
print("url: " + driver.current_url)
print("title: " + driver.title)
sleep(2)

add_user_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button')
add_user_button.click()
sleep(1)
user_name_filed = driver.find_element(By.XPATH, '//*[@id=":rk:"]')
sleep(1)
user_name_filed.send_keys('Testing')

add_user_button2 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]')
add_user_button2.click()
sleep(3)
driver.quit()