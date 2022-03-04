# 引入3個包

from selenium import webdriver
from time import sleep
import random
import os
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
load_dotenv()

chrome_options = Options() 
chrome_options.add_argument('--headless')  # 啟動Headless 無頭
chrome_options.add_argument('--disable-gpu') #關閉GPU 避免某些系統或是網頁出錯
# 程式啟動後先休眠1-4秒
sleep(random.randint(1,4))

# 呼叫Selenium WebDriver的庫 和 各個瀏覽器的驅動程序 進行互動，傳遞
# Selenium命令 給它們，並且獲取命令執行的結果，返回給我們的程式碼進行處理。
# 下載有個chrome瀏覽器的驅動到本地，把驅動地址替換成你自己儲存的地址
# 通過webdriver.Chrome啟動瀏覽器
driver = webdriver.Chrome(executable_path='C:\\Users\\Administrator\\Desktop\\成大\\app試作\\體溫機器人\\chromedriver.exe',chrome_options=chrome_options)
# 定義url地址，這個地址最好是未登入的情況下開啟的簽到頁面url，以便登入後直接跳轉到簽到頁面
url = "https://app.pers.ncku.edu.tw/ncov/index.php?auth"
driver.get(url)
# 獲取當前頁面的控制代碼
new_handle = driver.current_window_handle
# 切換到當前頁面視窗
driver.switch_to.window(new_handle)
# 清空登入頁面 使用者名稱和密碼框內的內容：
driver.find_element_by_id("user_id").clear()
driver.find_element_by_id("passwd").clear()
# 填入要登入的使用者名稱和密碼
driver.find_element_by_id("user_id").send_keys(os.getenv("username"))
driver.find_element_by_id("passwd").send_keys(os.getenv("passwd"))
# 填入後再休眠1-4秒鐘
print("登入惹")
sleep(random.randint(1,4))
# 通過CSS選擇器，找到登入按鈕，使用click()實現點選登入
driver.find_element_by_css_selector("#submit_by_acpw").click()
# a = driver.find_elements_by_xpath('//button[@class="pn vm"]')

# 獲取登入後的頁面
new_handle = driver.current_window_handle
# 切換到登入後的頁面
driver.switch_to.window(new_handle)

# 休眠4秒，以便頁面載入完畢，如果簽到按鈕沒有加載出來就點選，簽到會失敗
sleep(4)
# 以下是兩種獲取點選按鈕然後點選的方式，具體樣式標籤要視頁面而定
driver.find_element_by_id("fs_upd_N").click()
try:
    driver.find_element_by_id("vaccine2_N").click()
except:
    print("齁齁齁")
driver.find_element_by_name("save").click()
# driver.find_element_by_xpath("//div//a[contains(@id,'JD_sign')]").click()
# 休眠5秒
sleep(5)
# 關閉瀏覽器
driver.quit() # driver.close()