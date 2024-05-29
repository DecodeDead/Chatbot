# streamlit_app/tests/test_system.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_upload_and_chat():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8501")  # Adjust URL if necessary

    # Add explicit wait to ensure the element is loaded
    wait = WebDriverWait(driver, 10)

    try:
        # Print page source for debugging
        print(driver.page_source)
        
        # Verify and locate upload element
        upload_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
        upload_element.send_keys("/path/to/filename.txt")

        time.sleep(2)  # Wait for upload to complete

        # Verify and locate question input
        question_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']")))
        question_input.send_keys("What is the capital of France?")
        question_input.send_keys(Keys.RETURN)

        time.sleep(2)  # Wait for response

        # Verify and locate response element
        response_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.element-container div.markdown-text-container p")))
        assert response_element.text == "Paris"

    except Exception as e:
        print(f"Error: {e}")

    finally:
        driver.quit()
