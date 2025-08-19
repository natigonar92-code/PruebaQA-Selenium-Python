from selenium.webdriver.common.by import By
import time
from helpers import iniciar_driver, screenshot
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_registro():
    # Iniciar navegador
    driver = iniciar_driver()
    driver.get("https://bioseguridad.godoycordoba.com")
    driver.maximize_window()
    time.sleep(2)

    # Login con usuario inexistente
    usuario = driver.find_element(By.ID, "TxtUsuario_I")
    usuario.send_keys("uhtgs@test.com")
    clave = driver.find_element(By.ID, "TxtClave_I")
    clave.send_keys("12345")
    driver.find_element(By.XPATH, "//*[@id='BtnIngresar_CD']").click()
    time.sleep(2)

    # Guardar captura
    screenshot(driver, "login_usuario_inexistente")

    # Ir a registro
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Registrate aquí"))
    ).click()

    # Llenar formulario de registro
    razon_social = driver.find_element(By.ID, "TxtNombre_I")
    razon_social.send_keys("SeguroBolivarpt")
    wait = WebDriverWait(driver, 10)
    nit_input = wait.until(EC.element_to_be_clickable((By.ID, "TxtNit_I")))
    nit_input.clear()
    nit_input.send_keys("111014020")
    nit_input.send_keys(Keys.TAB)  # Disparar onblur/onchange si es necesario
    sector_input = driver.find_element(By.ID, "LstSector_I")
    sector_input.send_keys("Caficultor")
    time.sleep(1)  
    sector_input.send_keys(Keys.ARROW_DOWN)
    sector_input.send_keys(Keys.ENTER)
    tele_fono = driver.find_element(By.ID, "TxtTelefono_I")
    tele_fono.send_keys("3104245714")
    email = driver.find_element(By.ID, "TxtCorreo_I")
    email.send_keys("segurobptb92@yopmail.com")
    password = driver.find_element(By.ID, "TxtClave_I")
    password.send_keys("Pruebas1522#")

    screenshot(driver, "Llenar formulario de registro")

    # Enviar formulario
    driver.find_element(By.ID, "BtnRegistrar_CD").click()
    time.sleep(3)
    screenshot(driver, "Enviar formulario")
    driver.quit()

    