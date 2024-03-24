from openai import OpenAI
from config import base_url, api_key, model


class mistral_chat(OpenAI):
    def __init__(self, base_url=base_url, api_key=api_key,model=model,system="",user=""):
        self.base_url = base_url
        self.api_key = api_key
        self.model = model
        self.system = system
        self.user = user

        self.client = OpenAI(
            base_url = base_url,
            api_key=api_key, # required, but unused
        )
        self.model = model
    def genarate_response(self):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system},
                {"role": "user", "content": self.user},
            ]
            )
        return response.choices[0].message.content

