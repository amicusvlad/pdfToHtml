from ebooklib import epub
from bs4 import BeautifulSoup

# Read the HTML file
with open('file.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create a new EPUB book
book = epub.EpubBook()

# Set the book metadata
book.set_title('Гарри Поттер и Кубок огня')
book.set_language('ru')
book.add_author('Дж. К. Ролинг')
book.add_metadata('DC', 'series', 'Гарри Поттер')
book.add_metadata('DC', 'series_index', '4')
book.add_metadata('DC', 'publisher', 'РОСМЭН')

# Add the book cover
book.set_cover('image.jpg', open('image.jpg', 'rb').read())

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')
headers = soup.find_all('h2')
paragraphs = soup.find_all('p')

# Add the table of contents
toc = epub.EpubNav()
book.add_item(toc)
toc_item = epub.EpubNavItem('Оглавление', 'toc.xhtml', [])
toc.item.append(toc_item)
for header in headers:
    title = header.get_text()
    chapter_id = 'chapter-' + str(headers.index(header) + 1)
    chapter_link = chapter_id + '.xhtml'
    chapter = epub.EpubHtml(title=title, file_name=chapter_link, lang='ru')
    chapter.content = str(header) + str(header.find_next('p'))
    book.add_item(chapter)
    toc_item.sub_items.append(epub.EpubNavItem(title, chapter_link, []))

# Add the book spine
book.spine = ['nav']
book.spine += [chapter for chapter in book.items[1:]]

# Save the EPUB file
epub.write_epub('book.epub', book, {})


