from driver.appium_driver import AppiumDriver
from loguru import logger


class CashInActivity(AppiumDriver):

    def enter_customer_numer(self, number='01810189667'):
        logger.info("User is in Cash-In view")
        locator = 'com.bkash.businessapp.uat:id/et_enter_search_content'
        self.send_key_helper(locator, number)

    def click_on_proceed_to_the_next_step(self):
        logger.info("User is in Cash-In view")
        locator = 'com.bkash.businessapp.uat:id/btn_next'
        self.click_helper(locator, 'ID')
