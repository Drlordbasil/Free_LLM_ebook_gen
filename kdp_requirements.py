import os
from api_requests import local_LLM_api

class Generate_kdp_details:
    def __init__(self, book_title, chapter, book_id, all_book_folder):
        self.book_title = book_title
        self.chapter = chapter
        self.author_name = "Anthony Snider"
        self.book_id = book_id
        self.book_folder = all_book_folder

    def generate(self):
        kdp_details_text_format = f"Title: {self.book_title}\nAuthor: {self.author_name}\nChapter: {self.chapter}"
        kdp_details = local_LLM_api.mistral_chat(
            system="""
            Analyze the provided text containing the title and the first chapter of an ebook. 
            Extract the necessary information to formulate a Title, generate a Subtitle based on the content,
            suggest a fair market price in USD, create a Short Description with high keyword density for SEO purposes, 
            identify seven relevant keywords, recommend an Age Range, and define a Category breadcrumb. 
            Ensure the response is organized and detailed, adhering to the specified format.
            """,
            user=f"""
            {kdp_details_text_format}
            I have a text snippet from an ebook that includes the title and the first chapter. 
            Based on this text, I need the following publishing details formatted correctly:

            Title: Extracted from the text.
            Subtitle: Generated based on the content.
            Price Suggested to List (honest USD price): Based on the content and genre.
            Description: Short Description for the marketplace with high keyword density for SEO.
            Seven Keywords: 1, 2, 3, 4, 5, 6, 7 (Identify relevant keywords from the text).
            Age Range: Suggest an appropriate age range (e.g., 1-18+).
            Category Breadcrumb Format: cat1 > subcat > final (Determine a fitting category path based on the content).

            Please analyze the text and provide the details in the specified format.
            """
        )
        print("KDP details generated successfully.")
        return kdp_details

    def save_details_to_book_folder(self):
        try:
            details_path = os.path.join(self.book_folder, self.book_id, "kdp_details.txt")
            with open(details_path, "w") as file:
                file.write(self.generate())
            print(f"KDP details saved successfully: {details_path}")
            return details_path
        except Exception as e:
            print(f"Error saving KDP details: {str(e)}")
            return None