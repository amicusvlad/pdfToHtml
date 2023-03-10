from bs4 import BeautifulSoup
import uuid
import os
def headers(text):
    try:
        # Разбиваем текст на строки
        lines = text.split("\n")

        # Итерируемся по строкам и обрабатываем каждую
        for i in range(len(lines)):
            # Если строка начинается со слова "Глава"
            if lines[i].startswith("<p>Глава"):
                # Превращаем строку в заголовок
                lines[i] = lines[i].replace("<p>", "<h2>")
                lines[i] = lines[i].replace("</p>", "</h2>")

        # Объединяем строки обратно в текст
        result = "\n".join(lines)

        print('Заголовки сформированы успешно')
    except Exception as e:
        print('При формировании заголовков возникла ошибка: ', e)
    return result

def headersId():
    try:
        with open('temp.html') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')
        for chapter in soup.find_all('h2'):
            chapter['id'] = str(uuid.uuid4())
        print('Заголовкам присвоены уникальные ID')
    except Exception as e:
        print('Ошибка при присвоении ID заголовкам: ', e)
    os.remove('temp.html')
    return str(soup)