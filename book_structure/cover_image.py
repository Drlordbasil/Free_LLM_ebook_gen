import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

class GenerateCoverImage:
    def __init__(self, cover_image_path, book_folder, book_id, book_title, author_name):
        self.cover_image_path = cover_image_path
        self.book_folder = book_folder
        self.book_id = book_id
        self.book_title = book_title
        self.author_name = author_name

    def generate_cover_pdf(self):
        try:
            output_path = os.path.join(self.book_folder, self.book_id, "cover.pdf")
            c = canvas.Canvas(output_path, pagesize=letter)

            # Add the cover image
            img = ImageReader(self.cover_image_path)
            c.drawImage(img, 0, 0, width=letter[0], height=letter[1])

            # Add the book title and author name
            c.setFont("Helvetica", 24)
            c.drawCentredString(letter[0] / 2, letter[1] - 100, self.book_title)
            c.setFont("Helvetica", 18)
            c.drawCentredString(letter[0] / 2, letter[1] - 130, f"by {self.author_name}")

            c.showPage()
            c.save()

            print(f"Generated cover PDF: {output_path}")
            return output_path
        except Exception as e:
            print(f"Error generating cover PDF: {str(e)}")
            raise