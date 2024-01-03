format_question_and_answer = {
    "type": "function",
    "function": {
        "name": "format_question_and_answer",
        "description": "Takes an array of questions and answers and creates objects",
        "parameters": {
            "type": "object",
            "properties": {
                "questions_and_answers": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "description": "object containing the question and its corresponding answer",
                        "properties": {
                            "question": {
                                "type": "string",
                                "description": "the question"
                            },
                            "answer": {
                                "type": "string",
                                "description": "the answer"
                            }
                        }
                    }
                }
            },
            "required": [
                'questions_and_answers'
            ]
        }
    }
}
