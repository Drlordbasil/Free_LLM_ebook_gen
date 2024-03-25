from api_requests.local_LLM_api import MistralChat
import re

def generate_title(book_premise):
    title_prompt = f"Generate a catchy and engaging title for a book about {book_premise}"
    title_response = MistralChat(system="You are a talented author that generates compelling titles that grab readers' attention.", user=title_prompt)

    # Check if the response is a string
    if isinstance(title_response, str):
        title = title_response
    else:
        # Handle cases where the response is not a string
        title = str(title_response)

    # Remove any leading/trailing quotes or line breaks
    title = re.sub(r'^"|"$|^\'|\'$', '', title)
    title = title.strip()

    return title