from question import Question
from quiz import Quiz
from data import questions



questions_bank = []

for q in questions:
    question = Question(q_text=q["question"], c_answer=q["correct_answer"], w_answers=q["incorrect_answers"])
    questions_bank.append(question)

quiz = Quiz(questions_bank)


while quiz.still_has_questions:
    quiz.get_question()