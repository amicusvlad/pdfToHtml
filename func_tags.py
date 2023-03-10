from bs4 import BeautifulSoup

def tagCleaning (html):
    try:
        # Прочитать содержимое переменной html в объект BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # Удалить все атрибуты у всех тегов
        for tag in soup.findAll(True):
            tag.attrs = {}

        # Удалить лишние теги, но оставить их содержимое
        for span_tag in soup.find_all('span'):
            span_tag.unwrap()
        for b_tag in soup.find_all('b'):
            b_tag.unwrap()
        for div_tag in soup.find_all('div'):
            div_tag.unwrap()
        for img_tag in soup.find_all('img'):
            img_tag.unwrap()
        print('Лишние теги удалены и очищены стили')
    except Exception as e:
        print('При работе с тегами возникла ошибка', e)
    return str(soup)