from driver.appium_driver import AppiumDriver
from loguru import logger


class LoginPinInputActivity(AppiumDriver):

    def click_on_input_pin(self):
        logger.info("User is in Login view ")
        locator = 'com.bkash.businessapp.uat:id/et_enter_pin'
        self.click_helper(locator, 'ID')

    def press_key(self, key):
        logger.info("User is in Login view ")
        locator = 'com.bkash.businessapp.uat:id/pinpad_button_' + str(key)
        self.click_helper(locator, 'ID')

    def press_login(self):
        logger.info("User is in Login view ")
        locator = 'com.bkash.businessapp.uat:id/btn_next'
        self.click_helper(locator, 'ID')


class LoginPinInputValidation(AppiumDriver):

    def get_title(self):
        logger.info("User is in Login view ")
        locator = 'com.bkash.businessapp.uat:id/tvTitleBold'
        return self.get_text_helper(locator)

    def get_the_text_of_pin_input_field(self):
        logger.info("User is in Login view ")
        locator = 'com.bkash.businessapp.uat:id/et_enter_pin'
        return self.get_text_helper(locator)
