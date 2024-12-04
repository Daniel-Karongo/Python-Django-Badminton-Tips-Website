import os
from selenium import webdriver

os.environ['PATH'] += r"D:\Projects\Python\Django Framework\Project001"
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")

driver.implicitly_wait(4)

my_element = driver.find_element_by_tag_name('a')

my_element.click()