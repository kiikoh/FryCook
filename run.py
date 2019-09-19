from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random as r
import time
from datetime import datetime, timedelta
now = datetime.now()
storeNum = 1345
# 1 = before 11
# 2 = before 1
# 3 = before 5
# 4 = before 7
# 5 = after 7
timeSlot = 4
date = now - timedelta(days=4)
date = "\'" + date.strftime("%m/%d/%Y") + "\'"
checkId = 37


def chooseAnswer(begin, end=None):
    if end == None:
        end = begin
    driver.execute_script(
        "document.getElementsByClassName('ui-radio')[{}].children[1].click()".format(r.randint(begin, end)))


def nextQuestion():
    driver.find_element_by_xpath(
        "/html/body/div[1]/section/div/form/nav/div/div[2]/input").click()


def getCode():
    timeBegin = time
    driver.get("https://smashburgerfeedback.survey.marketforce.com/")
    # Enter store id
    driver.find_element_by_id("EntryCode").send_keys(str(storeNum))
    # Enter date
    driver.execute_script(
        "document.getElementById('DateOfVisit').value = " + date)
    # Enter Time
    # driver.find_element_by_id("TimeOfVisit-button").click()
    select = Select(driver.find_element_by_id('TimeOfVisit'))
    select.select_by_value(str(timeSlot))
    # Enter Check ID
    driver.find_element_by_id("CheckNum").send_keys(str(checkId))
    # Start button
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div/div/form/div/div[5]").click()
    # Begin Survey
    driver.find_element_by_xpath(
        "/html/body/div[1]/section/div/form/div/input").click()
    # Pick an answer randomly
    chooseAnswer(0, 4)
    nextQuestion()
    driver.execute_script("document.getElementById('scaleConfirmed').click()")
    time.sleep(1.5)
    chooseAnswer(0, 5)
    chooseAnswer(7)
    nextQuestion()
    chooseAnswer(4)
    nextQuestion()
    chooseAnswer(0, 4)
    chooseAnswer(5, 9)
    chooseAnswer(14)
    nextQuestion()
    chooseAnswer(0)
    nextQuestion()
    chooseAnswer(0, 4)
    chooseAnswer(5, 9)
    nextQuestion()
    chooseAnswer(1)
    nextQuestion()
    chooseAnswer(0, 5)
    chooseAnswer(6, 10)
    chooseAnswer(11, 13)
    chooseAnswer(14, 15)
    nextQuestion()
    chooseAnswer(0, 4)
    nextQuestion()
    chooseAnswer(1)
    chooseAnswer(3)
    nextQuestion()
    chooseAnswer(0, 1)
    chooseAnswer(3, 8)
    nextQuestion()
    print(driver.find_element_by_xpath(
        "/html/body/div[1]/section/div/section/h2/p[2]/span/strong/span").text)
    driver.close()


while True:
    driver = webdriver.Firefox()
    getCode()
