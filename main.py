import logging
from book_structure import chapter_gen
from api_requests import free_image_gen
from book_structure import combine_text_and_images
from config import all_book_folder, book_id

def generate_chapter(prompt):
    try:
        chapter_generator = chapter_gen.Generate_chapters_dynamically(prompt)
        chapter = chapter_generator.generate_chapters()
        logging.info("Chapter generated successfully.")
        print(f"Generated chapter: {chapter}")
        return chapter
    except Exception as e:
        logging.error(f"Error generating chapter: {str(e)}")
        raise

def generate_and_combine_image(chapter, book_folder, book_id):
    try:
        free_image_gen.generate_context_image(book_folder=book_folder, book_id=book_id, chapter_content=chapter, image_filename="chapter_image.jpg")
        combine = combine_text_and_images.join_into_docx_format(text=chapter, image_path=f"{book_folder}/{book_id}/chapter_image.jpg", book_folder=f"{book_folder}/{book_id}")
        combine.add_text()
        combine.add_image()
        combine.save_doc()
        logging.info("Image generated and combined with text successfully.")
        print(f"Generated image: {book_folder}/{book_id}/chapter_image.jpg")
    except Exception as e:
        logging.error(f"Error generating or combining image: {str(e)}")
        raise

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    prompt = "write a short story about AGI and the future of humanity"

    print("Generating chapter...")
    chapter = generate_chapter(prompt)

    print("Generating and combining image...")
    generate_and_combine_image(chapter, all_book_folder, book_id)

    print("Book generation completed.")

if __name__ == "__main__":
    main()