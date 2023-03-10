import os
from func_pdf2html import *
from func_tags import *
from func_lineBreaks import *
from func_saving import *
from func_ptags import *
from func_dialogues import *
from func_headers import *

for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".pdf"):
                pdfName = os.path.join(file)
destFile = pdfName.rstrip('pdf')+'html'

html = pdf2html(pdfName)
html = tagCleaning(html)
html = emptyLineBreaksRemoving(html)
html = pTagsMerging(html)
html = dialogues(html)
fileSaving('temp.html', html)
html = headers(html)
html = headersId()
fileSaving(destFile, html)