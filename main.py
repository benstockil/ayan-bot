from selenium import webdriver
import math, numpy
from bisect import bisect_left

from sympy.ntheory import factorint

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
chromeOptions.add_argument("--start-fullscreen")
driver = webdriver.Chrome(options=chromeOptions)
driver.implicitly_wait(0)

driver.get('https://isthisprime.com/game/')
driver.find_element_by_id("start").click()

numElem = driver.find_element_by_id("n")
yesElem = driver.find_element_by_id("yes")
noElem = driver.find_element_by_id("no")

while True:
    number = int(numElem.text)
    if factorint(number) == {number: 1}:
        yesElem.click()
    else:
        noElem.click()