import os
from func_pdf2html import *
from func_tags import *
from func_lineBreaks import *
from func_saving import *
from func_ptags import *
from func_dialogues import *

for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".pdf"):
                pdfName = os.path.join(file)
# pdfName = path_file
# pdfName = '1.Гарри_Поттер_и_философский_камень.pdf'
destFile = pdfName.rstrip('pdf')+'html'

html = pdf2html(pdfName)
html = tagCleaning(html)
html = emptyLineBreaksRemoving(html)
html = pTagsMerging(html)
html = dialogues(html)
fileSaving(destFile, html)