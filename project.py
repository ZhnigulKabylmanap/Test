from selenium import webdriver

def test_web_page():
 driver=webdriver.Chrome()
 driver.get("https://www.kaspi.kz/")
 assert "Kaspi" in driver.title
 driver.quit()


def test_google_title():
 driver = webdriver.Chrome()
 driver.get("https://google.com")
 assert driver.title == "Google"
 driver.quit()
