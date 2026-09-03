from jupyprint import jupyprint
from marking_sub_functions import soft_assert, sub_check, award_marks, pre_define_blanks_ans
from mk_var import mk_var
import numpy as np

# SET TOTAL MARKS FOR EXERCISE
total_marks = 5

def pre_define_blanks(n_ans):
    return  pre_define_blanks_ans(n_ans)

### FUNCTIONS TO MARK EACH QUESTION

# TEMPLATE:
# def check_answer_X(answer_X, 
#                    return_mark=False):
#     question_name = "Question X"
#     answer_name = "answer_X"
#     marks_available = 1
#     conditions = np.array([soft_assert(<condition>,
#                               f"Your answer to {question_name} is not correct! `{answer_name}` is the wrong number!",
#                                 return_mark=return_mark)])
#     mark = sub_check(question_name, 
#                      conditions,
#                      return_mark=return_mark)
#     return award_marks(mark, marks_available=marks_available)

def check_answer_1(answer_1, 
                   return_mark=False):
    question_name = "Question 1"
    answer_name = "answer_1"
    marks_available = 1
    conditions = np.array([soft_assert(np.isclose(answer_1, 100 ** 2),
                              f"Your answer to {question_name} is not correct! `{answer_name}` is the wrong number!",
                                return_mark=return_mark)])
    mark = sub_check(question_name, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)

def check_answer_2(answer_2, 
                   return_mark=False):
    question_name = "Question 2"
    answer_name = "answer_2"
    marks_available = 1
    conditions = np.array([soft_assert(np.isclose(answer_2, 8 * 4 / 2),
                              f"Your answer to {question_name} is not correct! `{answer_name}` is the wrong number!",
                                return_mark=return_mark)])
    mark = sub_check(question_name, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)

def check_answer_3(answer_3, 
                   return_mark=False):
    question_name = "Question 3"
    answer_name = "answer_3"
    marks_available = 1
    conditions = np.array([soft_assert(np.isclose(answer_3, 2 ** 2 * (4 + 6)),
                              f"Your answer to {question_name} is not correct! `{answer_name}` is the wrong number!",
                                return_mark=return_mark)])
    mark = sub_check(question_name, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)

def check_answer_4(answer_4, 
                   return_mark=False):
    question_name = "Question 4"
    answer_name = "answer_4"
    marks_available = 1
    conditions = np.array([soft_assert(np.isclose(answer_4, (8 - 6) * 2 + 24),
                              f"Your answer to {question_name} is not correct! `{answer_name}` is the wrong number!",
                                return_mark=return_mark)])
    mark = sub_check(question_name, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)

def check_answer_5(answer_5, 
                   return_mark=False):
    question_name = "Question 5"
    answer_name = "answer_5"
    marks_available = 1
    conditions = np.array([soft_assert(np.isclose(answer_5, 9 * 4 + 8 / (2 - 3)),
                              f"Your answer to {question_name} is not correct! `{answer_name}` is the wrong number!",
                                return_mark=return_mark)])
    mark = sub_check(question_name, 
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
             return_mark=True,
             test_all=False):
    
    if test_all==True:
        usr_k = input()
        if usr_k == mk_var():
            # Utility answers for testing within exercise notebook
            jupyprint(np.array([    
                    answer_1 :=  100 ** 2,
                    answer_2 :=  8 * 4 / 2,
                    answer_3 := 2 ** 2 * (4 + 6),
                    answer_4 := (8 - 6) * 2 + 24,
                    answer_5 := 9 * 4 + 8 / (2 - 3)]))
            
    marks= np.sum([check_answer_1(answer_1, return_mark=return_mark),
                  check_answer_2(answer_2, return_mark=return_mark),
                  check_answer_3(answer_3, return_mark=return_mark),
                  check_answer_4(answer_4, return_mark=return_mark),
                  check_answer_5(answer_5, return_mark=return_mark)
                  ])
    return jupyprint(f"# You got {marks}/{total_marks} marks.")