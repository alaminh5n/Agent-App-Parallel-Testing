import time
from driver.appium_driver import AppiumDriver
from loguru import logger


class InsertAmountActivity(AppiumDriver):

    def enter_amount(self, amount):
        logger.info("User is in Insert Amount view")
        locator = 'com.bkash.businessapp.uat:id/etAmount'
        time.sleep(3)
        self.send_key_helper(locator, amount)

    def click_on_cash_in_amount_1(self):
        logger.info("User is in Insert Amount view")
        locator = 'com.bkash.businessapp.uat:id/tvCashinAmount1'
        time.sleep(3)
        self.click_helper(locator, 'ID')

    def click_on_cash_in_amount_2(self):
        logger.info("User is in Insert Amount view")
        locator = 'com.bkash.businessapp.uat:id/tvCashinAmount2'
        time.sleep(3)
        self.click_helper(locator, 'ID')

    def click_on_cash_in_amount_3(self):
        logger.info("User is in Insert Amount view")
        locator = 'com.bkash.businessapp.uat:id/tvCashinAmount3'
        time.sleep(3)
        self.click_helper(locator, 'ID')

    def click_on_cash_in_amount_4(self):
        logger.info("User is in Insert Amount view")
        locator = 'com.bkash.businessapp.uat:id/tvCashinAmount4'
        time.sleep(3)
        self.click_helper(locator, 'ID')

    def click_on_proceed_to_next_step(self):
        logger.info("User is in Insert Amount view")
        locator = 'com.bkash.businessapp.uat:id/btn_Next'
        self.click_helper(locator, 'ID')

