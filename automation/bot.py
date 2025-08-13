from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import date

CHROME_DRIVER_PATH = "/usr/local/bin/chromedriver"

OP = webdriver.ChromeOptions()
# OP.add_argument('--headless')  

service = Service(executable_path=CHROME_DRIVER_PATH)

DRIVER = webdriver.Chrome(service=service, options=OP)


class AutomationWeb:
    def __init__(self, EMAIL, PASSWORD, LINK_LOGIN):
        self.email = EMAIL
        self.password = PASSWORD
        self.link_login = LINK_LOGIN
        
    def login(self):
        try:
            DRIVER.get(self.link_login)
            
            time.sleep(5)
            username = DRIVER.find_element(By.CSS_SELECTOR, value="input[name='username']")
            password = DRIVER.find_element(By.CSS_SELECTOR, value="input[name='password']")
            continue_btn = DRIVER.find_element(By.ID, value="login-submit")

            # send keys email
            username.send_keys(self.email)
            time.sleep(2)

            # klik button
            continue_btn.click()
            time.sleep(2)

            # send keys password
            password.send_keys(self.password)
            time.sleep(3)

            # klik button
            continue_btn.click()
            time.sleep(10)
            
        except Exception as e:
            print(f"kesalahan {e}")
            DRIVER.close()
            
    def make_board(self):
        
        try:
            time.sleep(2)
            button_create_board = DRIVER.find_element(By.CSS_SELECTOR, value="[data-testid='create-board-tile']")
            time.sleep(4)
            button_create_board.click()
            time.sleep(5)
            
            board_title = DRIVER.find_element(By.CSS_SELECTOR, value="[data-testid='create-board-title-input']")
            board_title.send_keys("Board Testing")
            time.sleep(3)

            create_btn_final = DRIVER.find_element(By.CSS_SELECTOR, value="[data-testid='create-board-submit-button']")
            create_btn_final.click()
            time.sleep(5)
        
        except Exception as e:
            print(f"kesalahan {e}")

            
            
            
    