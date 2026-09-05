# Make Markdown text for exercises. Binder should be used. If it is unavailable,
# backup links can be made for a Markdown file to put on Github to link to 
# Colab, then if that also fails, Deepnote (should not be used by default because
# of AI assistance)...

# Example usage:

# from mk_launch_links import make_launch_links
# make_launch_links(2, "Expressions", "exercise_2_expressions.ipynb", "mark_exercise_2.py")

def mk_binder_links(ex_num, ex_name, notebook_link, name_of_exercise_marking_file):
    text =  f"""
## Exercise {ex_num} - {ex_name}

We will now do another exercise!

*Remember*: your [assignments, tests and exams](https://pxr687.github.io/Intro_Comp_Programming/1_02_Class_Grades_Assignments_Exams.html) will also be a bit like this.

Click [here 🚀](https://mybinder.org/v2/gh/pxr687/Intro_Comp_Programming/main?urlpath=tree/{notebook_link}) to launch the exercise on Binder.
"""

    print(text)

################################################################################
# BACKUP LINKS

# Make backup links to Deepnote and Colab, IFF Binder is not available.

# Example usage:
# from mk_launch_links import make_colab_links
# make_colab_links(2, "Expressions", "exercise_2_expressions.ipynb", "mark_exercise_2.py")

def mk_colab_links(ex_num, ex_name, notebook_link, name_of_exercise_marking_file):
    text =  f"""
## Exercise {ex_num} - {ex_name} - Backup Link

Because Binder is not working we will use a different service to run our notebooks.
We will use Google Colab. The link is below.

**Important**: you must NOT use Google Colab's AI. Think about
the questions and write the code yourself. Turn off the AI in the settings menu,
me and the TA will make sure you have done this. Go to `Tools --> Settings --> AI Assistance` and 
tick/untick the boxes like this:

![](https://raw.githubusercontent.com/pxr687/Intro_Comp_Programming/refs/heads/main/images/AI_off_colab.JPG)

Click [here 🚀](https://colab.research.google.com/github/pxr687/Intro_Comp_Programming/blob/main/{notebook_link}) to launch the exercise on Google Colab.

**NOTE**: on Goolge Colab, you will have to make a new cell at the start of the 
notebook, and run this code to make the marking work:

```
!wget -q https://raw.githubusercontent.com/pxr687/Intro_Comp_Programming/main/{name_of_exercise_marking_file}
!wget -q https://raw.githubusercontent.com/pxr687/Intro_Comp_Programming/main/marking_sub_functions.py
!wget -q https://raw.githubusercontent.com/pxr687/Intro_Comp_Programming/main/mk_var.py
!pip install jupyprint
```

When you finish your answer, you can download your work:

![](https://raw.githubusercontent.com/pxr687/Intro_Comp_Programming/refs/heads/main/images/download_your_work_colab.png)
"""

    print(text)


# Deepnote links. Least preferred because of usage limit and inability to turn
# off AI. Use as a last resort.

# from mk_launch_links import make_deepnote_links
# make_deepnote_links(2, "Expressions", "exercise_2_expressions.ipynb", "mark_exercise_2.py")

def mk_deepnote_links(ex_num, ex_name, notebook_link, name_of_exercise_marking_file):
    text =  f"""
## Exercise {ex_num} - {ex_name} - Backup Link

Because Binder is not working we will use a different service to run our notebooks.
We will use Deepnote. The link is below.

**Important**: you must NOT use Deepnote's AI. Think about
the questions and write the code yourself. 

Click [here 🚀](https://deepnote.com/launch?url=https://github.com/pxr687/Intro_Comp_Programming/blob/main/{notebook_link}) to launch the exercise on Deepnote. 

**NOTE**: if you use Deepnote, you will have to make a new cell at the start of the notebook, and run this code to make the marking work:

```
pip install jupyprint
```
"""

    print(text)