from driver.appium_driver import AppiumDriver
from loguru import logger


class BannerActivity(AppiumDriver):

    def click_on_close_button(self):
        logger.info("User is watching the error Banner")
        locator = 'com.bkash.businessapp.uat:id/closeBtn'
        self.click_helper(locator, 'ID')


class BannerValidation(AppiumDriver):

    def get_banner_text(self):
        logger.info("Reading the text from Banner")
        locator = 'com.bkash.businessapp.uat:id/errorDescription'
        return self.get_text_helper(locator)
