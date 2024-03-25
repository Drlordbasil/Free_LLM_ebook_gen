from api_requests.local_LLM_api import MistralChat

class Generate_chapters_dynamically:
    def __init__(self, prompt, num_chapters, system_prompt=None, user_prompt=None, previous_chapters=None):
        self.prompt = prompt
        self.num_chapters = num_chapters
        self.system_prompt = system_prompt or "You are an amazing author that uses complex story mechanics and uses them as mirroring problems of day-to-day life for normal people."
        self.user_prompt = user_prompt or self.prompt
        self.previous_chapters = previous_chapters or []
        self.client = MistralChat(system=self.system_prompt, user=self.user_prompt)
        self.chapters = []
        self.extension_count = {i: 0 for i in range(1, num_chapters + 1)}
    def clean_chapters(self):
        if "<api_requests.local_LLM_api.mistral_chat>" in self.chapters:
            self.chapters.remove("<api_requests.local_LLM_api.mistral_chat>")
        return self.chapters
    def generate_chapters(self):
        for i in range(self.num_chapters):
            try:
                chapter_prompt = f"Generate chapter {i+1} of the story. Ensure it maintains contextual coherence with the previous chapters: {' '.join(self.previous_chapters)}"
                chapter = self.client.generate_response(chapter_prompt)
                print(f"Generated chapter {i+1} successfully.")
                self.chapters.append(chapter)
                self.previous_chapters.append(chapter)
            except Exception as e:
                print(f"Error generating chapter {i+1}: {str(e)}")
                raise
        print(f"All {self.num_chapters} chapters generated successfully.")
        return self.chapters

    def extend_chapter(self, chapter_index):
        if chapter_index < 1 or chapter_index > self.num_chapters:
            print(f"Invalid chapter index: {chapter_index}. Chapter index must be between 1 and {self.num_chapters}.")
            return
        if self.extension_count[chapter_index] >= 3:
            print(f"Extension limit reached for chapter {chapter_index}. Maximum of 3 extensions allowed per chapter.")
            return

        try:
            current_content = self.chapters[chapter_index - 1]
            extension_prompt = f"Continue the story from: {current_content}"
            extension = self.client.generate_response(extension_prompt)
            print(f"Extended chapter {chapter_index} successfully.")
            self.chapters[chapter_index - 1] += extension
            self.extension_count[chapter_index] += 1
        except Exception as e:
            print(f"Error extending chapter {chapter_index}: {str(e)}")
            raise