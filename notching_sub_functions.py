from jupyprint import jupyprint
import numpy as np

# SIMPLE WORKFLOW FOR SIMPLE MARKING:
# Soft assert to use in-line in notebooks.
def inline_soft_assert(condition, warning_text):
    if (condition == False):
        jupyprint("*"+warning_text+"*")
    else:
        jupyprint("*That is **CORRECT**, well done!*")

# Put at end of erroring cells, when fixed, affirmation appeats!
def affirmation():
     jupyprint("*You have fixed the error! Well done! :-)*")

# FUNCTIONS TO USE WITHIN QUESTION SPECIFIC FUNCTIONS
def pre_define_blanks_ans(n_ans):
    return np.repeat(-99999999999, n_ans)
                     
def soft_assert(condition, warning_text, return_mark=False):
    if (condition == False):
        jupyprint("*"+warning_text+"*")
    return condition # Bool as indicator of mark obtained.

def sub_check(question_number, answer_var, conditions_array, return_mark):
    all_conditions_true = (conditions_array.sum() == len(conditions_array))
    if all_conditions_true:
        jupyprint(f"*Your answer to {question_number} is **CORRECT**! `{answer_var}` is the right answer!*")
    if return_mark & all_conditions_true:
        return "got_mark"
    if return_mark & (all_conditions_true == False):
        return "did_not_get_mark"

def award_marks(mark, marks_available):
    if mark == "got_mark":
        return marks_available
    if mark == "did_not_get_mark":
        return 0

################################################################################
# Generate a new marking function. Best used from IPython then output pasted into
# script.

# Example use:
# mk_new_q_marking([1, 2, 3, 4])

def mk_new_q_marking(qnum, question_name ="{question_name}", answer_name="{answer_name}"):

    for i in np.arange(len(qnum)):

        text = f"""
def check_answer_{qnum[i]}(answer_{qnum[i]}, 
                   return_mark=False):
    question_name = "Question {qnum[i]}"
    answer_name = "answer_{qnum[i]}"
    marks_available = 1
    conditions = np.array([soft_assert(<condition>,
                              f"Your answer to {question_name} is **NOT CORRECT!** `{answer_name}` is the wrong value!",
                                return_mark=return_mark)])
    mark = sub_check(question_name, answer_{qnum[i]}, 
                     conditions,
                     return_mark=return_mark)
    return award_marks(mark, marks_available=marks_available)
"""
        print(text)