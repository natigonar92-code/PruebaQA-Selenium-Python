# 🚀 PruebaQA - Selenium con Python

Este proyecto contiene **pruebas automatizadas** desarrolladas en **Python** utilizando **Selenium WebDriver** y **Pytest**.

---

## 📋 Requisitos previos

Antes de ejecutar las pruebas, asegúrate de tener instalado:

- [Python 3.10+](https://www.python.org/downloads/)
- [Google Chrome](https://www.google.com/chrome/) (o el navegador que uses)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (compatible con tu versión de navegador)
- [pip](https://pip.pypa.io/en/stable/) (administrador de paquetes de Python)

---

## ⚙️ Instalación

1. **Clonar o descomprimir** este proyecto:
   ```bash
   git clone https://github.com/tu_usuario/PruebaQA-Selenium-Python.git
   cd PruebaQA-Selenium-Python
   ```

2. (Opcional, recomendado) **Crear entorno virtual**:
   ```bash
   python -m venv venv
   # En Linux/Mac
   source venv/bin/activate
   # En Windows
   venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

   > ⚠️ Si no existe el archivo `requirements.txt`, instala manualmente:
   ```bash
   pip install selenium pytest
   ```

---

## ▶️ Ejecución de pruebas

Ejecutar todas las pruebas con:

```bash
pytest tests/
```

Ejecutar un caso en específico (ejemplo `test_registro.py`):

```bash
pytest tests/test_registro.py
```

Ejecutar mostrando más detalles:

```bash
pytest -v
```

---

## 📂 Estructura del proyecto

```
PruebaQA-Selenium-Python/
│── tests/                 # Casos de prueba
│   ├── test_registro.py   # Ejemplo: prueba de registro
│── venv/                  # Entorno virtual (no subir a GitHub)
│── requirements.txt       # Dependencias del proyecto
│── README.md              # Este archivo
```

---

## ✅ Notas

- Asegúrate de que el **ChromeDriver** esté en el `PATH` del sistema.
- Si usas otro navegador (Firefox, Edge, etc.), actualiza la configuración en los tests.
- El entorno virtual `venv/` no debe subirse a GitHub, agrega `.gitignore`.

---
