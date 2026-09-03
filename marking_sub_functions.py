from jupyprint import jupyprint
import numpy as np

# FUNCTIONS TO USE WITHIN QUESTION SPECIFIC FUNCTIONS
def pre_define_blanks_ans(n_ans):
    return np.repeat(-99999999999, n_ans)
                     
def soft_assert(condition, warning_text, return_mark=False):
    if (condition == False):
        jupyprint("*"+warning_text+"*")
    return condition # Bool as indicator of mark obtained.

def sub_check(question_number, conditions_array, return_mark):
    all_conditions_true = (conditions_array.sum() == len(conditions_array))
    if all_conditions_true:
        jupyprint(f"*Your answer to {question_number} is correct!*")
    if return_mark & all_conditions_true:
        return "got_mark"
    if return_mark & (all_conditions_true == False):
        return "did_not_get_mark"

def award_marks(mark, marks_available):
    if mark == "got_mark":
        return marks_available
    if mark == "did_not_get_mark":
        return 0