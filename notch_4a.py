from jupyprint import jupyprint
from notching_sub_functions import *
from util import * 
from mk_var import mk_var
import numpy as np

# SET TOTAL MARKS FOR EXERCISE
total_marks = 5

number = X
for name in list(globals()):
    if callable(globals()[name]) and name.startswith("mk_t_") and not name.endswith(f"{number}"):
        del globals()[name]

def pre_define_blanks(n_ans):
    return  pre_define_blanks_ans(n_ans)


def check_answer_1(answer_1, 
                   return_mark=False):
    question_name = "Question 1"
    answer_name = "answer_1"
    marks_available = 1
    conditions = np.array([soft_assert(<condition>,
                              f"Your answer to {question_name} is **NOT CORRECT!** `{answer_name}` is the wrong value!",
                                return_mark=return_mark)])
    mark = sub_check(question_name, answer_1, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)


def check_answer_2(answer_2, 
                   return_mark=False):
    question_name = "Question 2"
    answer_name = "answer_2"
    marks_available = 1
    conditions = np.array([soft_assert(<condition>,
                              f"Your answer to {question_name} is **NOT CORRECT!** `{answer_name}` is the wrong value!",
                                return_mark=return_mark)])
    mark = sub_check(question_name, answer_2, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)


def check_answer_3(answer_3, 
                   return_mark=False):
    question_name = "Question 3"
    answer_name = "answer_3"
    marks_available = 1
    conditions = np.array([soft_assert(<condition>,
                              f"Your answer to {question_name} is **NOT CORRECT!** `{answer_name}` is the wrong value!",
                                return_mark=return_mark)])
    mark = sub_check(question_name, answer_3, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)


def check_answer_4(answer_4, 
                   return_mark=False):
    question_name = "Question 4"
    answer_name = "answer_4"
    marks_available = 1
    conditions = np.array([soft_assert(<condition>,
                              f"Your answer to {question_name} is **NOT CORRECT!** `{answer_name}` is the wrong value!",
                                return_mark=return_mark)])
    mark = sub_check(question_name, answer_4, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)

###############################################################################

### MARKING
def mark_all(answer_1, 
             answer_2, 
             answer_3,
             answer_4,
             return_mark=True,
             test_all=False):
    
    if test_all==True:
        usr_k = input()
        if usr_k == mk_var():
            # Utility answers for testing within exercise notebook
            jupyprint(np.array([    
                    answer_1 := -999,
                    answer_2 := -999,
                    answer_3 := -999,
                    answer_4 := -999]))
            
    marks= np.sum([check_answer_1(answer_1, return_mark=return_mark),
                  check_answer_2(answer_2, return_mark=return_mark),
                  check_answer_3(answer_3, return_mark=return_mark),
                  check_answer_4(answer_4, return_mark=return_mark)
                  ])
    return jupyprint(f"# You got {marks}/{total_marks} marks.")