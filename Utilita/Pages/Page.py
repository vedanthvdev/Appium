from appium import webdriver


class PageConv:
    
    def __init__(self,_driver):
        self.driver = _driver


    def AppOpen(self):
        desired_cap = {

            "deviceName": "emulator-5554",
            "platformName": "android",
            "appPackage": "com.ba.universalconverter",
            "appActivity": ".MainConverterActivity",
            "noReset": True
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    def AppOpenVerify(self):
        assert self.driver.find_element_by_accessibility_id("Open navigation drawer").is_displayed()


    def NavDrawer(self):
        self.driver.find_element_by_accessibility_id("Open navigation drawer").click()


    def NavDrawerVerify(self):
        assert self.driver.find_element_by_id(
            "com.ba.universalconverter:id/legend_line2").is_displayed()


    def length(self):
        self.driver.find_element_by_id(
            "com.ba.universalconverter:id/legend_line2").click()


    def lengthVerify(self):
        assert self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.Spinner[1]/android.widget.RelativeLayout/android.widget.TextView").is_displayed()


    def clear(self):
        el2C = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.Button[3]")
        el2C.click()


    def clearVerify(self):
        assert self.driver.find_element_by_id(
            "com.ba.universalconverter:id/target_value_placeholder").is_displayed()


    def firstUnit(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.Spinner[1]/android.widget.RelativeLayout/android.widget.TextView").click()


    def unitKM(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.TextView[1]").click()


    def secondUnit(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.Spinner[2]/android.widget.RelativeLayout/android.widget.TextView").click()


    def unitMiles(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.TextView[1]").click()


    def num2(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.Button[2]").click()


    def num0(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.Button[1]").click()


    def result(self, value):
        num3 = self.driver.find_element_by_id(
            "com.ba.universalconverter:id/target_value").get_attribute("text")
        assert round(float(num3), 2) == float(value)
