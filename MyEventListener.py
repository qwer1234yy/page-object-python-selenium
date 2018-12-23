from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver


class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print('before_navigate_to {0}'.format(url))

    def after_navigate_to(self, url, driver):
        print('after_navigate_to {0}'.format(url))

    def before_navigate_back(self, driver):
        print('before_navigate_back')

    def after_navigate_back(self, driver):
        print('after_navigate_back')

    def before_navigate_forward(self, driver):
        print('before_navigate_forward')

    def after_navigate_forward(self, driver):
        print('after_navigate_forward')

    def before_find(self, by, value, driver):
        print('before_find {0} {1} {2}'.format(by, value, driver))

    def after_find(self, by, value, driver):
        print('after_find {0} {1} {2}'.format(by, value, driver))

    def before_click(self, element, driver):
        print('before_click {0} {1}'.format(element, driver))

    def after_click(self, element, driver):
        print('after_click{0} {1}'.format(element, driver))

    def before_change_value_of(self, element, driver):
        print('before_change_value_of {0} {1}'.format(element, driver))

    def after_change_value_of(self, element, driver):
        print('after_change_value_of {0} {1}'.format(element, driver))

    def before_execute_script(self, script, driver):
        print('before_execute_script {0} {1}'.format(script, driver))

    def after_execute_script(self, script, driver):
        print('after_execute_script {0} {1}'.format(script, driver))

    def before_close(self, driver):
        print('before_close')

    def after_close(self, driver):
        print('after_close')

    def before_quit(self, driver):
        print('before_quit')

    def after_quit(self, driver):
        print('after_quit')

    def on_exception(self, exception, driver):
        print('on_exception {0} {1}'.format(exception, driver))