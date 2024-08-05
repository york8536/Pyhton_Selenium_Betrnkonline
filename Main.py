# -------------------------------------------------------------------載入相關模組
import TestCase
import Config
import time


driver = TestCase.setup_driver()
# TestCase.google_login(driver, Config.account, Config.password)
TestCase.open_new_tab(driver, Config.URL)
TestCase.close_limitAge_btn(driver)
TestCase.open_news(driver)
time.sleep(2)
# TestCase.open_newbie(driver)
# time.sleep(2)
# TestCase.open_ranking(driver)
# time.sleep(2)
# TestCase.open_purchase(driver)
# time.sleep(2)
# TestCase.open_service(driver)
# time.sleep(2)
# TestCase.open_member(driver)
# time.sleep(10)