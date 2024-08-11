# -------------------------------------------------------------------載入相關模組
import TestCase
import Config
import time


driver = TestCase.setup_driver()
TestCase.google_login(driver, Config.account, Config.password)
TestCase.open_new_tab(driver, Config.URL)
TestCase.close_limitAge_btn(driver)
TestCase.betrnk_login(driver) # 必須先完成google_login()
TestCase.control_slider_ad(driver)
TestCase.test_news(driver)
TestCase.test_newbie(driver)
TestCase.test_ranking(driver)
TestCase.test_purchase(driver)
time.sleep(3)

driver.quit()