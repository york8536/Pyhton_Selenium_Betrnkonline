# -------------------------------------------------------------------載入相關模組
import TestCase
import Config
import time


driver = TestCase.setup_driver() # 瀏覽器驅動設置

TestCase.google_login(driver, Config.account, Config.password) # GOOGLE登入
TestCase.open_new_tab(driver, Config.URL) # 開新瀏覽器分頁
TestCase.close_limitAge_btn(driver) # 18歲限制視窗
TestCase.betrnk_login(driver) # 官網登入--->必須先完成google_login()

TestCase.control_slider_ad(driver) # 輪播廣告測試
TestCase.test_news(driver) # 最新消息測試
TestCase.test_newbie(driver) # 新手必看測試
TestCase.test_ranking(driver) # 排行榜測試
TestCase.test_purchase(driver) # 購點兌換測試
TestCase.test_service(driver) # 客服中心測試
TestCase.test_member(driver) # 會員中心測試
time.sleep(3)

driver.quit()

