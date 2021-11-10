# Importerer drivere
import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Starter Chromium i incognito kiosk modus
chromeoptions = Options()
chromeoptions.add_argument("--incognito")
chromeoptions.add_argument("--kiosk")
chromeoptions.add_experimental_option("excludeSwitches", ["enable-automation"])
chromeoptions.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', 0, chromeoptions)

# Hva scriptet skal se etter for å fylle ut påloggingsinformasjon
BRUKER_FELT = (By.XPATH, "XPATH bane")
PASSORD_FELT = (By.XPATH, "XPATH bane")
KNAPP = (By.XPATH, "XPATH bane")

# Nettside samt utførelse av pålogging
driver.get(config.link)
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(BRUKER_FELT)).send_keys(config.username)
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(PASSORD_FELT)).send_keys(config.password)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(KNAPP)).click()