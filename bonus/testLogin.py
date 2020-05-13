import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time #para hacer uso de implicity wait y del time.sleep


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome()  #Se exporta el chrome driver para poder ejecutar la prueba en chrome
        self.driver.implicitly_wait(10) #se espera 10 segundo antes de iniciar las acciones , para evitar que realice cosas en la pagina y todavia no esten cargadas
        self.driver.maximize_window() # Agranda la ventana a pantalla completa
        #Ingreso a la app
        self.driver.get("file:///C:/Users/Cristian%20Marquez/Desktop/Login%20Drixit/index.html") #se pone la ruta o url a testear

    #Definimos las acciones que vamos a realizar
    def test01(self):
    #hacer click sobre el placeholder de usuario
        usuario=self.driver.find_element(By.XPATH,"//*[@id='usuario']").send_keys("admin@drixit.com") #se le envia los datos al placeholder

    #se va hacia el placeholder del password
        contraseña=self.driver.find_element(By.XPATH,"//*[@id='contraseña']").send_keys("testing")

    #Se hace click al boton de log in para certificar el usuario y contraseña
        btnLog=self.driver.find_element(By.XPATH,"//*[@id='btnLog']").click()

        time.sleep(10)

    def tearDown(self):
        self.driver.close() #cerramos el navegador si el resultado es positivo

if __name__ == '__main__':
    unittest.main()
