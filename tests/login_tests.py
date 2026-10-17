
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login():
    """Verify login using valid student credentials."""
    driver = webdriver.Chrome()

    try:
        driver.get("http://localhost:3000/login")

        driver.find_element(By.NAME, "email").send_keys(
            "student@example.com"
        )
        driver.find_element(By.NAME, "password").send_keys(
            "TestPassword123"
        )
        driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("dashboard") 
        )

        assert "dashboard" in driver.current_url.lower()

    finally:
        driver.quit()
