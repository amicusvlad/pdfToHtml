from bs4 import BeautifulSoup

def emptyLineBreaksRemoving(html):
    try:
        # разбиваем текст на строки
        lines = html.split("\n")

        # удаляем пустые строки
        non_empty_lines = [line for line in lines if line.strip() != ""]

        # объединяем оставшиеся строки с помощью переносов строк
        clean_text = "\n".join(non_empty_lines)

        print('Пустые переносы строк удалены')
    except Exception as e:
        print('При удалении пустых переносов строк возникла ошибка:', e)

    return clean_text