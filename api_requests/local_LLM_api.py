from openai import OpenAI
from config import base_url, api_key, model

class mistral_chat(OpenAI):
    def __init__(self, base_url=base_url, api_key=api_key, model=model, system="", user=""):
        self.base_url = base_url
        self.api_key = api_key
        self.model = model
        self.system = system
        self.user = user

        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key,  # required, but unused
        )
        self.model = model

    def generate_response(self, chapter_prompt):
        response = self.client.chat.completions.create(
            model=self.model,
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
                 story where you left off:
                 '''
                 In the year 2045, the world is a bleak place. The only escape is the OASIS, a virtual reality universe created by the enigmatic James Halliday. When Halliday dies, he leaves behind a series of puzzles that lead to an Easter egg hidden within the OASIS. The first chapter follows the protagonist, Wade Watts, as he embarks on a quest to find the egg and win the ultimate prize. Along the way, he encounters other gunters (egg hunters), as well as the sinister IOI corporation, which seeks to control the OASIS for its own gain.
                 '''
                 """},
                {"role": "assistant", "content": """
                    Wade Watts is a high school student living in the Stacks, a poverty-stricken neighborhood in Columbus, Ohio. He spends his days attending school in the OASIS and his nights searching for clues to the first puzzle. When he finally solves it, he becomes an instant celebrity and a target for the IOI. With the help of his friends Aech and Art3mis, Wade must navigate the dangers of the OASIS and the real world to find the egg before it falls into the wrong hands.
                 """},
                {"role": "user", "content": """
                    begin the next chapter of the book, here is the entire book so far:
                 
                    '''
                 title: Ready Player One
                    chapter 1:
                    In the year 2045, the world is a bleak place. The only escape is the OASIS, a virtual reality universe created by the enigmatic James Halliday. When Halliday dies, he leaves behind a series of puzzles that lead to an Easter egg hidden within the OASIS. The first chapter follows the protagonist, Wade Watts, as he embarks on a quest to find the egg and win the ultimate prize. Along the way, he encounters other gunters (egg hunters), as well as the sinister IOI corporation, which seeks to control the OASIS for its own gain. 
                 wade watts is a high school student living in the stacks, a poverty-stricken neighborhood in columbus, ohio. he spends his days attending school in the oasis and his nights searching for clues to the first puzzle. when he finally solves it, he becomes an instant celebrity and a target for the ioi. with the help of his friends aech and art3mis, wade must navigate the dangers of the oasis and the real world to find the egg before it falls into the wrong hands.


                 """
                },
                {"role": "assistant", "content": """
                    
                    Wade and his friends Aech and Art3mis continue their quest to find the egg. They travel to the planet Ludus, where they must complete a series of challenges to unlock the next clue. Along the way, they"""},

                {"role": "user", "content": self.user},
                {"role": "user", "content": chapter_prompt},
            ]
        )
        return response.choices[0].message.content