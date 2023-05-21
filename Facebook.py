from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Edge(executable_path="C:/Users/romsk/PycharmProjects/Robot Framework Selenium/venv/Scripts/msedgedriver.exe")

driver.get("https://web.facebook.com/?_rdc=1&_rdr")

email = driver.find_element("id", "email")
password = driver.find_element("id", "pass")
email.send_keys("rj.bardillon")
password.send_keys("Bardillon@001")
login = driver.find_element("name", "login")
login.click()
