from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import undetected_edgedriver as ed
# import undetected_chromedriver as uc
path = 'C:\Program Files (x86)\Common Files\chromedriver.exe'
# options = uc.Chrome(path)
driver = webdriver.Chrome(path)
url='https://www.marinetraffic.com/en/data/?asset_type=vessels&columns=flag,shipname,photo,recognized_next_port,reported_eta,reported_destination,current_port,imo,ship_type,show_on_live_map,time_of_latest_position,lat_of_latest_position,lon_of_latest_position,notes'
driver.get('https://www.marinetraffic.com')
driver.maximize_window()
time.sleep(10)
element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-1yp8yiu")))
element.click()
time.sleep(2)
element = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div[2]/div/section[1]/div/div/div[3]/div/div[1]/div/div[3]/button/div/div/div[2]/span/div/div/div/div[2]')))
element.click()
time.sleep(2)
search=WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="genericid-3"]/div/div[1]/div/div/input')))
search.send_keys("Length")
search.send_keys(Keys.RETURN)
time.sleep(2)
search_s=WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="genericid-3"]/div/div[2]/div/ul[1]/li[2]/div')))
search_s.click()
time.sleep(2)
lenght = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="slider-input-1"]')))

time.sleep(2)
lenght.send_keys(Keys.BACKSPACE)
lenght.send_keys(Keys.BACKSPACE)
lenght.send_keys(Keys.BACKSPACE)
lenght.send_keys("150")
lenght.send_keys(Keys.RETURN)

time.sleep(2)
search_b=WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="genericid-3"]/div[2]/div[2]/button')))
search_b.click()
time.sleep(10)
element = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div[2]/div/section[1]/div/div/div[3]/div/div[1]/div/div[3]/button/div/div/div[2]/span/div/div/div/div[2]')))
element.click()
time.sleep(2)
search2=WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="genericid-3"]/div/div[1]/div/div/input')))
search2.send_keys("Vessel Type - Generic")
search2.send_keys(Keys.RETURN)
time.sleep(2)
search_s=WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="genericid-3"]/div/div[2]/div/ul[1]/li[2]/div')))
search_s.click()
search_tank=WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="genericid-3"]/div[1]/div[2]/div/div[2]/ul/li[2]/div')))
search_tank.click()
time.sleep(2)
search_t=WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="genericid-3"]/div[2]/div[2]/button')))
search_t.click()
time.sleep(10)
datas=driver.find_elements(By.XPATH,'//*[@id="borderLayout_eGridPanel"]/div[1]/div/div/div[3]/div[3]/div/div/div/div[1]/div')
temas=driver.find_elements(By.XPATH,'//*[@id="borderLayout_eGridPanel"]/div[1]/div/div/div[3]/div[1]/div/div/div[3]/div')
a=[]
b=[]

for data in datas:
    a.append(data.find_element(By.CLASS_NAME,"ag-cell-content").text)
for tema in temas:
    b.append(tema.find_element(By.CLASS_NAME,'ag-cell-content').text)

print(a,b)
#
