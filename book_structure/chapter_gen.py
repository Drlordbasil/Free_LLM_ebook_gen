from api_requests.local_LLM_api import mistral_chat

class Generate_chapters_dynamically:
    def __init__(self, prompt, system_prompt="You are an amazing author", user_prompt=None):
        self.prompt = prompt
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt or self.prompt
        self.client = mistral_chat(system=self.system_prompt, user=self.user_prompt)

    def generate_chapters(self):
        try:
            chapter = self.client.genarate_response()
            print(f"Generated chapter: {chapter}")
            return chapter
        except Exception as e:
            print(f"Error generating chapter: {str(e)}")
            raise