# -------------------------------------------------------------------載入相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import sys

# ------------------------------------------------------------------- 建立ChromeDriver並套用基礎設定
def setup_driver():
    try:
        options = Options()
        # options.executable_path = "D:/chromedriver.exe"  # 設定ChromeDriver路徑
        # options.add_argument("--auto-open-devtools-for-tabs")  # 開啟F12
        driver = webdriver.Chrome(options=options) # 建立ChromeDriver實例
        driver.maximize_window() # 視窗最大化
        driver.implicitly_wait(8)  # 設置隱性等待
        driver.get("https://www.google.com.tw/?hl=zh_TW") # 取得網址
        sys.stdout.reconfigure(encoding='utf-8') # 套用UTF-8編碼
        return driver
    except WebDriverException as e:
        print(f"Error setting up driver: {e}")
        return None

# ------------------------------------------------------------------- 登入
def google_login(driver, account, password): # Google登入
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[2]/a").click()
        driver.find_element(By.ID, "identifierId").send_keys(account) 
        driver.find_element(By.ID, "identifierNext").click()
        driver.find_element(By.NAME, "Passwd").send_keys(password)
        driver.find_element(By.ID, "passwordNext").click()
    except NoSuchElementException as e:
        print(f"Error logging in to Google: {e}")

def open_new_tab(driver, URL): # 開分頁
    try:
        driver.execute_script(f"window.open('{URL}', '_blank');") 
        current_window_handle = driver.current_window_handle # 獲取當前視窗分頁的 ID
        for handle in driver.window_handles:     # 切到新分頁
            if handle != current_window_handle:
                driver.switch_to.window(handle)
                break
    except WebDriverException as e:
        print(f"Error opening new tab: {e}")

def close_limitAge_btn(driver): # 關閉年紀限制視窗
    try:
        noremind_checkbox = driver.find_element(By.CLASS_NAME, "limitAge_checkbox__d6XiN")
        noremind_checkbox.click()
        get_limitAge_btn = driver.find_element(By.XPATH, "//*[text()='已滿18歲']")
        get_limitAge_btn.click()
    except NoSuchElementException as e:
        print(f"Error closing limit age button: {e}")

def open_play(driver): # 打開立即玩
    try:
        get_play = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[1]")
        get_play.click()
    except NoSuchElementException as e:
        print(f"Error opening 'Play Now': {e}")

def open_news(driver): # 打開最新消息
    try:
        get_news = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[2]")
        get_news.click()
        get_all = driver.find_element(By.XPATH, ".//ul[@class='tab_owlTab__ib_3_']/li[1]")
        get_all.click()
        get_activity = driver.find_element(By.XPATH, ".//ul[@class='tab_owlTab__ib_3_']/li[2]")
        get_activity.click()
        get_maintain = driver.find_element(By.XPATH, ".//ul[@class='tab_owlTab__ib_3_']/li[3]")
        get_maintain.click()
        get_other = driver.find_element(By.XPATH, ".//ul[@class='tab_owlTab__ib_3_']/li[4]")
        get_other.click()
    except NoSuchElementException as e:
        print(f"Error opening 'News': {e}")

def open_newbie(driver): # 打開新手必看
    try:
        get_newbie = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[3]")
        get_newbie.click()
    except NoSuchElementException as e:
        print(f"Error opening 'Newbie Guide': {e}")

def open_ranking(driver): # 打開活動排行
    try:
        get_ranking = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[4]")
        get_ranking.click()
    except NoSuchElementException as e:
        print(f"Error opening 'Ranking': {e}")

def open_purchase(driver): # 打開購點兌換
    try:
        get_purchase = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[5]")
        get_purchase.click()
    except NoSuchElementException as e:
        print(f"Error opening 'Purchase': {e}")

def open_service(driver): # 打開客服中心
    try:
        get_service = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[6]")
        get_service.click()
    except NoSuchElementException as e:
        print(f"Error opening 'Service': {e}")

def open_member(driver): # 打開會員中心
    try:
        get_member = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[7]")
        get_member.click()
    except NoSuchElementException as e:
        print(f"Error opening 'Member Center': {e}")
