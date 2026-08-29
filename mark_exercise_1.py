from jupyprint import jupyprint
import numpy as np

### CHECKS
def check_answer_1(dir_from_notebook, 
                   return_mark=False):
    assert "answer_1" in dir_from_notebook, "Variable `answer_1` does not exist!"

    if return_mark == False:
        jupyprint("*Checks passed for question 1!*")

    if return_mark:
        return 1

def check_answer_2(double,                    
                   return_mark=False):
    assert double(4) == 8
    assert double(100) == 200

    if return_mark == False:
        jupyprint("*Checks passed for question 2!*")

    if return_mark:
        return 1

### MARKING
def mark_all(answer_1, answer_2):
    marks= np.sum([answer_1==100,
                    check_answer_2(answer_2, return_mark=True)])

    return jupyprint(f"{marks} marks were obtained.")