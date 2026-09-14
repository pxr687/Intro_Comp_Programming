from jupyprint import jupyprint
from time import sleep
import numpy as np
import random
import string

# Interactice revision of literals, expressions, functions.
def lit_exp_or_func():

    legal_answers = ["number literal", "text literal", "expression made from two literals", "function"]

    for i in np.arange(10):
        four_flip = np.random.choice([1, 2, 3, 4])
        correct = legal_answers[four_flip-1]
        if four_flip == 1:
            number_literal = int(np.random.normal(10, 3))
            output = number_literal
            article = "a"
        elif four_flip == 2:
            text_literal =  "".join(random.choices(string.ascii_letters + string.digits, k=int(np.random.uniform(1, 10))))
            output = f"'{text_literal}'"
            article = "a"
        elif four_flip == 3:
            two_flip = np.random.choice([1, 2])
            if two_flip == 1:
                number_literal_1 = int(np.random.normal(10, 3))
                number_literal_2 = int(np.random.normal(10, 3))
                op = np.random.choice(['+', '-', '*', '/'])
                random_exp = f"{number_literal_1} {op} {number_literal_2}"
                output = random_exp
                article = "an"
            if two_flip == 2:
                text_literal_1 =  "".join(random.choices(string.ascii_letters + string.digits, k=int(np.random.uniform(1, 10))))
                text_literal_2 =  "".join(random.choices(string.ascii_letters + string.digits, k=int(np.random.uniform(1, 10))))
                op = np.random.choice(['+'])
                random_exp = f"'{text_literal_1}' {op} '{text_literal_2}'"
                output = random_exp
                article = "an"
        else:
            func = np.random.choice(["`print()`", "`help()`" , "`abs()`", "`round()`"])
            output = func
            article = "a"

        jupyprint(f"## Question {i + 1}")
        jupyprint(f"What Python element is this?: `{output}`")
        passed = False
        while passed == False:
            jupyprint(f"Type `{legal_answers[0]}`, `{legal_answers[1]}`, `{legal_answers[2]}` or `{legal_answers[3]}` in the box below.")
            sleep(1)
            usr_input = input()
            usr_input = usr_input.lower().replace('"', '').replace("'", "").lstrip().rstrip()
            if usr_input in legal_answers:
                if usr_input == correct:
                    passed = True
                    jupyprint(f"Well done! That is **CORRECT**. `{output}` is {article} {correct}!")
                    if correct in ["number literal", "text literal"]:
                        jupyprint("**Remember**: literals are a special type of expression, because they show a value. They are an expression made fron **one** literal!")
                elif usr_input != correct :
                    jupyprint("That is **NOT CORRECT**. Answer again, and check the textbook if you need to!")
            else:
                jupyprint(f"Hmmm looks like you didn't type `{legal_answers[0]}`, `{legal_answers[1]}`, `{legal_answers[2]}` or `{legal_answers[3]}`")
    jupyprint("### Well done! You have finished the exercise! You can re-run the cell if you want more practice.")