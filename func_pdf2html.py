import fitz
from bs4 import BeautifulSoup
import os

def pdf2html(pdfName):
    # Открываем PDF-файл
    pdf = fitz.open(pdfName)

    # Проходим по всем страницам PDF-файла
    for page in pdf:
        # Извлекаем текст страницы
        text = page.get_text("html")#.strip()

        # Создаем HTML-файл с именем "example.html"
        with open('example.html', 'a', encoding='utf-8') as file:
            # Записываем текст страницы в HTML-файл
            file.write(f'<div>{text}</div>')

    with open("example.html", "r") as f:
        html = BeautifulSoup(f, "html.parser")

    os.remove('example.html')

    return str(html)
