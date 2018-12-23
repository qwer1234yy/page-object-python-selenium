import unittest
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from selenium.webdriver import Firefox
import MyEventListener


class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigate to %s" % url)
    def after_navigate_to(self, url, driver):
        print("After navigate to %s" % url)

driver = Firefox()
ef_driver=EventFiringWebDriver(driver,MyEventListener.MyListener)
ef_driver.get("http://zhihu.com")

assert "TestArt" in ef_driver.title

ef_driver.close()


if __name__ == '__main__':
    print('----')
    # unittest.main()
