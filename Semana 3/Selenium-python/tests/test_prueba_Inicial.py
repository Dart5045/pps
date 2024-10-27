# Para iniciar el navegador, necesitamos crear una nueva instancia de nuestro Webdriver.
# El controlador web representa el navegador y es el que nos permite interactuar con él.
# para realizar la instancia, necesitamos importarlo con la siguiente línea en la parte superior de nuestro archivo
from selenium import webdriver

import pytest


from webdriver_manager.chrome import ChromeDriverManager

# Para iniciar el navegador, necesitamos crear una nueva instancia de nuestro Webdriver.
# En este caso, instalamos el driverMangaer
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))


def test_Prueba():
    driver.get("http://www.google.com")
    titulo = driver.title
    assert titulo == "Google"
