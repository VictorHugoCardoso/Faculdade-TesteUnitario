from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser

class sistemaAcademico(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        cls.driver = webdriver.Chrome("C:/Users/victo/Documents/Github/testeUnitario/chromedriver.exe",options=option)
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

    def test_addDisciplina(self):
        self.driver.get("http://localhost:8000/disciplinas/")
        self.driver.find_element_by_name("newdisciplina").click()
        self.driver.find_element_by_name("nomeDisciplina").send_keys("Banco de dados")
        self.driver.find_element_by_name("savebutton").click()     

    def test_editDisciplina(self):
        self.driver.get("http://localhost:8000/disciplinas/")
        self.driver.find_element_by_name("editdisciplina").click()
        self.driver.find_element_by_name("nomeDisciplina").send_keys("plus")
        self.driver.find_element_by_name("savebutton").click()   

    def test_editNota(self):
        self.driver.get("http://localhost:8000/disciplinas/")
        self.driver.find_element_by_name("editnota").click()
        self.driver.find_element_by_name("editnotaaluno").click()
        self.driver.find_element_by_name("nota2").send_keys("5")
        self.driver.find_element_by_name("savebutton").click()

    def test_addPresenca(self):
        self.driver.get("http://localhost:8000/disciplinas/")
        self.driver.find_element_by_name("namedisciplina").click()
        self.driver.find_element_by_name("addpresenca").click()
        self.driver.find_element_by_name("backbutton").click()              

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/victo/Desktop"))
