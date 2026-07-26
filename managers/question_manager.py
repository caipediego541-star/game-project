import json
import random


class QuestionManager:

    def __init__(self):

        self.questions = {}


    def load_questions(self, category):

        path = (
            f"data/questions/{category}.json"
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            self.questions[category] = json.load(file)


    def get_question(self, category):

        if category not in self.questions:
            self.load_questions(category)


        question = random.choice(
            self.questions[category]
        )

        return question