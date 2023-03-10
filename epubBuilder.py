# title = 'Гарри Поттер и Кубок огня'
# book.set_title(title)
# book.set_language('ru')
# book.add_author('Дж. К. Ролинг')
# book.add_metadata('DC', 'series', 'Гарри Поттер')
# book.add_metadata('DC', 'series_index', '4')
# book.add_metadata('DC', 'publisher', 'РОСМЭН')
# book.set_cover('image.jpg', open('image.jpg', 'rb').read())

import os
from ebooklib import epub
from bs4 import BeautifulSoup
import uuid


book = epub.EpubBook()
title = 'Гарри Поттер и Кубок огня'
book.set_title(title)
book.set_language('ru')
book.add_author('Дж. К. Ролинг')
book.add_metadata('DC', 'series', 'Гарри Поттер')
book.add_metadata('DC', 'series_index', '4')
book.add_metadata('DC', 'publisher', 'РОСМЭН')
book.set_cover('image.jpg', open('image.jpg', 'rb').read())


with open('example.html') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')

# Найти все теги h2 и добавить к ним уникальный id
for chapter in soup.find_all('h2'):
    chapter['id'] = str(uuid.uuid4())

# Теперь можно использовать созданные id вместо текстовых заголовков для создания оглавления:
chapter_list = soup.find_all('h2')

# Создайте объект epub-оглавления
epub_toc = epub.EpubNav()
epub_toc.add_item(epub.EpubNav())

# Добавьте каждый заголовок в оглавление и создайте новую главу для каждого заголовка
for chapter in chapter_list:
    chapter_title = chapter.text
    chapter_id = chapter['id']
    chapter_content = str(chapter) + str(chapter.find_next_sibling())
    c = epub.EpubHtml(title=chapter_title, file_name='chapter_{}.xhtml'.format(chapter_id), lang='hr')
    c.content = chapter_content
    book.add_item(c)
    epub_toc.add_nav_point(epub.NavPoint(chapter_title, 'chapter_{}.xhtml'.format(chapter_id), []))

# Добавьте epub-оглавление в книгу
book.add_item(epub_toc)
book.toc = epub_toc
book.spine.append(epub_toc)

epub.write_epub('book.epub', book, {})
