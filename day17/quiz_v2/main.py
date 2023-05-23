from question import Question
from quiz import Quiz
from data import questions



questions_bank = []

for q in questions:
    question = Question(q_text=q["question"], c_answer=q["correct_answer"], w_answers=q["incorrect_answers"])
    questions_bank.append(question)

new_quiz = Quiz(questions_bank)

new_quiz.get_question()