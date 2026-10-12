from selenium import webdriver
from selenium.webdriver.common.by import By  
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from FixHuawei import FixMe
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from HuaweiStriper import stripper
from MatcherHuawei import get_names_for_mac_addresses
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import traceback
from datetime import datetime
import socket
chrome_options = Options()
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
def get_device_name():
    try:
        # Get the device name (hostname)
        device_name = socket.gethostname()
        return device_name
    except socket.error as e:
        print(f"Error getting device name: {e}")
        return None

def get_local_ip():
    try:
        # Get a list of IP addresses associated with the local host
        ip_list = socket.gethostbyname_ex(socket.gethostname())[2]

        # Filter out local and loopback addresses
        local_ip = [ip for ip in ip_list if not ip.startswith("127.") and not ip.startswith("169.254.")][0]
        return local_ip
    except socket.error as e:
        print(f"Error getting local IP address: {e}")
        return None

def get_current_time():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d | %H:%M:%S")
    return formatted_time

# Example usage
current_time_value = get_current_time()
print("Current Time:", current_time_value)

# Login
def SignIn(driver):
 driver.get('http://192.168.100.1')
 Username = driver.find_element(By.XPATH, '//*[@id="txt_Username"]')
 Username.send_keys('telecomadmin')
 Password = driver.find_element(By.XPATH, '//*[@id="txt_Password"]')
 Password.send_keys('admintelecom')
 Login = driver.find_element(By.XPATH, '//*[@id="button"]')
 Login.click()
 time.sleep(2)
 # Gets the mac addresses of connected devices along with their name
def dhcplist1():
 num = 1
 driver = webdriver.Chrome(options=chrome_options)
 SignIn(driver)
 driver.get("http://192.168.100.1/html/bbsp/common/GetLanUserDhcpInfo.asp")

 body_text = driver.find_element(By.TAG_NAME, "body").text

 data = FixMe(body_text)
 processeddata = ('\n'.join(data))
 return processeddata
 # Turns filter on
def dhcpnamestripper():
 num = 1
 driver = webdriver.Chrome(options=chrome_options)
 SignIn(driver)
 driver.get("http://192.168.100.1/html/bbsp/common/GetLanUserDhcpInfo.asp")

 body_text = driver.find_element(By.TAG_NAME, "body").text

 data = FixMe(body_text)
 unstripped_data = ('\n'.join(data))
 return unstripped_data

def on1():
 
 driver = webdriver.Chrome(options=chrome_options)
 SignIn(driver)
 time.sleep(2)
 driver.find_element(By.XPATH, '//*[@id="headerTab"]/ul/li[6]/div[2]').click()
 time.sleep(2)
 driver.find_element(By.CSS_SELECTOR, '#nav > ul > li:nth-child(4)').click()
 time.sleep(2)
 driver.find_element(By.ID, 'frameContent')
 driver.switch_to.frame('frameContent')
 Checkbox = driver.find_element(By.XPATH, '//*[@id="EnableMacFilter"]')
 
 if Checkbox.is_selected():
  Message = ("Mac filter is already on.")
 else:
  Checkbox.click()
  Message = ("Mac filter has been turned on.")
 time.sleep(1) 
 return Message 
# Turns filter off
def off2():
 driver = webdriver.Chrome(options=chrome_options)
 SignIn(driver)
 time.sleep(2)
 driver.find_element(By.XPATH, '//*[@id="headerTab"]/ul/li[6]/div[2]').click()
 time.sleep(2)
 driver.find_element(By.CSS_SELECTOR, '#nav > ul > li:nth-child(4)').click()
 time.sleep(2)
 iframe = driver.find_element(By.ID, 'frameContent')
 driver.switch_to.frame('frameContent')
 Checkbox = driver.find_element(By.XPATH, '//*[@id="EnableMacFilter"]')
 
 if Checkbox.is_selected():
   Checkbox.click()
   Message1 = "Turned Mac filter off."
 else:
   Message1 = "It's already off."
 time.sleep(1)  
 return Message1

def get_mac_whitelist():
 num = -1
 num2 = -1
 abcd = []
 driver = webdriver.Chrome(options=chrome_options)
 SignIn(driver)
 time.sleep(2)
 driver.find_element(By.XPATH, '//*[@id="headerTab"]/ul/li[6]/div[2]').click()
 time.sleep(2)
 driver.find_element(By.CSS_SELECTOR, '#nav > ul > li:nth-child(4)').click()
 time.sleep(2)
 driver.switch_to.frame('frameContent')
 unprocesseddata = dhcpnamestripper()
 input_data = [line.strip() for line in unprocesseddata.strip().split('\n')]
 macaddresses = []
 for i in range(16):
  try:
   num = num + 1
   mac_whitelisted = driver.find_element(By.XPATH, f'//*[@id="WMacfilterConfigList_{num}_2"]')
   text = mac_whitelisted.text
   macaddresses.append(text)
   output = f'{num}. ' + text


  except NoSuchElementException:
   pass
 Unproc2 = f"""{unprocesseddata}"""
 input_data = [line.strip() for line in Unproc2.strip().split('\n')]
 result2 = get_names_for_mac_addresses(input_data, macaddresses)
 abcd.append("Whitelisted Devices:")
 for mac, name in zip(macaddresses, result2):
    num2 = num2 + 1
    abcd.append(("\n"+ f"{num2}. MAC Address: {mac}, Name: {name}"))
 abcd2 = " ".join(abcd)  
 return abcd2


def remove1(indexnumber):
 num = -1
 driver = webdriver.Chrome(options=chrome_options)
 SignIn(driver)
 time.sleep(2)
 driver.find_element(By.XPATH, '//*[@id="headerTab"]/ul/li[6]/div[2]').click()
 time.sleep(2)
 driver.find_element(By.CSS_SELECTOR, '#nav > ul > li:nth-child(4)').click()
 time.sleep(2)
 driver.switch_to.frame('frameContent')
 goop1 = []
 try:
     if indexnumber == 'all':
        for i in range(16):
            num = num + 1
            try:
                element = driver.find_element(By.XPATH, f'//*[@id="WMacfilterConfigList_rml{num}"]')
                element.click()
                mac_whitelisted = driver.find_element(By.XPATH, f'//*[@id="WMacfilterConfigList_{num}_2"]')
                text = mac_whitelisted.text
                goop1.append(f"Removed: ~~{text}.~~")
            except NoSuchElementException:
                goop1.append(f"Element {num} not found")
                continue

        time.sleep(5)
        deletebutton = driver.find_element(By.XPATH, '//*[@id="DeleteButton"]')
        deletebutton.click()
        

        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert.accept()
        

        time.sleep(5)
     else:
        driver.find_element(By.XPATH, f'//*[@id="WMacfilterConfigList_rml{indexnumber}"]').click()
        mac_whitelisted2 = driver.find_element(By.XPATH, f'//*[@id="WMacfilterConfigList_{indexnumber}_2"]')
        text2 = mac_whitelisted2.text
        goop1.append(f"Removed ~~{text2}.~~")

        deletebutton = driver.find_element(By.XPATH, '//*[@id="DeleteButton"]')
        deletebutton.click()
        

        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert.accept()
        
        

 except (NoSuchElementException, TimeoutException):
   pass
 goop2 = "\n ".join(goop1)  
 return goop2
def add1(macaddress):
 num = -1
 driver = webdriver.Chrome(options=chrome_options)
 SignIn(driver)
 time.sleep(2)
 driver.find_element(By.XPATH, '//*[@id="headerTab"]/ul/li[6]/div[2]').click()
 time.sleep(2)
 driver.find_element(By.CSS_SELECTOR, '#nav > ul > li:nth-child(4)').click()
 time.sleep(2)
 driver.switch_to.frame('frameContent')
 driver.find_element(By.XPATH, '//*[@id="Newbutton"]').click()
 try:
  alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
  alert.accept()
 except TimeoutException:
  pass
 field = driver.find_element(By.XPATH, '//*[@id="SourceMACAddress"]')
 field.click()
 field.send_keys(macaddress)
 driver.find_element(By.XPATH,'//*[@id="btnApply_ex"]').click()
 haha = f"Added **{macaddress}** successfully."
 return haha
def wlan1(option):
  lowercase = option.lower()
  driver = webdriver.Chrome(options=chrome_options)
  SignIn(driver)
  time.sleep(2)
  driver.find_element(By.CSS_SELECTOR, '#headerTab > ul > li:nth-child(5) > div.tabBtnCenter').click()
  time.sleep(5)
  driver.switch_to.frame('frameContent')
  button = driver.find_element(By.XPATH, '//*[@id="wlEnbl"]')
  if lowercase == 'on':
    if button.is_selected():
      Sol = "Wireless Network is already enabled."
    else:
      button.click()
      Sol ="Wireless Network has been enabled. "
  elif lowercase == 'off':
    if button.is_selected():
      button.click()
      Sol = "Turned off Wireless Network."
    else:
      Sol ="Wireless Network is already disabled."   
  return Sol     
def rebat():
  cec = "``The router is restarted.``"
  driver = webdriver.Chrome(options=chrome_options)
  SignIn(driver)
  print('P1')
  time.sleep(1)
  driver.find_element(By.CSS_SELECTOR, '#headerTab > ul > li:nth-child(11) > div.tabBtnCenter').click()
  time.sleep(1)
  print('P2')
  driver.switch_to.frame('frameContent')
  driver.find_element(By.XPATH, '//*[@id="btnReboot"]').click()
  alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
  alert.accept()
  print('P3')
  time.sleep(80)
  return cec
