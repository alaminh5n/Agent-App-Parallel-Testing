from driver.appium_driver import AppiumDriver
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.touch_action import TouchAction
from custom_exception.appium_exceptions import CouldNotExecute
from loguru import logger


class TapAndHoldActivity(AppiumDriver):

    def press_and_hold(self):
        logger.info("User is in Tap and Hold view ")
        try:
            locator = 'com.bkash.businessapp.uat:id/tvTapAndHoldText'
            self.wait_for_element(locator)
            actions = TouchAction(self.driver)
            actions.long_press(self.driver.find_element(By.ID, locator))
            actions.perform()
            logger.info('Tap and Hold is pressed and hold for payment confirmation')
        except Exception as e:
            logger.info('Could not press Tap and Hold')
            raise CouldNotExecute('Could not press Tap and Hold')

    def press_on_cross(self):
        logger.info("User is in Tap and Hold view ")
        locator = 'com.bkash.businessapp.uat:id/ibTitleIcon'
        self.click_helper(locator, 'ID')
