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
        user_answer = input(f"Q.{self.question_number + 1} : {current_question.question_text}\nA:{answers[0]}\nB:{answers[1]}\nC:{answers[2]}\nD:{answers[3]}\nYour answer (A-B-C-D):").lower()
        if user_answer == "a":
            user_answer = answers[0]
        elif user_answer == "b":
            user_answer = answers[1]
        elif user_answer == "c":
            user_answer = answers[2]
        elif user_answer == "d":
            user_answer = answers[3]
        else:
            user_answer

        self.check_answer(user_answer, current_question.correct_answer)


    

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That is wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Tour current score is : {self.score}/{self.question_number}")