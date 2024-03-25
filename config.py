import time

base_url = 'http://localhost:11434/v1'
api_key = 'ollama'
model = "mistral"
all_book_folder = "output_ebooks"
book_id = str(int(time.time()))  # Generate a unique book_id based on the current timestamp