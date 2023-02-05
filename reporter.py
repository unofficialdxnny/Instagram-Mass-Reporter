from pystyle import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

from time import sleep
import keyboard as kb
import os
import json
import undetected_chromedriver as uc




os.system('cls & title Instagram Reporter ~ unofficialdxnny')

config = open('config.json', 'r')
data = json.load(config)

username_report = input("Username > ")

options = Options()
options.page_load_strategy = 'eager'
options.headless = False
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--log-level=OFF")
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options) 
driver.get(f'https://www.instagram.com/accounts/login/?next=%2F{username_report}%2F&source=desktop_nav')
## driver.maximize_window()
wait = WebDriverWait(driver, 100)

print('Logging into Instagram')


cookies = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]")))
cookies.click()

username = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")))

username.clear()
username.send_keys(data["username"])

password = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")))
password.clear()
password.send_keys(data["password"])


login = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button")))
login.click()


save_login_info = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")))
save_login_info.click()


while True:
    more = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div/button")))
    more.click()


    report = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]")))
    report.click()

    report_acc = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]/div/div[1]")))
    report_acc.click()

    second = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[2]/div/div[1]")))
    second.click()

    me = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/fieldset/div[1]/label")))
    me.click()

    submit = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[6]/button")))
    submit.click()

    close = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div[4]")))
    close.click()