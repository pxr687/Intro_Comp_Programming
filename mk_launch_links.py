# Make Markdown text for exercise.

# Example usage:

# from mk_launch_links import make_launch_links
# make_launch_links(4, "Cool Stuff", "exercise_10_cool_stuff.ipynb", "mark_exercise_10.py")

def mk_launch_links(ex_num, ex_name, notebook_link, name_of_exercise_marking_file):
    text =  f"""
## Exercise {ex_num} - {ex_name}

We will now do another exercise!

*Remember*: your [assignments, tests and exams](https://pxr687.github.io/Intro_Comp_Programming/1_02_Class_Grades_Assignments_Exams.html) will also be a bit like this.

Click [here 🚀](https://mybinder.org/v2/gh/pxr687/Intro_Comp_Programming/main?urlpath=tree/{notebook_link}) to launch the exercise on Binder.

Or click [here 🚀](https://colab.research.google.com/github/pxr687/Intro_Comp_Programming/blob/main/{notebook_link}) to launch the exercise on Google Colab.

**NOTE**: if you use Google Colab, you will have to make a new cell at the start of the notebook, and run this code:

```
!wget -q https://raw.githubusercontent.com/pxr687/Intro_Comp_Programming/main/{name_of_exercise_marking_file}
!wget -q https://raw.githubusercontent.com/pxr687/Intro_Comp_Programming/main/marking_sub_functions.py
!wget -q https://raw.githubusercontent.com/pxr687/Intro_Comp_Programming/main/mk_var.py
!pip install jupyprint
```
    """

    print(text)