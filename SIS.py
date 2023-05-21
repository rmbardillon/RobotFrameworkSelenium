from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Edge(executable_path="C:/Users/romsk/PycharmProjects/Robot Framework Selenium/venv/Scripts/msedgedriver.exe")

driver.get("https://sis2.pup.edu.ph/student/")

email = driver.find_element("id", "studno")
password = driver.find_element("id", "password")
email.send_keys("2019-00513-SR-0")
password.send_keys("Romsky@001")
month = Select(driver.find_element("id", "SelectMonth"))
day = Select(driver.find_element("id", "SelectDay"))
year = driver.find_element("xpath", "//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[3]/select[1]")
month.select_by_visible_text("July")
day.select_by_visible_text("30")
year.send_keys("2001")

element = driver.find_element("name", "Login")
element.click()
grades = driver.find_element("xpath", "//a[contains(text(),'Schedule')]")
grades.click()
