from jupyprint import jupyprint
from marking_sub_functions import soft_assert, sub_check, award_marks, pre_define_blanks_ans, mk_new_q_marking
from util import *
from mk_var import mk_var
import numpy as np

number = "r2ta"[1::2]
for name in list(globals()):
    if name.startswith("mk_t_"):
        continue
    if callable(globals()[name]) and not name.endswith(f"{number}"):
        del globals()[name]

# SET TOTAL MARKS FOR EXERCISE
total_marks = 9

def pre_define_blanks(n_ans):
    return  pre_define_blanks_ans(n_ans)
obs_1, obs_2, obs_3, obs_4 = mk_t_2a()

### FUNCTIONS TO MARK EACH QUESTION
# Use `mk_new_q_marking()` in IPython to generate marking function template.

def check_answer_1(answer_1, 
                   return_mark=False):
    question_name = "Question 1"
    answer_name = "answer_1"
    marks_available = 1
    conditions = np.array([soft_assert(answer_1 in ["a", "b", "c"],
                              f"{question_name} is not correct! `{answer_name}`  should be `'a'`, `'b'`or `'c'`. Make sure you did not forget to use quotation marks! `'`",
                                return_mark=return_mark),
                            soft_assert(answer_1 == obs_2,
                              f"{question_name} is not correct! `{answer_name}` is the wrong answer.",
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
    conditions = np.array([soft_assert(answer_2 in ["a", "b", "c"],
                              f"{question_name} is not correct! `{answer_name}`  should be `'a'`, `'b'`or `'c'`. Make sure you did not forget to use quotation marks! `'`",
                                return_mark=return_mark),
                            soft_assert(answer_2 == obs_3,
                              f"{question_name} is not correct! `{answer_name}` is the wrong answer.",
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
    conditions = np.array([soft_assert(answer_3 in ["a", "b", "c", "d"],
                              f"{question_name} is not correct! `{answer_name}`  should be `'a'`, `'b'`, `'c'` or `'d'`. Make sure you did not forget to use quotation marks! `'`",
                                return_mark=return_mark),
                            soft_assert(answer_3 == obs_1,
                              f"{question_name} is not correct! `{answer_name}` is the wrong answer.",
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
    conditions = np.array([soft_assert(answer_4 in ["a", "b", "c", "d"],
                              f"{question_name} is not correct! `{answer_name}`  should be `'a'`, `'b'`, `'c'` or `'d'`. Make sure you did not forget to use quotation marks! `'`",
                                return_mark=return_mark),
                            soft_assert(answer_4 == obs_3,
                              f"{question_name} is not correct! `{answer_name}` is the wrong answer.",
                                return_mark=return_mark)])
    mark = sub_check(question_name, answer_4, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)

def check_answer_5(answer_5, 
                   return_mark=False):
    question_name = "Question 5"
    answer_name = "answer_5"
    marks_available = 1
    conditions = np.array([soft_assert(answer_5 in ["a", "b", "c", "d"],
                              f"{question_name} is not correct! `{answer_name}`  should be `'a'`, `'b'`, `'c'` or `'d'`. Make sure you did not forget to use quotation marks! `'`",
                                return_mark=return_mark),
                            soft_assert(answer_5 == obs_4,
                              f"{question_name} is not correct! `{answer_name}` is the wrong answer.",
                                return_mark=return_mark)])
    mark = sub_check(question_name, answer_5, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)

def check_answer_6(answer_6, 
                   return_mark=False):
    question_name = "Question 6"
    answer_name = "answer_6"
    marks_available = 1
    conditions = np.array([soft_assert(answer_6 in ["a", "b", "c", "d"],
                              f"{question_name} is not correct! `{answer_name}`  should be `'a'`, `'b'`, `'c'` or `'d'`. Make sure you did not forget to use quotation marks! `'`",
                                return_mark=return_mark),
                            soft_assert(answer_6 == obs_4,
                              f"{question_name} is not correct! `{answer_name}` is the wrong answer.",
                                return_mark=return_mark)])
    mark = sub_check(question_name, answer_6, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)

def check_answer_7(answer_7, 
                   return_mark=False):
    question_name = "Question 7"
    answer_name = "answer_7"
    marks_available = 1
    conditions = np.array([soft_assert(answer_7 in ["a", "b", "c", "d"],
                              f"{question_name} is not correct! `{answer_name}`  should be `'a'`, `'b'`, `'c'` or `'d'`. Make sure you did not forget to use quotation marks! `'`",
                                return_mark=return_mark),
                            soft_assert(answer_7 == obs_3,
                              f"{question_name} is not correct! `{answer_name}` is the wrong answer.",
                                return_mark=return_mark)])
    mark = sub_check(question_name, answer_7, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)

def check_answer_8(answer_8, 
                   return_mark=False):
    question_name = "Question 8"
    answer_name = "answer_8"
    marks_available = 1
    conditions = np.array([soft_assert(answer_8 in ["a", "b", "c", "d"],
                              f"{question_name} is not correct! `{answer_name}`  should be `'a'`, `'b'`, `'c'` or `'d'`. Make sure you did not forget to use quotation marks! `'`",
                                return_mark=return_mark),
                            soft_assert(answer_8 == obs_2,
                              f"{question_name} is not correct! `{answer_name}` is the wrong answer.",
                                return_mark=return_mark)])
    mark = sub_check(question_name, answer_8, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)

def check_answer_9(answer_9, 
                   return_mark=False):
    question_name = "Question 9"
    answer_name = "answer_9"
    marks_available = 1
    conditions = np.array([soft_assert(answer_9 in ["a", "b", "c", "d"],
                              f"{question_name} is not correct! `{answer_name}`  should be `'a'`, `'b'`, `'c'` or `'d'`. Make sure you did not forget to use quotation marks! `'`",
                                return_mark=return_mark),
                            soft_assert(answer_9 == obs_3,
                              f"{question_name} is not correct! `{answer_name}` is the wrong answer.",
                                return_mark=return_mark)])
    mark = sub_check(question_name, answer_9, 
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
             answer_7,
             answer_8,
             answer_9,
             return_mark=True,
             test_all=False):
    
    if test_all==True:
        usr_k = input()
        if usr_k == mk_var():
            # Utility answers for testing within exercise notebook
            jupyprint(np.array([    
                    answer_1 := obs_2,
                    answer_2 := obs_3,
                    answer_3 := obs_1,
                    answer_4 := obs_3,
                    answer_5 := obs_4,
                    answer_6 := obs_4,
                    answer_7 := obs_3,
                    answer_8 := obs_2,
                    answer_9 := obs_3]))
            
    marks= np.sum([check_answer_1(answer_1, return_mark=return_mark),
                  check_answer_2(answer_2, return_mark=return_mark),
                  check_answer_3(answer_3, return_mark=return_mark),
                  check_answer_4(answer_4, return_mark=return_mark),
                  check_answer_5(answer_5, return_mark=return_mark),
                  check_answer_6(answer_6, return_mark=return_mark),
                  check_answer_7(answer_7, return_mark=return_mark),
                  check_answer_8(answer_8, return_mark=return_mark),
                  check_answer_9(answer_9, return_mark=return_mark)
                  ])
    return jupyprint(f"# You got {marks}/{total_marks} marks.")