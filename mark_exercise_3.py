from jupyprint import jupyprint
from marking_sub_functions import *
from util import * 
from mk_var import mk_var
import numpy as np

# SET TOTAL MARKS FOR EXERCISE
total_marks = 6

number = 3
for name in list(globals()):
    if callable(globals()[name]) and name.startswith("mk_t_") and not name.endswith(f"{number}"):
        del globals()[name]

def pre_define_blanks(n_ans):
    return  pre_define_blanks_ans(n_ans)

### FUNCTIONS TO MARK EACH QUESTION
# Use `mk_new_q_marking()` in IPython to generate marking function template.

def check_answer_1(total, 
                   return_mark=False):
    question_name = "Question 1"
    answer_name = "total"
    marks_available = 1
    conditions = np.array([soft_assert(type(total) != str,
                              f"{question_name} is not correct! `{answer_name}` should be either `int` or `float` data type! `{answer_name}` is the `str` datatype at the moment. You will see a NASTY error below this message, because of this!",
                                return_mark=return_mark) ,
                            soft_assert(np.isclose(total, mk_t_3()[0].astype(float)),
                              f"{question_name} is not correct! `{answer_name}` is the wrong value!",
                                return_mark=return_mark)])
    mark = sub_check(question_name, total, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)


def check_answer_2(number_of_students, 
                   return_mark=False):
    question_name = "Question 2"
    answer_name = "number_of_students"
    marks_available = 1
    conditions = np.array([soft_assert(type(number_of_students) != str,
                              f"{question_name} is not correct! `{answer_name}` should be either `int` or `float` data type! `{answer_name}` is the `str` datatype at the moment. You will see a NASTY error below this message, because of this!",
                                return_mark=return_mark),
                            soft_assert(np.isclose(number_of_students, mk_t_3()[1].astype(float)),
                              f"{question_name} is not correct! `{answer_name}` is the wrong value!",
                                return_mark=return_mark)])
    mark = sub_check(question_name, number_of_students, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)


def check_answer_3(test_score, 
                   return_mark=False,
                   dir_from_notebook=dir()):
    question_name = "Question 3"
    answer_name = "test_score"
    marks_available = 1
    conditions = np.array([soft_assert(type(test_score) != str,
                              f"{question_name} is not correct! `{answer_name}` should be the `float` data type! `{answer_name}` is the `str` datatype at the moment. You will see a NASTY error below this message, because of this!",
                                return_mark=return_mark),
                            soft_assert(np.isclose(test_score, mk_t_3()[2].astype(float)),
                              f"{question_name} is not correct! `{answer_name}` is the wrong value!",
                                return_mark=return_mark)])
    mark = sub_check(question_name, test_score, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)


def check_answer_4(welcome_20, 
                   return_mark=False):
    question_name = "Question 4"
    answer_name = "welcome_20"
    marks_available = 1
    conditions = np.array([soft_assert(welcome_20 == mk_t_3()[3].astype(str),
                              f"{question_name} is not correct! `{answer_name}` is the wrong value! It should be the string: `{mk_t_3()[3]}`",
                                return_mark=return_mark)])
    mark = sub_check(question_name, welcome_20, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)


def check_answer_5(n_forms, 
                   return_mark=False):
    question_name = "Question 5"
    answer_name = "n_forms"
    marks_available = 1
    conditions = np.array([soft_assert(type(n_forms) != str,
                              f"{question_name} is not correct! `{answer_name}` should be `float` or `int` data type! `{answer_name}` is the `str` datatype at the moment. You will see a NASTY error below this message, because of this!",
                                return_mark=return_mark),
                            soft_assert(np.isclose(n_forms,mk_t_3()[4].astype(float)),
                              f"{question_name} is not correct! `{answer_name}` is the wrong value!",
                                return_mark=return_mark)])
    mark = sub_check(question_name, n_forms, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)


def check_answer_6(savings_after_six_months, 
                   return_mark=False):
    question_name = "Question 6"
    answer_name = "savings_after_six_months"
    marks_available = 1
    conditions = np.array([soft_assert(type(savings_after_six_months) == float,
                              f"{question_name} is not correct! `{answer_name}` should be a `float`",
                                return_mark=return_mark),
                            soft_assert(np.isclose(savings_after_six_months, mk_t_3()[5].astype(float)),
                              f"{question_name} is not correct! `{answer_name}` is the wrong value!",
                                return_mark=return_mark)])
    mark = sub_check(question_name, savings_after_six_months, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)

###############################################################################

### MARKING
def mark_all(answer_1, 
             answer_2, 
             answer_3,
             answer_4,
             answer_5,
             answer_6,
             return_mark=True,
             test_all=False):
    
    if test_all==True:
        usr_k = input()
        if usr_k == mk_var():
            # Utility answers for testing within exercise notebook
            jupyprint(np.array([    
                    answer_1 :=  mk_t_3()[0].astype(float),
                    answer_2 :=  mk_t_3()[1].astype(float),
                    answer_3 := mk_t_3()[2].astype(float),
                    answer_4 := mk_t_3()[3].astype(str),
                    answer_5 :=  mk_t_3()[4].astype(float),
                    answer_6 :=  mk_t_3()[5].astype(float)
                    ]))
            
    marks= np.sum([check_answer_1(answer_1, return_mark=return_mark),
                  check_answer_2(answer_2, return_mark=return_mark),
                  check_answer_3(answer_3, return_mark=return_mark),
                  check_answer_4(answer_4, return_mark=return_mark),
                  check_answer_5(answer_5, return_mark=return_mark),
                  check_answer_6(answer_6, return_mark=return_mark)
                  ])
    return jupyprint(f"# You got {marks}/{total_marks} marks.")