import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

GoogleURL = 'https://docs.google.com/forms/d/e/1FAIpQLSfUDj5d5o4DMUbWLj75UU4G9WJE33ovZmjccKtRkTluwOiQZA'

urlResponse = GoogleURL + '/formResponse'
urlReferer = GoogleURL + '/viewform'

# Список вопросов и их вариантов ответов
questions = {
    "How frequently do you interact with virtual characters based on AI?": ["Daily", "Weekly", "Monthly", "Rarely or Never"],
    "What is your primary reason for interacting with virtual characters?": ["Entertainment", "Learning", "Assistance with tasks", "Other (please specify)"],
    "How satisfied are you with the current virtual character interactions available?": ["Very satisfied", "Somewhat satisfied", "Neutral", "Somewhat dissatisfied", "Very dissatisfied"],
    "What features do you find most important in a virtual character?": ["Natural language understanding", "Emotional intelligence", "Personalization", "Visual appearance", "Other (please specify)"],
    "How likely are you to recommend our virtual character application to others?": ["Very likely", "Likely", "Neutral", "Unlikely", "Very unlikely"],
    "Have you encountered any challenges or frustrations while interacting with virtual characters? If yes, please describe.": ["Yes", "No"],
    "How comfortable are you with the idea of virtual characters having the ability to mimic human emotions?": ["Very comfortable", "Somewhat comfortable", "Neutral", "Somewhat uncomfortable", "Very uncomfortable"],
    "Do you believe virtual characters based on AI have the potential to replace human interaction in certain scenarios?": ["Yes, completely", "Yes, to some extent", "No, not at all"],
    "Which aspect of interacting with a virtual character do you find most appealing?": ["Convenience", "Novelty", "Learning experience", "Emotional connection", "Other (please specify)"],
    "How important is it for virtual characters to have distinct personalities?": ["Very important", "Somewhat important", "Neutral", "Not very important", "Not important at all"],
    "In what areas do you think virtual characters based on AI could improve?": ["Understanding user intent", "Providing accurate information", "Emotional responses", "Visual representation", "Other (please specify)"],
    "Would you prefer virtual characters to have a consistent personality across different interactions, or should they adapt their personality based on the user?": ["Consistent personality", "Adaptive personality", "No preference"]
}

# Функция для отправки ответов
def submit_form():
    driver = webdriver.Chrome()
    driver.get(GoogleURL)
    
    for question, options in questions.items():
        # Находим все радиокнопки для текущего вопроса
        radio_buttons = driver.find_elements(By.XPATH, f"//div[contains(text(), '{question}')]/following-sibling::div//span[@role='radio']")
        # Выбираем случайную радиокнопку
        random.choice(radio_buttons).click()
    
    # Нажимаем кнопку "Submit"
    submit_button = driver.find_element(By.XPATH, "//div[@role='button' and contains(text(), 'Submit')]")
    submit_button.click()
    
    time.sleep(2)  # Пауза между отправками формы
    driver.quit()

# Задаем количество раз, которое нужно отправить форму
num_submissions = 10

# Отправляем форму заданное количество раз
for _ in range(num_submissions):
    submit_form()
