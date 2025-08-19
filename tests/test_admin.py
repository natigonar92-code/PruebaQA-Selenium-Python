from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from helpers import iniciar_driver, screenshot

# Datos
sectores = [
    {"nombre": "Agriculturas", "tema": "20"},
    {"nombre": "Artes", "tema": "30"},
    {"nombre": "Tormeta", "tema": "40"}
]

temas = [
    {"sector": "Agriculturas", "nombre": "Tecnología"},
    {"sector": "Artes", "nombre": "Salud"},
    {"sector": "Tormeta", "nombre": "Ambiente"}
]

# Crear sector
def crear_sector(driver, nombre, tema):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Nuevo']"))
    ).click()

    sector_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ContentPlaceHolder_GridSector_DXEditor1_I"))
    )
    sector_input.clear()
    sector_input.send_keys(nombre)

    tema_input = driver.find_element(By.ID, "ContentPlaceHolder_GridSector_DXEditor2_I")
    tema_input.clear()
    tema_input.send_keys(tema)

    screenshot(driver, f"Sector_{nombre}")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Actualizar']"))
    ).click()
    time.sleep(2)

# Crear tema
def crear_tema(driver, sector_nombre, tema_nombre):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Nuevo']"))
    ).click()

    sector_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ContentPlaceHolder_GridTema_DXEditor1_I"))
    )
    sector_input.clear()
    sector_input.send_keys(sector_nombre)
    time.sleep(0.5)
    sector_input.send_keys(Keys.ARROW_DOWN)
    sector_input.send_keys(Keys.ENTER)

    tema_input = driver.find_element(By.ID, "ContentPlaceHolder_GridTema_DXEditor2_I")
    tema_input.clear()
    tema_input.send_keys(tema_nombre)

    screenshot(driver, f"Tema_{tema_nombre}")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Actualizar']"))
    ).click()
    time.sleep(2)

# Crear subtemas
def crear_subtemas(driver, sector_nombre, tema_nombre):
    for i in range(1, 4):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Nuevo']"))
        ).click()

        sector_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ContentPlaceHolder_GridSubtema_DXEditor1_I"))
        )
        sector_input.clear()
        sector_input.send_keys(sector_nombre)
        time.sleep(1)
        sector_input.send_keys(Keys.ARROW_DOWN)
        sector_input.send_keys(Keys.ENTER)

        tema_input = driver.find_element(By.ID, "ContentPlaceHolder_GridSubtema_DXEditor2_I")
        tema_input.clear()
        tema_input.send_keys(tema_nombre)
        time.sleep(1)
        tema_input.send_keys(Keys.ARROW_DOWN)
        tema_input.send_keys(Keys.ENTER)

        subtema_nombre = f"Subtema_{i}"
        subtema_input = driver.find_element(By.ID, "ContentPlaceHolder_GridSubtema_DXEditor3_I")
        subtema_input.clear()
        subtema_input.send_keys(subtema_nombre)
        time.sleep(3)

        screenshot(driver, f"Subtema_{subtema_nombre}")
        WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Actualizar']"))
        ).click()
        time.sleep(4)

# Función para seleccionar opciones en dropdowns personalizados
def seleccionar_custom_dropdown(driver, locator_click, locator_lista, valor):
    # 1. Clic en el dropdown que abre opciones
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator_click)).click()
    time.sleep(0.5)

    # 2. Esperar las opciones desplegadas
    opciones = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(locator_lista))

    # 3. Buscar opción por texto y hacer clic
    for opcion in opciones:
        if opcion.text.strip() == valor:
            opcion.click()
            break

    time.sleep(0.5)  # validación opción seleccionada

# Crear preguntas
def crear_preguntas(driver, sector, tema, subtema):
    # Navegar a Preguntas
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='Pregunta.aspx']"))
    ).click()
    time.sleep(2)

    for i in range(1, 4):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Nuevo']"))
        ).click()

    # Seleccionar sector
    seleccionar_custom_dropdown(
    driver,
    (By.ID, "ContentPlaceHolder_GridPregunta_DXEditor1_B-1"),
    (By.XPATH, "//div[contains(@id,'ContentPlaceHolder_GridPregunta_DDD_PW')]//tr"),
    sector
)

# Seleccionar tema
    seleccionar_custom_dropdown(
    driver,
    (By.ID, "ContentPlaceHolder_GridPregunta_DXEditor2_B-1"),
    (By.XPATH, "//div[contains(@id,'ContentPlaceHolder_GridPregunta_DDD_PW')]//tr"),
    tema
)

# Seleccionar subtema
    seleccionar_custom_dropdown(
    driver,
    (By.ID, "ContentPlaceHolder_GridPregunta_DXEditor3_B-1"),
    (By.XPATH, "//div[contains(@id,'ContentPlaceHolder_GridPregunta_DDD_PW')]//tr"),
    subtema
)


# Ingresar pregunta
    pregunta_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ContentPlaceHolder_GridPregunta_DXEditor4_I"))
        )
    texto = f"¿Cuál es el nombre su perro {i}?"
    pregunta_input.clear()
    pregunta_input.send_keys(texto)

    screenshot(driver, f"Pregunta_{i}")

        # Guardar
    actualizar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Actualizar']"))
        )
    driver.execute_script("arguments[0].scrollIntoView(true);", actualizar)
    actualizar.click()
    time.sleep(1)

# Test principal
def test_registro():
    driver = iniciar_driver()
    driver.get("https://bioseguridad.godoycordoba.com/Admin")
    driver.maximize_window()
    time.sleep(2)

    # Login
    driver.find_element(By.ID, "TxtUsuario_I").send_keys("bioadmin")
    driver.find_element(By.ID, "TxtClave_I").send_keys("B10@dm1n")
    screenshot(driver, "Login")
    driver.find_element(By.ID, "BtnIngresar_CD").click()
    time.sleep(2)

    # Crear sectores
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='Sector.aspx']"))
    ).click()
    time.sleep(3)
    for sector in sectores:
        crear_sector(driver, sector["nombre"], sector["tema"])

    # Crear temas
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='Tema.aspx']"))
    ).click()
    time.sleep(3)
    for tema in temas:
        crear_tema(driver, tema["sector"], tema["nombre"])

    # Crear subtemas
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='Subtema.aspx']"))
    ).click()
    time.sleep(3)
    crear_subtemas(driver, temas[0]["sector"], temas[0]["nombre"])

    # Crear preguntas con el primer subtema
    crear_preguntas(driver, temas[0]["sector"], temas[0]["nombre"], "Subtema_1")

    driver.quit()

