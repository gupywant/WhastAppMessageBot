from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

try:
  # Text Message
  text = """Testing Message"""
  # destination number
  phone = "6285772293479"
  # Browser Driver
  browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
  wait = WebDriverWait(browser, 600)
  # Open WhatsApp Web For qr scanning
  browser.get("https://web.whatsapp.com/")
  input('Press something after scanning ')
  # sending message
  browser.get(f"https://web.whatsapp.com/send?phone={phone}&text={text}")
  print('Chatting.. ')
  textBox = "//div[@title='Type a message']"
  reply = wait.until(EC.presence_of_element_located((By.XPATH, textBox)))
  reply.send_keys(Keys.RETURN)
  print('Message sent.. ')
except Exception as e:
    print(e)
