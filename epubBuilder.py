import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

# загрузка исходного HTML файла
with open('example.html', 'r', encoding='utf-8') as f:
    html = f.read()

# парсинг HTML
soup = BeautifulSoup(html, 'html.parser')

# создание объекта книги
book = epub.EpubBook()

# установка метаданных
book.set_title('Гарри Поттер и Кубок огня')
book.set_language('ru')
book.add_author('Дж. К. Ролинг')
book.add_metadata('DC', 'series', 'Гарри Поттер')
book.add_metadata('DC', 'series_index', '4')
book.add_metadata('DC', 'publisher', 'РОСМЭН')
book.set_cover('image.jpg', open('image.jpg', 'rb').read())

# создание оглавления
toc = []
for h2 in soup.find_all('h2'):
    toc.append(epub.Link(h2['id'], h2.text, h2['id']))
book.toc = toc
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# создание контента
content = epub.EpubHtml(title='Содержание', file_name='content.xhtml', lang='ru')
content.content = str(soup.find('body'))

# добавление контента в книгу
book.add_item(content)

# упаковка книги в epub-файл
epub.write_epub('book.epub', book, {})
