import ollama

class MistralChat:
    def __init__(self, system="", user=""):
        self.system = system
        self.user = user

    def generate_response(self, chapter_prompt):
        response = ollama.chat(
            model='mistral',
            messages=[
                {"role": "system", "content": self.system},
                {"role": "user", "content": "generate a title for a novel"},
                {"role": "assistant", "content": "Ready Player One"},
                {"role": "user", "content": "generate the first chapter for the novel Ready Player One"},
                {"role": "assistant", "content": """
                 In the year 2045, the world is a bleak place. The only escape is the OASIS, a virtual reality universe created by the enigmatic James Halliday. When Halliday dies, he leaves behind a series of puzzles that lead to an Easter egg hidden within the OASIS. The first chapter follows the protagonist, Wade Watts, as he embarks on a quest to find the egg and win the ultimate prize. Along the way, he encounters other gunters (egg hunters), as well as the sinister IOI corporation, which seeks to control the OASIS for its own gain.
                 
                 """},
                {"role": "user", "content": """
                 continue generating the story where you left off:
                 '''
                 In the year 2045, the world is a bleak place. The only escape is the OASIS, a virtual reality universe created by the enigmatic James Halliday. When Halliday dies, he leaves behind a series of puzzles that lead to an Easter egg hidden within the OASIS. The first chapter follows the protagonist, Wade Watts, as he embarks on a quest to find the egg and win the ultimate prize. Along the way, he encounters other gunters (egg hunters), as well as the sinister IOI corporation, which seeks to control the OASIS for its own gain.
                 
                 """},
                {"role": "user", "content": self.user},
                {"role": "user", "content": chapter_prompt},
            ]
        )
        return response['message']['content']


