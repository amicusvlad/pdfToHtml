from ebooklib import epub
from bs4 import BeautifulSoup

# Открываем HTML-файл и парсим его с помощью BeautifulSoup
with open('example.html', 'r') as file:
    html = file.read()
    soup = BeautifulSoup(html, 'html.parser')

# Создаем объект книги и задаем метаданные
book = epub.EpubBook()
book.set_identifier('id123456')
book.set_title('Гарри Поттер и Кубок огня')
book.set_language('ru')
book.add_author('Дж. К. Ролинг')
book.set_cover('image.jpg', open('image.jpg', 'rb').read(), 'image/jpeg')
book.add_metadata('DC', 'series', 'Гарри Поттер')
book.add_metadata('DC', 'series_index', '4')
book.add_metadata('DC', 'publisher', 'РОСМЭН')

# Создаем оглавление из заголовков h2
toc = []
for tag in soup.find_all('h2'):
    chapter = epub.EpubHtml(title=tag.text, file_name='chapter{}.xhtml'.format(len(toc) + 1), lang='ru')
    chapter.set_content(str(tag))
    book.add_item(chapter)
    toc.append(chapter)

# Устанавливаем оглавление
book.toc = tuple(toc)

# Создаем файл книги
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# Создаем контейнер и добавляем книгу в него
book.spine = toc
book.epub_version = '3.0'
epub.write_epub('book.epub', book, {})
