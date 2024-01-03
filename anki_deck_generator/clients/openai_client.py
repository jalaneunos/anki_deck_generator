from openai import OpenAI
from anki_deck_generator.models.openai_function_calling import format_question_and_answer


class OpenAIClient:
    def __init__(self, api_key: str) -> None:
        self.client = OpenAI(api_key=api_key)

    def chat_completion(self, model: str, messsages) -> str:
        response = self.client.chat.completions.create(
            messages=messsages,
            model=model,
            max_tokens=1024,
            tools=[format_question_and_answer],
            tool_choice={"type": "function", "function": {"name": format_question_and_answer["function"]["name"]}}
        )
        return response
