import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_largest_image(driver):
    images = driver.find_elements(By.TAG_NAME, "img")
    largest_img = max(images, key=lambda img: int(img.get_attribute("width")) * int(img.get_attribute("height")), default=None)

    if largest_img:
        location = largest_img.location
        size = largest_img.size
        x, y = location['x'] + size['width'] // 2, location['y'] + size['height'] // 2
        return x, y
    return None

def scrape_images(url, pages):
    # Setup Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(3)  # Allow time for page to load

    for _ in range(pages):
        coords = get_largest_image(driver)
        if coords:
            pyautogui.moveTo(coords[0], coords[1], duration=0.5)
            pyautogui.click()
            time.sleep(2)  # Wait for next page to load
        else:
            print("No image found.")
            break

    driver.quit()

# Example usage
url = input("Enter the URL: ")
pages = int(input("Enter the number of pages to scrape: "))
scrape_images(url, pages)