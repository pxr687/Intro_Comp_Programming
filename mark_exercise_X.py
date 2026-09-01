from jupyprint import jupyprint
from marking_sub_functions import soft_assert, sub_check, award_marks, pre_define_blanks_ans
from mark_exercise_var import mk_var
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
#     marks_available = 1
#     QX_conditions = np.array([soft_assert(<condition>,
#                               f"{question_name} is not correct!",
#                                 return_mark=return_mark)])
#     mark = sub_check(question_name, 
#                      QX_conditions,
#                      return_mark=return_mark)
#     return award_marks(mark, marks_available=marks_available)


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
                    answer_1 := <ans>,
                    answer_2 := <ans>,
                    answer_3 := <ans>,
                    answer_4 := <ans>,
                    answer_5 := <ans>]))
            
    marks= np.sum([check_answer_1(answer_1, return_mark=return_mark),
                  check_answer_2(answer_2, return_mark=return_mark),
                  check_answer_3(answer_3, return_mark=return_mark),
                  check_answer_4(answer_4, return_mark=return_mark),
                  check_answer_5(answer_5, return_mark=return_mark)
                  ])
    return jupyprint(f"# You got {marks}/{total_marks} marks.")