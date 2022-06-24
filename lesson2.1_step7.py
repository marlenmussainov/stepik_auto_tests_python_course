from selenium import webdriver
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_xpath("//*[@id='treasure']")
x = x_element.get_attribute('valuex')
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
browser.find_element_by_xpath("//*[@id='robotCheckbox']").click()
browser.find_element_by_xpath("//*[@id='robotsRule']").click()
browser.find_element_by_xpath("//*[@type='submit']").click()
