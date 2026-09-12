# Interactice scientific notation exercise
from jupyprint import jupyprint
import numpy as np
from time import sleep

def test_me(n_iter=10):
    score_arr = np.array([]).astype('float')
    for rep in np.arange(n_iter):
        jupyprint(f'## Question {rep+1}')
        random_big_or_small = np.random.normal(0, 60000)
        jupyprint(f"Here is a number in scientific notation: {random_big_or_small:e}")
        jupyprint(f"Type this number WITHOUT scientific notation.")
        jupyprint("*Note*: you must type a number, not text, or you will get an error.")
        sleep(1)
        usr_input = float(input())
        if np.isclose(usr_input, random_big_or_small):
            score_arr = np.append(score_arr, 1)
            jupyprint(f"That is **correct**! Well done! {usr_input} is the same value as {random_big_or_small:e}.")
        else:
            jupyprint(f"That is **NOT correct**! {usr_input} is NOT the same value as {random_big_or_small:e}.")
            score_arr = np.append(score_arr, 0.0)
    jupyprint(f"## You got {int(score_arr.sum())} out of {n_iter} marks!")