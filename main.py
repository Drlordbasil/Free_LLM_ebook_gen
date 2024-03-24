from book_structure import chapter_gen
from api_requests import free_image_gen
from book_structure import combine_text_and_images

def main():
    # Create a new chapter generator
    prompt = "write a short story about AGI and the future of humanity"
    chapter_generator = chapter_gen.Generate_chapters_dynamically(prompt)
    
    chapter = chapter_generator.generate_chapters()
    free_image_gen.generate_context_image(book_folder="output_ebooks", chapter_content=chapter, image_filename="chapter_image.jpg")
    combine = combine_text_and_images.join_into_docx_format(text=chapter, image_path="output_ebooks/chapter_image.jpg", book_folder="output_ebooks")
    combine.add_text()
    combine.add_image()
    combine.save_doc()
    
if __name__ == "__main__":
    main()
