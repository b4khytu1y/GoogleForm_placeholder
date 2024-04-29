import requests
import random
import time
from urllib.parse import urlencode

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
    form_data = {}
    for question, options in questions.items():
        form_data[f'entry.{question}'] = random.choice(options)
    
    user_agent = {'Referer': urlReferer,
                  'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
    
    # Преобразуем данные формы в строку
    data_str = urlencode(form_data)
    
    r = requests.post(urlResponse, data=data_str, headers=user_agent)
    print("Form submitted")
    time.sleep(2)  # Пауза между отправками формы

# Задаем количество раз, которое нужно отправить форму
num_submissions = 10

# Отправляем форму заданное количество раз
for _ in range(num_submissions):
    submit_form()
