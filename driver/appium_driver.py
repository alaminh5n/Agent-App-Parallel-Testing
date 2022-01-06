import os
from appium import webdriver
from time import sleep
from loguru import logger
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from devices.common_desire_caps import android_common_desired_caps, for_pixel, for_samsung
from custom_exception.env_variable_exception import EnvVariableNotSetException
from custom_exception.appium_exceptions import AppiumConnectionFailException, InvalidDeviceTypeException,\
    CouldNotFindTheElement, CouldNotFindTheXpath, CouldNotExecute
from utils.functions import get_android_desired_caps_from_os_env
logger.add("logs/file_{time}.log", format="{time} {level} {message}", level="INFO")


class AppiumDriver:
    driver = None
    ANDROID = 'android'
    desired_caps = None

    if "DEVICE_TYPE" not in os.environ:
        logger.critical(f"Env Variable 'device_type' is not set")
        raise EnvVariableNotSetException(f"Env Variable 'device_type' is not set")

    if "HUB_URL" not in os.environ:
        logger.critical(f"Env variable 'hub_url' is not set")
        raise EnvVariableNotSetException(f"Env variable 'hub_url' is not set")

    device_type = os.getenv('DEVICE_TYPE')
    logger.info(f'Testing for device type {device_type}')
    hub_url = os.getenv('HUB_URL')
    logger.info(f'Appium server url is {hub_url}')

    if driver is None:
        if device_type.lower() == ANDROID:
            android_desired_cap = get_android_desired_caps_from_os_env()
            desired_caps = {
                **android_common_desired_caps,
                **android_desired_cap
            }
        else:
            logger.critical(f'Invalid device type provided')
            raise InvalidDeviceTypeException("Invalid device type provided")

    try:
        driver = webdriver.Remote(command_executor=hub_url, desired_capabilities=desired_caps)
        logger.info(f'Connected to the appium server')
    except Exception as e:
        logger.critical(f'Could not connect to appium server.')
        raise AppiumConnectionFailException("Could not connect to appium server.")

    # desired_caps = dict(
    #     **android_common_desired_caps,
    #     # **for_pixel
    #     **for_samsung
    # )
    # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_caps)

    def wait_for_element(self, locator):
        logger.info(f'Waiting for the element: {locator}')
        wait = WebDriverWait(self.driver, 10)
        try:
            return wait.until(EC.presence_of_element_located((By.ID, locator)))
        except Exception as e:
            logger.error(f'Could not find the element: {locator}')
            raise CouldNotFindTheElement(f'Could not find the element: {locator}')

    def wait_for_xpath(self, locator):
        logger.info(f'Waiting for the Xpath')
        wait = WebDriverWait(self.driver, 10)
        try:
            return wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        except Exception as e:
            logger.error(f'Could not find the Xpath: {locator}')
            raise CouldNotFindTheXpath(f'Could not find the Xpath: {locator}')

    def get_the_activity_name(self):
        sleep(5)
        return str(self.driver.current_activity)

    def close_app_(self):
        self.driver.close_app()
        logger.info(f'App is closed')

    def launch_the_app(self):
        self.driver.launch_app()
        logger.info(f'App is launched')

    def click_helper(self, locator, element):
        if element == 'ID':
            self.wait_for_element(locator)
            try:
                self.driver.find_element(By.ID, locator).click()
                logger.info(f'ID: {locator} is clicked')
            except Exception as e:
                logger.error(f'Could not click the ID: {locator}')
                raise CouldNotExecute(f'Could not click the ID')
        elif element == 'XPATH':
            self.wait_for_xpath(locator)
            try:
                self.driver.find_element(By.XPATH, locator).click()
                logger.info(f'XPATH: {locator} is clicked')
            except Exception as e:
                logger.error(f'Could not click the XPATH: {locator}')
                raise CouldNotExecute(f'Could not click the XPATH')

    def send_key_helper(self, locator, data):
        self.wait_for_element(locator)
        try:
            self.driver.find_element(By.ID, locator).send_keys(data)
            logger.info(f'{data} has been inserted to {locator}')
        except Exception as e:
            logger.error(f'Could not insert {data} into {locator}')
            raise CouldNotExecute(f'Could not insert {data} into {locator}')

    def get_text_helper(self, locator):
        self.wait_for_element(locator)
        try:
            text = self.driver.find_element(By.ID, locator).text
            logger.info(f'{locator} is giving {text}')
            return text
        except Exception as e:
            logger.error(f'Could not get the text from {locator}')
            raise CouldNotExecute(f'Could not get the text from {locator}')
