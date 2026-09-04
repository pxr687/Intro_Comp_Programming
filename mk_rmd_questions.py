# Function to make an RMD qurstion
import sys
import numpy as np

# Use from terminal:
# `python -m mk_rmd_questions 1 3 index.html``
# This will generate three blank questions for exercise 1 (exercise 1 denotes the
# relevant `mark_exercise_X.py` file)

def make_questions(exnum, n_qs, textbook_page_name, python="{python}"):

    answer_vars = f"{', '.join(f'answer_{i}' for i in np.arange(1, int(n_qs) + 1))}"

    start_of_ex_text = f"""
---
jupyter:
  jupytext:
    text_representation:
      extension: .Rmd
      format_name: rmarkdown
      format_version: '1.2'
      jupytext_version: 1.17.3
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Exercise {exnum}

If you need help, open the _[textbook page](https://pxr687.github.io//Intro_Comp_Programming/{textbook_page_name})_ for this exercise.

## Instructions

**IMPORTANT**: If you see a comment which says `# DO NOT CHANGE THIS CODE` then **DO NOT CHANGE THAT CODE**. You will probably break the exercise if you do...

**First, run the code cell below**. Click on the cell, then press `Shift + Enter`:

```{python}
# RUN THIS CELL - DO NOT CHANGE THE CODE.
import numpy as np
import mark_exercise_{exnum}
# {answer_vars} = mark_exercise_{exnum}.pre_define_blanks({n_qs})
```

**ALSO IMPORTANT**: in **ALL** exercises, and **ALL** assignments/tests/exams. You **MUST** use the right variable names in your answers. 

If the question says "make a variable called `answer_1`" you **MUST** call you variable `answer_1` or you will **NOT** get a mark.

If the question says "make a variable called `me_and_my_cat`" you **MUST** call you variable `me_and_my_cat` or you will **NOT** get a mark.

### Downloading your work

*Binder and Google Colab will NOT save your work*. If you are working on Binder, when you finish all of the questions, you can download your work as an `.ipynb` file, by clicking the button shown below:

![](https://raw.githubusercontent.com/pxr687/Intro_Comp_Programming/refs/heads/main/images/download_your_work.png)

You can also do this if you are working on Google Colab:

![](https://raw.githubusercontent.com/pxr687/Intro_Comp_Programming/refs/heads/main/images/download_your_work_colab.png)

When you download your work, you can view it by uploading the file here: https://code-format.com/ipynb-viewer 

Later in the course we will install Python on your own laptop...

"""
    print(start_of_ex_text)

    for i in np.arange(int(n_qs)):

        text = f"""
## Question {i+1}

```{python}
# Type your answer below.
answer_{i+1} = ...
```

### Run the next cell to mark your answer.

```{python}
# DO NOT CHANGE THIS CODE.
# RUN THIS CELL TO MARK YOUR ANSWER.
mark_exercise_{exnum}.check_answer_{i+1}(answer_{i+1})
```
    """

        print(text)

    end_of_ex_text = f"""
# Mark all your answers

```{python}
# DO NOT CHANGE THIS CELL. 
# Run this cell to mark all of your answers.
mark_exercise_{exnum}.mark_all({answer_vars})
```

## Go back to the textbook:

Click _[here](https://pxr687.github.io/Intro_Comp_Programming/{textbook_page_name})_ to go back to the course textbook.

"""

    print(end_of_ex_text)

if __name__ == "__main__":

    make_questions(sys.argv[1], sys.argv[2], sys.argv[3])