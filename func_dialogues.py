import re

def dialogues(html):
    try:
        text = html
        pattern = r"</p>\n<p>—"

        # Удаляем найденные последовательности из строки
        text = re.sub(pattern, lambda match: "<br/>" + match.group()[8], text)
        print('Удалены лишние переносы строк')
    except Exception as e:
        print('При удалении переносов возникла ошибка: ', e)
    return str(text)