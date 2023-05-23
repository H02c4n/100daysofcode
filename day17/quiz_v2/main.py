from question import Question
from quiz import Quiz
from data import questions



question_bank = []

for q in questions:
    question = Question(q_text=q["question"], c_answer=q["correct_answer"], w_answers=q["incorrect_answers"])
    question_bank.append(question)

new_quiz = Quiz(question_bank)


while new_quiz.still_has_questions():
    new_quiz.get_question()

print("You hace completed the quiz")
print(f"Your final score was: {new_quiz.score}/{len(question_bank)}")