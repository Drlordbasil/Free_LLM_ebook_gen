import logging
import os
from book_structure import chapter_gen
from api_requests import free_image_gen
from book_structure import combine_text_and_images
from config import all_book_folder, book_id
import docx
from kdp_requirements import Generate_kdp_details
from book_structure import title_gen
def generate_chapters(prompt, num_chapters):
    try:
        chapter_generator = chapter_gen.Generate_chapters_dynamically(prompt, num_chapters)
        chapters = chapter_generator.generate_chapters()
        logging.info("Chapters generated successfully.")
        return chapters
    except Exception as e:
        logging.error(f"Error generating chapters: {str(e)}")
        raise

def generate_and_combine_images(chapters, book_folder, book_id):
    combined_doc = docx.Document()
    for i, chapter in enumerate(chapters):
        try:
            image_filename = f"chapter_{i+1}_image.jpg"
            free_image_gen.generate_context_image(book_folder=book_folder, book_id=book_id, chapter_content=chapter, image_filename=image_filename)
            combine = combine_text_and_images.join_into_docx_format(text=chapter, image_path=f"{book_folder}/{book_id}/{image_filename}", book_folder=f"{book_folder}/{book_id}", chapter_title=f"Chapter {i+1}")
            combine.add_text(combined_doc)
            combine.add_image(combined_doc)
            logging.info(f"Image generated and combined for chapter {i+1}.")
            print(f"Generated image for chapter {i+1}: {book_folder}/{book_id}/{image_filename}")
        except Exception as e:
            logging.error(f"Error generating or combining image for chapter {i+1}: {str(e)}")
            raise

    output_path = os.path.join(book_folder, book_id, "output.docx")
    combined_doc.save(output_path)
    print(f"Generated docx file: {output_path}")


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    num_chapters = 5
    title = title_gen.generate_title()
    book_title = f"{title}"
    author_name = "Anthony Snider"
    prompt = f"Write a novel about the title {book_title} by {author_name} and if no context is given, generate the start of the story.ALWAYS AVOID: To be continued, The End, or any other phrases that indicate the story is incomplete."


    print("Generating chapters...")
    chapters = generate_chapters(prompt, num_chapters)
    kdp=Generate_kdp_details(book_title, author_name, chapters[0], book_id, all_book_folder)
    kdp_details=kdp.generate()
    print(kdp_details)
    print("Generating and combining images...")
    generate_and_combine_images(chapters, all_book_folder, book_id)

    print("Book generation completed.")

if __name__ == "__main__":
    main()