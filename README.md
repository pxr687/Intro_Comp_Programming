# Introduction to Computer Programming

Textbook for the September 2026 Introduction to Computer Programming course at Global Academy, Siam University.

### To re-build Github Pages

Too add new page(s), uncommnet in TOC, then:

```
rm -r _build/

jupyter-book build .

ghp-import -n -p -f _build/html
```

### To make a new Exercise Notebook (e.g. not a textbook page)

Each `ipynb` file is linked by `jupytext` with an `Rmd` file. To make a new 
exercise, run this from terminal:

`python -m mk_rmd_questions <exercise number> <number of questions>`

So for example:
`python -m mk_rmd_questions 9 3 index.html`

...will print 3 blank questions for exercise 9 (exercise 9 denotes the
relevant `mark_exercise_X.py` file that will be used to mark the questions).
`index.html` puts links in the exercise to the online book, change it to a 
specific page (ideally one which helps with the exercise).

If editing an existing exercise, it can be easier to:

- temporarily delete the `ipynb` file for the exercise notebook.

- edit the `.Rmd` and marking file in a text editor.

- opening the `.Rmd` in Jupyter to test and save to re-create the `ipynb`.

Use `mk_launch_links.py` to make Markdown text containing the exercise links to
put in a textbook page.

Exercises are marked by `mark_exercise_*.py` files. These import a function from
`marking_sub_functions.py` called `mk_new_q_marking()` which generates blank
marking code.

As a (very) lo-fi way to make an exercise, `exercise_X_TEMPLATE.ipynb` is a template
for the exercise notebook. `mark_exercise_X.py` is a marking template.

### A note on checking spelling

The book is built from `.ipynb` files, but `.Rmd` files are synced because they are
easier for spellchecking. Run this from the command line to spellcheck all notebooks:

```
codespell *.Rmd
```