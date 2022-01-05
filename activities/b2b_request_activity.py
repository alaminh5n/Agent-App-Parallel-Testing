from driver.appium_driver import AppiumDriver
from loguru import logger


class B2BRequestActivity(AppiumDriver):

    def click_on_e_money_request(self):
        logger.info("User is in B2B Request view")
        locator = 'com.bkash.businessapp.uat:id/frame_layout_button_b2b_request_type_e_money'
        self.click_helper(locator, 'ID')

    def click_on_cash_request(self):
        logger.info("User is in B2B Request view")
        locator = 'com.bkash.businessapp.uat:id/frame_layout_button_b2b_request_type_cash'
        self.click_helper(locator, 'ID')
