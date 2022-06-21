from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException

from ticketClass import createTicket


options = webdriver.ChromeOptions()
PATH = "C:/Program Files (x86)/chromedriver.exe"
DRIVER = webdriver.Chrome(PATH)
TN_LOTTERY_WEBSITE = 'https://tnlottery.com/games/instant-games/'

WAIT = WebDriverWait(DRIVER, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
