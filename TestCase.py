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
        options.add_experimental_option('useAutomationExtension', False) # 停用Automation Extension
        options.add_experimental_option("excludeSwitches", ['enable-automation']) # 排除 enable-automation 開關
        
        driver = webdriver.Chrome(options=options) # 建立ChromeDriver實例
        driver.maximize_window() # 視窗最大化
        driver.implicitly_wait(10)  # 設置隱性等待
        driver.get("https://www.google.com.tw/?hl=zh_TW") # 取得網址
        sys.stdout.reconfigure(encoding='utf-8') # 套用UTF-8編碼
        return driver
    except WebDriverException as e:
        print(f"ChromeDriver設定異常: {e}")
        return None

# ------------------------------------------------------------------- 登入
def google_login(driver, account, password): # Google登入
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[2]/a").click()
        driver.find_element(By.ID, "identifierId").send_keys(account) 
        driver.find_element(By.ID, "identifierNext").click()
        driver.find_element(By.NAME, "Passwd").send_keys(password)
        driver.find_element(By.ID, "passwordNext").click()
        print('Google登入-OK')
    except NoSuchElementException as e:
        print(f"Google登入-Error: {e}")

def betrnk_login(driver): # 官網登入
    try:
        driver.find_element(By.CLASS_NAME, "signInFloat_signInButton___h228").click()
        driver.find_element(By.CLASS_NAME, "signIModal_loginBtnGoogle__bFsCU").click()
        memberTitle = driver.find_element(By.CLASS_NAME, "signInFloat_memberTitle__dz7NN")
        return memberTitle
    except NoSuchElementException as e:
        print(f"官網登入-Error: {e}")

def open_new_tab(driver, URL): # 開瀏覽器新分頁
    try:
        driver.execute_script(f"window.open('{URL}', '_blank');") 
        current_window_handle = driver.current_window_handle # 獲取當前視窗分頁的 ID
        for handle in driver.window_handles:     # 切到新分頁
            if handle != current_window_handle:
                driver.switch_to.window(handle)
                break
        print('開瀏覽器新分頁-OK')
    except WebDriverException as e:
        print(f"開瀏覽器新分頁-Error: {e}")

def close_limitAge_btn(driver): # 關閉年齡限制視窗
    try:
        noremind_checkbox = driver.find_element(By.CLASS_NAME, "limitAge_checkbox__d6XiN")
        noremind_checkbox.click()
        get_limitAge_btn = driver.find_element(By.XPATH, "//*[text()='已滿18歲']")
        get_limitAge_btn.click()
        print('關閉年齡限制視窗-OK')
    except NoSuchElementException as e:
        print(f"關閉年齡限制視窗-Error: {e}")
    
def control_slider_ad(driver): # 大廳輪播廣告
    try:
        get_prevArrow = driver.find_element(By.CLASS_NAME, "indexCarousel_samplePrevArrow__IVQan")
        get_prevArrow.click()
        time.sleep(1)
        get_nextArrow = driver.find_element(By.CLASS_NAME, "indexCarousel_sampleNextArrow__7zNz_")
        get_nextArrow.click()
        time.sleep(1)
        print('切換輪播廣告-OK')
    except NoSuchElementException as e:
        print(f"切換輪播廣告-Error: {e}")

def open_play(driver): # 打開立即玩
    try:
        get_play = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[1]")
        get_play.click()
        print('打開立即玩-OK')
    except NoSuchElementException as e:
        print(f"打開立即玩-Error: {e}")

def open_news(driver): # 開啟最新消息
    try:
        get_news = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[2]")
        get_news.click()
        time.sleep(1)
        # WebDriverWait(driver,timeout=3).until(EC.element_to_be_clickable((By.XPATH, ".//ul[@class='tab_owlTab__ib_3_']/li[1]"))) # 顯性等待
        get_activity = driver.find_element(By.XPATH, ".//ul[@class='tab_owlTab__ib_3_']/li[2]")
        get_activity.click()
        time.sleep(1)
        get_maintain = driver.find_element(By.XPATH, ".//ul[@class='tab_owlTab__ib_3_']/li[3]")
        get_maintain.click()
        time.sleep(1)
        get_other = driver.find_element(By.XPATH, ".//ul[@class='tab_owlTab__ib_3_']/li[4]")
        get_other.click()
        time.sleep(1)
        get_all = driver.find_element(By.XPATH, ".//ul[@class='tab_owlTab__ib_3_']/li[1]")
        get_all.click()
        time.sleep(1)
        print('開啟最新消息-OK')
    except NoSuchElementException as e:
        print(f"開啟最新消息-Error: {e}")

def read_news(driver): # 查看最新消息
    try:
        open_all = driver.find_elements(By.XPATH, ".//div[@class='announcement_page_ListContainer__8lxIu']/div")
        for news in open_all:
            news.click()
            time.sleep(0.5)
            get_news_title = driver.find_element(By.XPATH, ".//div[@class='annModal_title__ztKHL']/h3")
            print('最新消息標題 : '+get_news_title.text)     
            close_news = driver.find_element(By.XPATH, ".//button[@class='detailModal_closeBtn__mWsKW']")     
            close_news.click()
            print('查看最新消息-OK')
    except NoSuchElementException as e:
        print(f"查看最新消息-Error: {e}")

def check_newsInside(driver): # 檢查最新消息內部按鈕
    try:
        open_all = driver.find_elements(By.XPATH, ".//div[@class='announcement_page_ListContainer__8lxIu']/div")
        open_all[0].click()
        time.sleep(1)
        copy_URL = driver.find_element(By.XPATH, ".//button[@class='detailModal_copyBtn__AvhU9']")
        copy_URL.click()
        WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '複製成功')]")))
        get_next = driver.find_element(By.XPATH, ".//div[@class='detailModal_annFooter__BFFIW']/button[2]")
        get_next.click()
        time.sleep(1)
        get_previous = driver.find_element(By.XPATH, ".//div[@class='detailModal_annFooter__BFFIW']/button[1]")
        get_previous.click()
        time.sleep(1)
        close_news = driver.find_element(By.XPATH, ".//button[@class='detailModal_closeBtn__mWsKW']")
        close_news.click()
        print('檢查最新消息內部按鈕-OK')
    except NoSuchElementException as e:
        print(f"檢查最新消息內部按鈕-Error: {e}")

def test_news(driver):  # 測試最新消息
    open_news(driver)
    read_news(driver)
    check_newsInside(driver)

def open_newbie(driver, subTab): # 打開新手必看子頁籤
    try:
        time.sleep(1)
        get_newbie = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[3]")
        get_newbie.click()
        time.sleep(1)
        match subTab:
            case 'gameGuide':
                get_gameGuide = driver.find_element(By.XPATH, ".//ul[@class='navBar_subMenu__cw8xl']/li[1]")
                get_gameGuide.click()
            case 'featuredGames':
                get_featuredGames = driver.find_element(By.XPATH, ".//ul[@class='navBar_subMenu__cw8xl']/li[2]")
                get_featuredGames.click()
            case 'vipDescription':
                get_vipDescription = driver.find_element(By.XPATH, ".//ul[@class='navBar_subMenu__cw8xl']/li[3]")
                get_vipDescription.click()
            case 'giftDescription':
                get_giftDescription = driver.find_element(By.XPATH, ".//ul[@class='navBar_subMenu__cw8xl']/li[4]")
                get_giftDescription.click()
    except NoSuchElementException as e:
        print(f"開啟新手必看-Error: {e}")

def open_gameGuide(driver): # 打開遊戲攻略
    try:
        open_newbie(driver, 'gameGuide')
        time.sleep(1)
        index = [0, -1]
        gameGuidesTitle_list = []
        for i in index:
            try:
                read_gameGuides = driver.find_elements(By.XPATH, ".//div[@class='gameGuidle_guidleList__XEg6B']/a")
                read_gameGuides[i].click()
                time.sleep(1)
                get_gameGuides_title = driver.find_element(By.XPATH, ".//h2[@class='gameGuidle_h2Title__i1X6j aos-init aos-animate']/strong")
                gameGuidesTitle_list.append(get_gameGuides_title.text)
                goBack = driver.find_element(By.XPATH, "//*[contains(text(), '遊戲攻略')]")
                goBack.click()
                time.sleep(1)
            except Exception as e:
                print(f"閱讀遊戲攻略-{i}-Error: {e}")
                break
        print('開啟遊戲攻略-OK  ', gameGuidesTitle_list)
        return gameGuidesTitle_list
    except Exception as e:
        print(f"開啟遊戲攻略-Error: {e}")
        return None

def open_featuredGames(driver): # 開啟特色遊戲
    try:
        open_newbie(driver, 'featuredGames')
        time.sleep(1)
        print("開啟特色遊戲-OK")
    except Exception as e:
        print(f"開啟特色遊戲-Error: {e}")

def open_vipDescription(driver): # 開啟VIP說明
    try:
        open_newbie(driver, 'vipDescription')
        time.sleep(1)
        print("開啟VIP說明-OK")
    except Exception as e:
        print(f"開啟VIP說明-Error: {e}")

def open_giftDescription(driver): # 開啟贈禮說明
    try:
        open_newbie(driver, 'giftDescription')
        time.sleep(1)
        print("開啟贈禮說明-OK")
    except Exception as e:
        print(f"開啟贈禮說明-Error: {e}")

def test_newbie(driver): # 測試新手必看
    open_gameGuide(driver)
    open_featuredGames(driver)
    open_vipDescription(driver)
    open_giftDescription(driver)

def open_ranking(driver, subTab): # 開啟活動排行子頁籤
    try:
        time.sleep(1)
        get_ranking = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[4]")
        get_ranking.click()
        time.sleep(1)
        match subTab:
            case 'activityList':
                get_activityList = driver.find_element(By.XPATH, ".//ul[@class='navBar_subMenu__cw8xl']/li[1]")
                get_activityList.click()
            case 'richList':
                get_richList = driver.find_element(By.XPATH, ".//ul[@class='navBar_subMenu__cw8xl']/li[2]")
                get_richList.click()
    except NoSuchElementException as e:
        print(f"開啟活動排行-Error: {e}")

def open_activityList(driver):  # 開啟活動榜
    try:
        open_ranking(driver, 'activityList')
        getActivityList = driver.find_element(By.XPATH, ".//table[@class='table_owlTable__GQgFr']")
        print('開啟活動榜-OK')

        return getActivityList
    except NoSuchElementException as e:
        print(f"開啟活動榜-Error: {e}")

def open_richList(driver):  # 開啟富豪榜
    try:
        open_ranking(driver, 'richList')
        getRichList = driver.find_element(By.XPATH, ".//table[@class='table_owlTable__GQgFr']")
        print('開啟富豪榜-OK')

        return getRichList
    except NoSuchElementException as e:
        print(f"開啟富豪榜-Error: {e}")

def test_ranking(driver): # 測試活動排行
    open_activityList(driver)
    open_richList(driver)

def open_purchase(driver, subTab): # 開啟購點兌換子頁籤
    try:
        time.sleep(1)
        get_purchase = driver.find_element(By.XPATH, ".//nav[@class='navBar_navTopList__Xaa_z']/ul/li[5]")
        get_purchase.click()
        time.sleep(1)
        match subTab:
            case 'buyPoints':
                get_buyPoints = driver.find_element(By.XPATH, ".//ul[@class='navBar_subMenu__cw8xl']/li[1]")
                get_buyPoints.click()
            case 'redeemPoints':
                get_redeemPoints = driver.find_element(By.XPATH, ".//ul[@class='navBar_subMenu__cw8xl']/li[2]")
                get_redeemPoints.click()
            case 'serialNumbers':
                get_serialNumbers = driver.find_element(By.XPATH, ".//ul[@class='navBar_subMenu__cw8xl']/li[3]")
                get_serialNumbers.click()            
    except NoSuchElementException as e:
        print(f"開啟購點兌換-Error: {e}")

def open_buyPoints(driver):  # 開啟購點頁面
    try:
        open_purchase(driver, 'buyPoints')
        getPurchaseTab = driver.find_element(By.CLASS_NAME, "tab_owlTab__ib_3_")
        print('開啟購點頁面-OK')

        return getPurchaseTab
    except NoSuchElementException as e:
        print(f"開啟購點頁面-Error: {e}")

def open_redeemPoints(driver):  # 開啟點數兌換
    try:
        open_purchase(driver, 'redeemPoints')
        getPurchaseTab = driver.find_element(By.CLASS_NAME, "tab_owlTab__ib_3_")
        print('開啟點數兌換-OK')

        return getPurchaseTab
    except NoSuchElementException as e:
        print(f"開啟點數兌換-Error: {e}")

def open_serialNumbers(driver):  # 開啟兌換碼兌換
    try:
        open_purchase(driver, 'serialNumbers')
        getRedeemButton = driver.find_element(By.CLASS_NAME, "coupon_exchangeBtnDisable__D_C_x")
        print('開啟兌換碼兌換-OK')

        return getRedeemButton
    except NoSuchElementException as e:
        print(f"開啟兌換碼兌換-Error: {e}")

def test_purchase(driver): # 測試購點兌換
    open_buyPoints(driver)
    open_redeemPoints(driver)
    open_serialNumbers(driver)

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
