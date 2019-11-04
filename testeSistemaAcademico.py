from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import HtmlTestRunner

class sistemaAcademico(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:/Users/Guilherme/Desktop/TESTE/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_addAluno(self):
        self.driver.get("http://localhost:8000/alunos/")
        self.driver.find_element_by_name("newaluno").click()
        self.driver.find_element_by_name("nomeAluno").send_keys("blablabla")
        self.driver.find_element_by_name("savebutton").click()

    def test_editAluno(self):
        self.driver.get("http://localhost:8000/alunos/")
        self.driver.find_element_by_name("editaluno").click()
        self.driver.find_element_by_name("nomeAluno").send_keys("blebleble")
        self.driver.find_element_by_name("savebutton").click() 

    def test_removeAluno(self):
        self.driver.get("http://localhost:8000/alunos/")
        self.driver.find_element_by_name("removealuno").click()
        self.driver.find_element_by_name("deletealuno").click()       

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Guilherme/Desktop/TESTE'))

