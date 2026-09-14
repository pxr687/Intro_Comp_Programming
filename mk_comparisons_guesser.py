from jupyprint import jupyprint
from time import sleep
import numpy as np

# Interactive task to practice comparison operators.
def comparison_guesser():
    # Start up message. Make variable name strings, and a collection of illegal
    # inputs for testing.
    jupyprint(f"*Making questions...*")
    variable_names = ["variable_"+str(val) for val in np.arange(1, 11)]
    illegal_moves_array = np.array(variable_names)
    illegal_moves_array = np.append(illegal_moves_array, "variables")
    # 10 questions total.
    for i in np.arange(10):
        sleep(2)
        # Variables in an array and unpacked.
        variables = np.random.poisson(lam=5, size=10)
        variable_1, variable_2, variable_3,\
        variable_4, variable_5, variable_6, \
        variable_7, variable_8, variable_9, \
        variable_10 = variables
        # Start question.
        jupyprint(f"## Question {i + 1}")
        jupyprint(f"A number has been selected between 0 and {variables.max()}. This number is stored in a variable called `variable_{i+1}`.")
        passed = False
        # Seek user input until correct number is guessed.
        while passed == False:
            jupyprint(f"Type Python code in the box below. Use comparison operators to work out what number `variable_{i+1}` is.")
            jupyprint(f"For example you can type `variable_{i+1} <= {variables.max() - 1}` and Python will tell you if this is `True` or `False`.")
            sleep(1)
            usr_input = input()
            # Stop user directly accessing variable values, or printing them.
            if (usr_input.strip() in illegal_moves_array) | ("print" in usr_input):
                jupyprint("#### CHECKING THE VALUE OF ANY VARIABLE IS **NOT** ALLOWED!")
            # Stop assignment statements (e.g. user cannot re-assign variable they are guessing value of).
            elif " = " in usr_input:
                jupyprint(f"#### You are trying to assign a new value to a variable. That is **NOT ALLOWED**. You should be asking about `variable_{i+1}`. You tried to use the assignment statement `{usr_input}`.")
            # Tell user if they are guessing about the wrong variable or have typed something totally irrelevant.
            elif variable_names[i] not in usr_input:
                jupyprint(f"#### You are NOT asking about the right variable, you should be asking about `variable_{i+1}`. You typed `{usr_input}`.")
            # If input is legal, evaluate it.
            else:
                print(eval(usr_input))
                sleep(1)
                jupyprint(f"Type your guess! What number do you think `variable_{i+1}` is?")
                usr_guess = input()
                if int(usr_guess) == variables[i]:
                    passed = True
                    jupyprint(f"Well done! That is **CORRECT**. You guessed `{usr_guess}` and `variable_{i+1} == {variables[i]}!`")
                else:
                    jupyprint("That is **NOT CORRECT**. Keep guessing!")