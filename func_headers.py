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