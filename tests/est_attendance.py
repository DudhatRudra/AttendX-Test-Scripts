
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_mark_attendance():
    """Verify that attendance is marked successfully."""
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

        wait = WebDriverWait(driver, 10)

        button = wait.until(
            EC.element_to_be_clickable((By.ID, "mark-attendance"))
        )
        button.click()

        status = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "attendance-status")
            )
        )

        assert "marked" in status.text.lower()

    finally:
        driver.quit()
