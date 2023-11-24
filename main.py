import datetime
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

current_time = datetime.datetime.now().time()
while current_time.hour != 7:
    time.sleep(1)

start_time = time.time()
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')
yandex_options = Options()
yandex_options.page_load_strategy = 'eager'
yandex_options.add_experimental_option('detach', True)
yandex_service = Service()
yandex_service.path = BASE_DIR / 'yandexdriver'
delay = 10
driver = webdriver.Chrome(yandex_options, yandex_service, keep_alive=True)

driver.get('https://passport.yandex.ru/auth?origin=music_button-header&retpath=https%3A%2F%2Fmusic.yandex.ru%2Fsettings%3Ffrom-passport')
select_email_login_button = WebDriverWait(driver, delay, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[1]/button')))
select_email_login_button.click()
login_input = WebDriverWait(driver, delay, poll_frequency=1).until(EC.element_to_be_clickable((By.ID, 'passp-field-login')))
login_input.click()
login_input.clear()
login_input.send_keys(os.getenv('YANDEX_LOGIN'))
login_button = WebDriverWait(driver, delay, poll_frequency=1).until(EC.element_to_be_clickable((By.ID, 'passp:sign-in')))
login_button.click()
password_input = WebDriverWait(driver, delay, poll_frequency=1).until(EC.element_to_be_clickable((By.ID, 'passp-field-passwd')))
password_input.click()
password_input.clear()
password_input.send_keys(os.getenv('YANDEX_PASSWORD'))
login_button = WebDriverWait(driver, delay, poll_frequency=1).until(EC.element_to_be_clickable((By.ID, 'passp:sign-in')))
login_button.click()

# collection_link = driver.find_element(By.XPATH, '/html/body/div[1]/div[12]/div/div/div[2]/div[1]/div/a[4]')
# collection_link.click()
# fav_collection_link = WebDriverWait(driver, delay, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[14]/div[2]/div/div/div[3]/div[2]/div/div[1]/div[1]/div[3]/div/span/a')))
# fav_collection_link.click()
driver.get('https://music.yandex.ru/users/vasil1y.nikulin/playlists/3')
driver.refresh()
driver.refresh()

favourite_playlist_play_button = WebDriverWait(driver, delay, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[14]/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/button')))
favourite_playlist_play_button.click()
random_order_button = WebDriverWait(driver, delay, poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[18]/div[1]/div[2]/div[9]/div[2]/div')))
random_order_button.click()

print("--- %s seconds ---" % (time.time() - start_time))
