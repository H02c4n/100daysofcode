import random

class Quiz:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list



    def get_question(self):
        current_question = self.question_list[self.question_number]
        answers = current_question.wrong_answers
        answers.append(current_question.correct_answer)
        random.shuffle(answers)
        input(f"Q.{self.question_number + 1} : {current_question.question_text}\nA:{answers[0]}\nB:{answers[1]}\nC:{answers[2]}\nD:{answers[3]}\n(Your answer A-B-C-D)")