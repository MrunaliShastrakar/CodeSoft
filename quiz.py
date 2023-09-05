class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        for idx, question in enumerate(self.questions, start=1):
            print(f"Question {idx}: {question.question}")
            for i, option in enumerate(question.options, start=1):
                print(f"{i}. {option}")
            answer = int(input("Your answer (enter the option number): "))
            if answer == question.correct_answer:
                self.score += 1
                print("Correct!\n")
            else:
                print(f"Wrong! The correct answer is {question.correct_answer}: {question.options[question.correct_answer - 1]}\n")
        print(f"Quiz completed! Your score is: {self.score}/{len(self.questions)}")

# Define your questions here
question1 = Question("What is the capital of France?", ["Paris", "Berlin", "Madrid", "Rome"], 1)
question2 = Question("Which planet is known as the Red Planet?", ["Mars", "Jupiter", "Venus", "Saturn"], 1)
question3 = Question("What is the largest mammal?", ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"], 3)

# Create a list of questions
questions = [question1, question2, question3]

# Create a Quiz instance and run the quiz
quiz = Quiz(questions)
quiz.run()
