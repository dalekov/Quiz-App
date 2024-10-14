from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.root = Tk()
        self.root.title("Quizzler")
        self.root.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="#F9E79F", font=("Courier", 40, "bold"))
        self.score_label.grid(row=0, column=0, columnspan=2)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Question here...",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        img_btn_correct = PhotoImage(file="images/true.png")
        img_btn_wrong = PhotoImage(file="images/false.png")

        self.true_button = Button(image=img_btn_correct, highlightthickness=0, command=self.true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=img_btn_wrong, highlightthickness=0, command=self.true)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.score_label.config(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="#F9E79F")
        self.root.after(1000, self.get_next_question)
