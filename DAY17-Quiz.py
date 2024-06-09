#this code contains differect classes and their objects.
#visit :https://replit.com/@devmoh04/quiz-game-final#question_model.py for question class
#visit: https://replit.com/@devmoh04/quiz-game-final#quiz_brain.py for other question related methods
#visit: https://replit.com/@devmoh04/quiz-game-final#data.py for quiz questions.
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
print("Welcome to the QUIZ!!")

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
