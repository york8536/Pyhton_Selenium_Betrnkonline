# -------------------------------------------------------------------載入相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException # 錯誤類型搭配except使用 
import sys
import time
from selenium.webdriver.support.ui import WebDriverWait #顯性等待​
from selenium.webdriver.support import expected_conditions as EC #等待條件

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
    
def control_slider_ad(driver): # 切換輪播廣告
    try:
        get_prevArrow = driver.find_element(By.CLASS_NAME, "indexCarousel_samplePrevArrow__IVQan")
        get_prevArrow.click()
        time.sleep(1.5)
        get_nextArrow = driver.find_element(By.CLASS_NAME, "indexCarousel_sampleNextArrow__7zNz_")
        get_nextArrow.click()
        time.sleep(1.5)
    except NoSuchElementException as e:
        print(f"Error controlling 'slider ad': {e}")

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
        # get_all = WebDriverWait(driver,timeout=3).until(EC.element_to_be_clickable((By.XPATH, ".//ul[@class='tab_owlTab__ib_3_']/li[1]"))) # 顯性等待
        get_all = driver.find_element(By.XPATH, ".//ul[@class='tab_owlTab__ib_3_']/li[1]")
        get_all.click()
        # time.sleep(1)
        open_all = driver.find_elements(By.XPATH, ".//div[@class='announcement_page_ListContainer__8lxIu']/div")
        for news in open_all:
            news.click()
            get_news_title = driver.find_element(By.XPATH, ".//div[@class='annModal_title__ztKHL']/h3")
            print('最新消息標題 : '+get_news_title.text)
            close_news = driver.find_element(By.XPATH, ".//button[@class='detailModal_closeBtn__mWsKW']")
            close_news.click()
        
        open_all[0].click()
        time.sleep(1.5)
        copy_URL = driver.find_element(By.XPATH, ".//button[@class='detailModal_copyBtn__AvhU9']")
        copy_URL.click()
        WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '複製成功')]")))
        get_next = driver.find_element(By.XPATH, ".//div[@class='detailModal_annFooter__BFFIW']/button[2]")
        get_next.click()
        time.sleep(1.5)
        get_previous = driver.find_element(By.XPATH, ".//div[@class='detailModal_annFooter__BFFIW']/button[1]")
        get_previous.click()
        close_news = driver.find_element(By.XPATH, ".//button[@class='detailModal_closeBtn__mWsKW']")
        close_news.click()
            
        get_activity = driver.find_element(By.XPATH, ".//ul[@class='tab_owlTab__ib_3_']/li[2]")
        get_activity.click()
        # time.sleep(1)
        get_maintain = driver.find_element(By.XPATH, ".//ul[@class='tab_owlTab__ib_3_']/li[3]")
        get_maintain.click()
        # time.sleep(1)
        get_other = driver.find_element(By.XPATH, ".//ul[@class='tab_owlTab__ib_3_']/li[4]")
        get_other.click()
        # time.sleep(1)
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
