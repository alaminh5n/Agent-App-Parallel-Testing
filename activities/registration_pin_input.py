from driver.appium_driver import AppiumDriver
from loguru import logger


class RegistrationPinInput(AppiumDriver):

    def click_on_allow_to_read_and_insert_the_pin(self):
        logger.info("User is in Registration view ")
        locator = 'com.google.android.gms:id/positive_button'
        self.click_helper(locator, 'ID')

    def click_on_deny(self):
        logger.info("User is in Registration view ")
        locator = 'com.google.android.gms:id/negative_button'
        self.click_helper(locator, 'ID')
