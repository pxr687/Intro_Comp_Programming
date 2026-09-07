# Abridged version of script for specific exercise.
from notching_sub_functions import *
import numpy as np

def check_answer(student_answer,
                 correct_string, 
                question_name = "Question 1",
                answer_name = "answer_1",
                   return_mark=False,
                   correct_is_string=True):
    marks_available = 1
    if correct_is_string:
        warning = f'Your answer to Your answer to {question_name} is **NOT CORRECT!** `{answer_name}` should be `"{correct_string}"`. At the moment it is `{student_answer}`!'
    else:
        warning = f"Your answer to Your answer to {question_name} is **NOT CORRECT!** `{answer_name}` should be `{correct_string}`. At the moment it is `{student_answer}`!"
    conditions = np.array([soft_assert(student_answer == correct_string,
                              warning,
                                return_mark=return_mark)])
    mark = sub_check(question_name, student_answer, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)

def homer():
    return "'The Iliad' by Homer is an ancient Greek epic poem composed around the late 8th or early 7th century BC. Set during the final weeks of the ten-year Trojan War, it follows the devastating anger of Achilles, the greatest Greek warrior, sparked by a bitter quarrel with King Agamemnon. As pride and wrath collide, the conflict escalates from personal dispute to battlefield tragedy, culminating in the death of Troy's champion, Hector. Gods intervene, heroes clash, and the fate of nations hangs in the balance."