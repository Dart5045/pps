# Para iniciar el navegador, necesitamos crear una nueva instancia de nuestro Webdriver.
# El controlador web representa el navegador y es el que nos permite interactuar con él.
# para realizar la instancia, necesitamos importarlo con la siguiente línea en la parte superior de nuestro archivo
from selenium import webdriver


from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


# Crear objeto de opciones para indicarle a chrome que deje el explorador abierto una vez hayan finalizado las pruebas
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# browser = webdriver.Chrome(options=options) # Crear una variable que se va a encargar a maniupular acciones del explorador


# Para iniciar el navegador, necesitamos crear una nueva instancia de nuestro Webdriver.
browser = webdriver.Chrome()

# Navegar a una página web
browser.get("https://github.com")

# Esperar a que la página se carge
browser.implicitly_wait(10)

# Si yo quiero que pinche en un elemento
link = browser.find_element(By.LINK_TEXT, "Sign in")

# Hacer clic en un elemento
link.click()

# Localizar un elemento por ID
user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")

# Enviar teclas a un elemento
user_input.send_keys("Mi_usuario_github")
pass_input.send_keys("Mi_pass_github")

user_input.send_keys(Keys.RETURN)

# Localizar un elemento por clase CSS
profile = browser.find_element(
    By.CLASS_NAME, "css-truncate.css-truncate-target.ml-1")

# Obtener un atributo de un elemento
label = profile.get_attribute("innerHTML")


# Validamos nuestro resultado
# Ahora solo tenemos que validar que obtuvimos el resultado deseado!
# Esto es tan simple como verificar que podemos encontrar un elemento que esperamos ver en este sitio
assert "bgonzales" in label

# Cerrar el navegador
browser.quit()
