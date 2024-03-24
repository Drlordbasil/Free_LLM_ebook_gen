from api_requests.local_LLM_api import mistral_chat


class Generate_chapters_dynamically:
    def __init__(self, prompt):
        self.prompt = prompt
        self.client = mistral_chat(system="You are an amazing author",user=self.prompt)

    def generate_chapters(self):
        return self.client.genarate_response()
    
