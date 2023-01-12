from driver.appium_driver import AppiumDriver
from loguru import logger
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder


class PayBillActivity(AppiumDriver):

    def click_on_DESCO_prepaid(self):
        # self.switch_native_to_flutter()
        # self.driver.switch_to.context('FLUTTER')
        self.driver.switch_to.context('WEBVIEW_stetho_com.bkash.businessapp.uat')
        text_finder = FlutterFinder().by_text("Palli Bidyut (Prepaid)")
        print(text_finder)
        text_element = FlutterElement(self.driver, text_finder)
        print(text_element)
        text_element.click()
