def fileSaving(fileName, content):
    try:
        # Сохранить содержимое страницы в файл.
        with open(fileName, "a", encoding="utf-8") as out_file:
            out_file.write(content)
        print('Результат успешно сохранен в файл: ', fileName)
    except Exception as e:
        print('Произошла ошибка при сохранении результата в файл:', e)