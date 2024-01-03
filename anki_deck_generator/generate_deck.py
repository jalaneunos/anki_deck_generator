import logging
import os
from anki_deck_generator.read_input_file import convert_file_to_text
from anki_deck_generator.command_line_parser import CommandLineParser
from anki_deck_generator.openai_question_generator import OpenAIQuestionGenerator
from anki_deck_generator.genanki_deck_generator import generate_anki_deck
from openai import OpenAI

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_deck(input_file):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    file_content = convert_file_to_text(input_file)

    question_generator = OpenAIQuestionGenerator(openai_api_key)
    question_generator.add_file_content(file_content)
    questions_and_answers = question_generator.generate_questions()
    generate_anki_deck(questions_and_answers)
