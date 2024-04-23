from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura el navegador
driver = webdriver.Chrome()  # Asegúrate de tener instalado el controlador adecuado para tu navegador
driver.get("https://www.colpensiones.gov.co/")
wait = WebDriverWait(driver, 10)

# Encuentra los elementos por ID, nombre y clase para el inicio de sesión
username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "login-button")))

# Ingresa las credenciales
username_field.send_keys("tu_usuario")
password_field.send_keys("tu_contraseña")

# Haz clic en el botón de inicio de sesión
login_button.click()

# Espera a que la página de inicio de sesión se cargue completamente
wait.until(EC.url_matches("https://www.colpensiones.gov.co/inicio"))

# Proceso de recuperación de cuenta por medio de Partial Link
recovery_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "recuperar cuenta")))
recovery_link.click()

# Aquí puedes continuar con el proceso de recuperación de cuenta

# Cierra el navegador al finalizar
driver.quit()
