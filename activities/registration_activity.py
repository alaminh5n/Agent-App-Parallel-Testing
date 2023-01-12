import os
from driver.appium_driver import AppiumDriver
from loguru import logger


class RegistrationActivity(AppiumDriver):

    def change_language_to_english(self):
        logger.info("User is in Registration view ")
        locator = 'com.bkash.businessapp.uat:id/btnChangeLanguage'
        if self.get_text_helper(locator) == 'English':
            self.click_helper(locator, 'ID')

    def enter_mobile_number(self, number='01321188766'):
        logger.info("User is in Registration view ")
        logger.info(AppiumDriver.desired_caps)
        locator = 'com.bkash.businessapp.uat:id/etEntryAccountNumber'
        self.send_key_helper(locator, os.environ[AppiumDriver.desired_caps.get('deviceName')])

    def click_on_next(self):
        logger.info("User is in Registration view ")
        locator = 'com.bkash.businessapp.uat:id/btn_next'
        self.click_helper(locator, 'ID')

    def operator_selection(self):
        logger.info("User is in Registration view ")
        locator ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.ImageView'
        self.click_helper(locator, 'XPATH')
