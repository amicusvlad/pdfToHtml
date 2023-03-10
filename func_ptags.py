import re

def pTagsMerging(html):
    try:
        text = html
        pattern = r"</p>\n<p>[а-яё]"
        # Удаляем найденные последовательности из строки
        text = re.sub(pattern, lambda match: " " + match.group()[8], text)
        print('Удалены лишние переносы строк')
    except Exception as e:
        print('При удалении переносов возникла ошибка: ', e)
    return str(text)