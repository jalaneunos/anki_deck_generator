import genanki
import random

DECK_ID = 69435063
MODEL_ID = 1851015


def generate_anki_deck(questions_content):
    deck = genanki.Deck(DECK_ID, 'my_deck')
    model = genanki.Model(MODEL_ID, 'my_simple_model',
                          fields=[
                              {'name': 'Question'},
                              {'name': 'Answer'},
                          ],
                          templates=[
                              {
                                  'name': 'Card 1',
                                  'qfmt': '{{Question}}',
                                  'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
                              },
                          ])

    for question_and_answer in questions_content['questions_and_answers']:
        new_note = genanki.Note(
            model,
            fields=[question_and_answer['question'], question_and_answer['answer']]
        )
        deck.add_note(new_note)

    genanki.Package(deck).write_to_file('output.apkg')
