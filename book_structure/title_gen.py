from api_requests.local_LLM_api import mistral_chat


def generate_title():
    title_prompt = "Generate a title for a new book. The title should be catchy and relevant to the content."
    title = mistral_chat(system="You are a talented author that generates titles of books that aren't too cheesy but still will grab someones attention.", user=title_prompt)
    return title