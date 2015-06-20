from selenium import webdriver
import unittest


class TestNuevoVisitante(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_ingresa_a_la_pagina_y_muestra_informacion(self):
        # el usuario entra a la pagina principal de la plataforma de elige.la
        self.browser.get('http://localhost:8000')

        # ve que en el titulo dice
        self.assertIn('Elige.la', self.browser.title)
        self.fail('Acabo la prueba')

        # ve que hay informacion del taller

        # ve que se muestran los auspiciadores

if __name__ == '__main__':
    unittest.main(warnings='ignore')
