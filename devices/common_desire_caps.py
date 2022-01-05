from conf.conf import APP_ACTIVITY, APK_PACKAGE_NAME, APK_PATH

android_common_desired_caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "newCommandTimeout": 60,
    "deviceReadyTimeout": 60,
    "adbExecTimeout": 20000,
    # "app": APK_PATH,
    "appPackage": APK_PACKAGE_NAME,
    "appActivity": APP_ACTIVITY,
    "autoGrantPermissions": True,
    "noReset": True,

}

for_pixel = {
    "platformVersion": "11",
    "deviceName": "Pixel Experience"
}

for_samsung = {
    "platformVersion": "10",
    "deviceName": "Samsung M21"
}
