from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.calculator.net/")
        self.driver.maximize_window()

    def test_percentage(self):
        self.driver.find_element(By.XPATH,'//*[@id="contentout"]/table/tbody/tr/td[3]/div[2]/a').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,'//*[@id="content"]/table[2]/tbody/tr/td/div[3]/a').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, "cpar1").send_keys('10')
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, "cpar2").send_keys('50')
        self.driver.find_element(By.XPATH,'//*[@id="content"]/table[1]/tbody/tr[2]/td/input[2]').click()
        result=self.driver.find_element(By.XPATH,'//*[@id="content"]/p[2]/font/b').text
        self.assertEqual(int(result), 5,
                         'incorrect percentage')
    
    def tearDown(self):
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(CalculatorTestCase('test_percentage'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())


'''
def test():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.calculator.net/")
    driver.maximize_window()
    #driver.find_element_by_xpath('//*[@id="contentout"]/table/tbody/tr/td[3]/div[2]/a').click()
    driver.find_element(By.XPATH,'//*[@id="contentout"]/table/tbody/tr/td[3]/div[2]/a').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,'//*[@id="content"]/table[2]/tbody/tr/td/div[3]/a').click()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "cpar1").send_keys('10')
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "cpar2").send_keys('50')
    driver.find_element(By.XPATH,'//*[@id="content"]/table[1]/tbody/tr[2]/td/input[2]').click()
    result=driver.find_element(By.XPATH,'//*[@id="content"]/p[2]/font/b').text
    print(result)
    driver.quit()
'''

