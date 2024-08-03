# -------------------------------------------------------------------載入相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys



# ------------------------------------------------------------------- 建立ChromeDriver並套用基礎設定
def setup_driver():
    options = Options()
    # options.executable_path = "D:/chromedriver.exe"  # 設定ChromeDriver路徑
    # options.add_argument("--auto-open-devtools-for-tabs")  # 開啟F12
    driver = webdriver.Chrome(options=options) # 建立ChromeDriver實例
    driver.maximize_window() # 視窗最大化
    driver.implicitly_wait(8)  # 設置隱性等待
    driver.get("https://www.google.com.tw/?hl=zh_TW") # 取得網址
    sys.stdout.reconfigure(encoding='utf-8') # 套用UTF-8編碼
    return driver

# ------------------------------------------------------------------- 登入

def close_limitAge_btn(driver): # 關閉年紀限制視窗
    noremind_checkbox = driver.find_element(By.CLASS_NAME, "limitAge_checkbox__d6XiN")
    noremind_checkbox.click()
    get_limitAge_btn = driver.find_element(By.XPATH, "//*[text()='已滿18歲']")
    get_limitAge_btn.click()

def google_login(driver,account, password): # Google登入
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div/div[2]/a").click()
    driver.find_element(By.ID, "identifierId").send_keys(account) 
    driver.find_element(By.ID, "identifierNext").click()
    driver.find_element(By.NAME,"Passwd").send_keys(password)
    driver.find_element(By.ID, "passwordNext").click()

def open_new_tab(driver, URL): # 開分頁
    driver.execute_script(f"window.open('{URL}', '_blank');") 
    current_window_handle = driver.current_window_handle # 獲取當前視窗分頁的 ID
    for handle in driver.window_handles:     # 切到新分頁
        if handle != current_window_handle:
            driver.switch_to.window(handle)
            break

def open_play(driver): # 打開立即玩
    get_play = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[1]")
    get_play.click()

def open_news(driver): # 打開最新消息
    get_news = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[2]")
    get_news.click()

def open_newbie(driver): # 打開新手必看
    get_newbie = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[3]")
    get_newbie.click()

def open_ranking(driver): # 打開活動排行
    get_ranking = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[4]")
    get_ranking.click()

def open_purchase(driver): # 打開購點兌換
    get_purchase = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[5]")
    get_purchase.click()

def open_service(driver): # 打開客服中心
    get_service = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[6]")
    get_service.click()

def open_member(driver): # 打開會員中心
    get_member = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[7]")
    get_member.click()



