from api_requests.local_LLM_api import mistral_chat

class Generate_chapters_dynamically:
    def __init__(self, prompt, num_chapters, system_prompt="You are an amazing author", user_prompt=None):
        self.prompt = prompt
        self.num_chapters = num_chapters
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt or self.prompt
        self.client = mistral_chat(system=self.system_prompt, user=self.user_prompt)

    def generate_chapters(self):
        chapters = []
        for i in range(self.num_chapters):
            try:
                chapter_prompt = f"Generate chapter {i+1} of the story. Ensure it maintains contextual coherence with the previous chapters."
                chapter = self.client.genarate_response(chapter_prompt)
                print(f"Generated chapter {i+1}: {chapter}")
                chapters.append(chapter)
            except Exception as e:
                print(f"Error generating chapter {i+1}: {str(e)}")
                raise
        return chapters