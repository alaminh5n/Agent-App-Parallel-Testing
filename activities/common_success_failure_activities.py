from driver.appium_driver import AppiumDriver
from loguru import logger


class ConfirmationActivity(AppiumDriver):

    def press_on_back_to_home(self):
        logger.info("User is in Transaction Confirmation view")
        locator = 'com.bkash.businessapp.uat:id/btnNext'
        self.click_helper(locator, 'ID')


class ConfirmationValidation(AppiumDriver):

    def get_confirmation_title(self):
        logger.info("User is in Transaction Confirmation view")
        locator = 'com.bkash.businessapp.uat:id/tvConfirmationTitle'
        return self.get_text_helper(locator)

    #Your Cash In transfer is complete.
    #Your B2B Transfer is complete.
    #Your E-Money Request is Successful
    #Your Cash Request is Successful

