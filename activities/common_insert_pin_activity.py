from driver.appium_driver import AppiumDriver
from loguru import logger


class InsertPinActivity(AppiumDriver):

    def click_on_input_pin(self):
        logger.info("User is in Insert Pin view")
        locator = 'com.bkash.businessapp.uat:id/tvEnterPin'
        self.click_helper(locator, 'ID')

    def press_key(self, key):
        logger.info("User is in Insert Pin view")
        locator = 'com.bkash.businessapp.uat:id/pinpad_button_' + str(key)
        self.click_helper(locator, 'ID')

    def press_confirm(self):
        logger.info("User is in Insert Pin view")
        locator = 'com.bkash.businessapp.uat:id/btnNext'
        self.click_helper(locator, 'ID')
