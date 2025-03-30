from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time

app = FastAPI(
    title="JobScraper API",
    description="API para extraer y consultar ofertas de trabajo de portales tecnológicos.",
    version="1.0.0",
    docs_url="/swagger",
    redoc_url="/documentacion"
)


@app.get("/scrape")
def scrape():
    # Configurar Firefox para abrirse en modo normal (no headless)
    options = Options()
    options.headless = False

    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options
    )

    try:
        # 1. Navegar a la web
        driver.get("https://www.python.org")
        time.sleep(2)

        # 2. Hacer scroll hacia abajo (por ejemplo, 1000px)
        driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(2)

        # 3. Hacer click en un enlace (por ejemplo: 'Donate')
        donate_link = driver.find_element("link text", "Donate")
        donate_link.click()
        time.sleep(2)

        # 4. Tomar captura de pantalla
        screenshot_path = "screenshot.png"
        driver.save_screenshot(screenshot_path)

        # 5. Devolver el título de la página actual
        return {
            "final_title": driver.title,
            "screenshot": screenshot_path
        }

    finally:
        driver.quit()