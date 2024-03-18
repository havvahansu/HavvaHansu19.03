from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://kariyer.baykartech.com/")  

def click_navbar_element(nav_element):
    nav_element.click()
   
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
   
    soup = BeautifulSoup(driver.page_source, "html.parser")
 
    print("Page Title:", soup.title.text)


def find_navbar_elements():
    navbar_elements = driver.find_elements(By.CSS_SELECTOR, ".navbar-element")  # Navbar elementlerinin CSS seçicisini buraya girin
    return navbar_elements

def change_language(language):
    def change_language(language):
    language_dropdown = driver.find_element(By.ID, "language-dropdown")  # Dil seçim dropdown'unun ID'sini buraya girin
    language_dropdown.click()

    language_options = driver.find_elements(By.siteCustomLi, "language-option")  # Dil seçeneklerinin sınıfını buraya girin

 
    for option in language_options:
        if option.text == language:
            option.click()
            break


    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    soup = BeautifulSoup(driver.page_source, "html.parser")
 

navbar_elements = find_navbar_elements()
for element in navbar_elements:
    click_navbar_element(element)

change_language("Portuguese")


driver.quit()
