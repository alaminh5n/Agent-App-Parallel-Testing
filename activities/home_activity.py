from driver.appium_driver import AppiumDriver
from loguru import logger
from appium.webdriver.common.mobileby import By


class HomeActivity(AppiumDriver):

    def click_outside(self):
        logger.info("User is in App Home view")
        locator = 'com.bkash.businessapp.uat:id/touch_outside'
        self.click_helper(locator, 'ID')

    def turn_on_agent_status(self):
        logger.info("User is in App Home view")
        locator = 'com.bkash.businessapp.uat:id/button_action'
        try:
            self.click_helper(locator, 'ID')
        except:
            logger.info(f"{locator} not found because agent status is on")

    def click_on_cash_in(self):
        logger.info("User is in App Home view")
        locator = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout'
        self.click_helper(locator, 'XPATH')

    def click_on_b2b_transfer(self):
        logger.info("User is in App Home view")
        locator = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout'
        self.click_helper(locator, 'XPATH')

    def click_on_b2b_request(self):
        logger.info("User is in App Home view")
        locator = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout'
        self.click_helper(locator, 'XPATH')

    def click_on_pay_bill(self):
        logger.info("User is in App Home view")
        locator = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.LinearLayout'
        self.click_helper(locator, 'XPATH')

    def click_yes_on_confrim_b2b(self):
        logger.info("User is in App Home view")
        locator = 'com.bkash.businessapp.uat:id/button_b2b_transfer_acknowledgement_yes'
        self.click_helper(locator, 'ID')

    def click_no_on_confirm_b2b(self):
        logger.info("User is in App Home view")
        locator = 'com.bkash.businessapp.uat:id/button_b2b_transfer_acknowledgement_no'
        self.click_helper(locator, 'ID')

    def click_on_very_good(self):
        logger.info("User is in App Home view")
        locator = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[5]/android.widget.ImageView'
        self.click_helper(locator, 'XPATH')

    def click_okay_on_tooltip(self):
        logger.info("User is in App Home View")
        locator = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView'
        try:
            self.click_helper(locator, 'XPATH')
        except:
            logger.info("tooltip does not exist")


class HomeActivityValidation(AppiumDriver):

    def get_recent_transaction_title(self):
        logger.info("User is in App Home view")
        locator = 'com.bkash.businessapp.uat:id/tv_latest_transaction_title'
        return self.get_text_helper(locator)
