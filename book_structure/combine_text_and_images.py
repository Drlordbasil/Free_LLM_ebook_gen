# This file is to combine the text from bookstructure/chapter_gen.py with the images from api_requests/free_image_gen.py
import docx
import os
from docx.shared import Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml
from docx.shared import RGBColor
from docx.enum.text import WD_COLOR_INDEX
from docx.shared import Length
from docx.enum.text import WD_LINE_SPACING
from docx.enum.text import WD_BREAK
from docx.shared import Cm
from docx.enum.text import WD_TAB_ALIGNMENT
class join_into_docx_format:
    def __init__(self, text, image_path, book_folder):
        self.text = text
        self.image_path = image_path
        self.book_folder = book_folder
        self.doc = docx.Document()
    def add_text(self):
        self.doc.add_heading('Chapter 1', level=1)
        self.doc.add_paragraph(self.text)
    def add_image(self):
        self.doc.add_picture(self.image_path, width=Inches(6))
    def save_doc(self):
        self.doc.save(os.path.join(self.book_folder, "output.docx"))