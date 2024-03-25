from api_requests.local_LLM_api import mistral_chat

class Generate_chapters_dynamically:
    def __init__(self, prompt, num_chapters, system_prompt="You are an amazing author that uses complex story mechanics and uses them as mirroring problems of day to day life for normal people.", user_prompt=None):
        self.prompt = prompt
        self.num_chapters = num_chapters
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt or self.prompt
        self.client = mistral_chat(system=self.system_prompt, user=self.user_prompt)
        self.chapters = []
        # Initialize a dictionary to track extensions for each chapter
        self.extension_count = {i: 0 for i in range(1, num_chapters + 1)}

    def generate_chapters(self):
        for i in range(self.num_chapters):
            try:
                chapter_prompt = f"Generate chapter {i+1} of the story. Ensure it maintains contextual coherence with the previous chapters."
                chapter = self.client.generate_response(chapter_prompt)
                print(f"Generated chapter {i+1}: {chapter}")
                self.chapters.append(chapter)
            except Exception as e:
                print(f"Error generating chapter {i+1}: {str(e)}")
                raise
        return self.chapters

    def extend_chapter(self, chapter_index):
        if chapter_index < 1 or chapter_index > self.num_chapters or self.extension_count[chapter_index] >= 3:
            print("Invalid chapter index or extension limit reached")
            return
        
        try:
            current_content = self.chapters[chapter_index - 1]
            extension_prompt = f"Continue the story from: {current_content}"  # Use the last 250 characters as context
            
            extension = self.client.generate_response(extension_prompt)
            print(f"Extended chapter {chapter_index}: {extension}")
            
            self.chapters[chapter_index - 1] += extension
            self.extension_count[chapter_index] += 1
        except Exception as e:
            print(f"Error extending chapter {chapter_index}: {str(e)}")
            raise
