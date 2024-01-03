from anki_deck_generator.clients.openai_client import OpenAIClient
from anki_deck_generator.data.gpt_system_prompt import SYSTEM_PROMPT
import json


class OpenAIQuestionGenerator:
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        self.client = OpenAIClient(api_key)
        self.model = model
        self.messages = [
            {'role': 'system',
             'content': SYSTEM_PROMPT
             }]

    def add_file_content(self, file_content: str):
        self.messages.append({
            'role': 'user',
            'content': f"Convert the following content into flashcards with questions and answers using the provided function (delimited with XML tags) : <content>{file_content}</content>"
        })

    def generate_questions(self):
        response = self.client.chat_completion(self.model, self.messages)
        return json.loads(response.choices[0].message.tool_calls[0].function.arguments)
