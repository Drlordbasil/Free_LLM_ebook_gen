import os
from gradio_client import Client
import time
from typing import Optional

client = Client("radames/Real-Time-Text-to-Image-SDXL-Lightning")

def generate_image(prompt: str, max_retries: int = 3, retry_delay: int = 2) -> Optional[str]:
    for attempt in range(max_retries):
        try:
            seed = client.predict(api_name="/get_random_value")
            response = client.predict(prompt, seed, api_name="/predict")
            return response
        except Exception as e:
            print(f"Error generating image (attempt {attempt + 1}): {str(e)}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
    
    print("Max retries reached. Skipping image generation.")
    return None

def save_image(image_path: str, target_folder: str, target_filename: str) -> Optional[str]:
    try:
        os.makedirs(target_folder, exist_ok=True)
        target_path = os.path.join(target_folder, target_filename)
        os.rename(image_path, target_path)
        print(f"Image saved as {target_path}")
        return target_path
    except Exception as e:
        print(f"Error saving image: {str(e)}")
        return None

def generate_cover_image(book_folder: str, title: str, max_retries: int = 3, retry_delay: int = 2) -> Optional[str]:
    prompt = f"Generate an engaging and visually appealing ebook cover for the title: {title}. The cover should capture the essence of the book and attract potential readers."
    image_path = generate_image(prompt, max_retries, retry_delay)
    
    if image_path:
        target_filename = f"{title}_cover.jpg"
        return save_image(image_path, book_folder, target_filename)
    
    return None

def generate_context_image(book_folder: str, chapter_content: str, image_filename: str, max_retries: int = 3, retry_delay: int = 2) -> Optional[str]:
    if len(chapter_content) > 500:
        chapter_content = f"{chapter_content[:500]}..."
    
    print("Retrying with a simplified prompt...")
    for attempt in range(max_retries):
        try:
            if attempt > 0:
                prompt = f"Create an image that represents the key elements or themes from the chapter content: {chapter_content}"
            else:
                prompt = f"Create a visually striking image that represents the key elements, themes, or a pivotal scene from the following chapter content:\n\n{chapter_content}\n\nEnsure the image enhances the reader's understanding and engagement with the story."
            
            image_path = generate_image(prompt)
            
            if image_path:
                return save_image(image_path, book_folder, image_filename)
        except Exception as e:
            print(f"Error generating context image (attempt {attempt + 1}): {str(e)}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
    
    print("Max retries reached. Skipping context image generation.")
    return None