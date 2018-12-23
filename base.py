import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# this Base class is serving basic attributes for every single page inherited from Page class

class Page(object):
    def __init__(self, driver, base_url='http://www.app.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
 
    def find_element(self, *locator):
        self.wait_page_load_done()
        self.wait_presence_of_element(*locator)
        time.sleep(1)
        return self.driver.find_element(*locator)
 
    def open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        
    def get_title(self):
        return self.driver.title
        
    def get_url(self):
        return self.driver.current_url
    
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    # added
    def get_page_resource(self):
        print('get_page_resource')
        html = self.driver.page_source
        return html

    def wait_page_load_done(self):
        print('wait_page_load_done')
        for i in range(1, 5):
            print(i)
            print(self.driver.execute_script('return document.readyState'))
            if ('complete' == self.driver.execute_script('return document.readyState')):
                print('complete')
                break
            else:
                time.sleep(1)

    def wait_presence_of_element(self, *locator):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(*locator)
            )
            print('wait_presence_of_element_presence')
        except Exception as e:
            print('wait_presence_of_element_failed:'+e.__str__())
        finally:
            print('wait_presence_of_element_over')