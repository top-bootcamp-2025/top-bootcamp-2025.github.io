from selenium import webdriver
from selenium.webdriver.common.by import By
# Создайте HTML-страницу с рецептом, используя только теги h1, h2 и p.
# Требования к содержимому:

BASE_URL = "https://tatiana-1009.github.io/Recipe.html"

# Название блюда (тег h1):
# Текст: "Простой бутерброд с сыром".
def test_01_h1():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    assert driver.find_element(By.TAG_NAME, "h1").text == "Простой бутерброд с сыром"

# Раздел "Что нужно" (тег h2):
def test_02_what():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    assert driver.find_element(By.TAG_NAME, "h2").text == "Что нужно"

# В абзаце (тег p) перечислите ингредиенты через запятую:
# "Хлеб, сливочное масло, сыр, зелень (по желанию)".
def test_03_ingredients():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    assert driver.find_element(By.TAG_NAME, "p").text == "Хлеб, сливочное масло, сыр, зелень (по желанию)"

# Раздел "Как приготовить" (тег h2):
# !!!! ЭТОТ ТЕСТ НЕ БУДЕТ ТАК РАБОТАТЬ
# Для этой проверке нам понадобится xPath
def test_04_how():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    assert driver.find_element(By.CSS_SELECTOR, "h2:nth-of-type(2)").text == "Как приготовить"

    #########################################
    # ЭТО НЕПРАВИЛЬНАЯ ПРОВЕРКА, ПОТОМУ ЧТО В ТРЕБОВАНИЯХ ЯВНО УКАЗАНО, ЧТО
    # ТЕКСТ "Как приготовить" должен быть в теге h2
    # А мы такой проверкой проверяем просто, что где-то на странице есть этот текст
    assert "Как приготовить" in driver.find_element(By.TAG_NAME, "body").text
    #########################################

# Разбейте инструкцию на отдельные шаги, каждый в своём абзаце (p):
# "Намажьте хлеб маслом."
# "Положите сверху ломтик сыра."
# "Добавьте зелень, если хотите."
# "Бутерброд готов!"
def test_05_steps():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    assert driver.find_element(By.CSS_SELECTOR, "p:nth-of-type(2)").text == "Намажьте хлеб маслом."
    assert driver.find_element(By.CSS_SELECTOR, "p:nth-of-type(3)").text == "Положите сверху ломтик сыра."
    assert driver.find_element(By.CSS_SELECTOR, "p:nth-of-type(4)").text == "Добавьте зелень, если хотите."
    assert driver.find_element(By.CSS_SELECTOR, "p:nth-of-type(5)").text == "Бутерброд готов!"

