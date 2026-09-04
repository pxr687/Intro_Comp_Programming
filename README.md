# Introduction to Computer Programming

Textbook for the September 2026 Introduction to Computer Programming course at Global Academy, Siam University.

### To re-build Github Pages

Too add new page(s), uncommnet in TOC, then:

```
rm -r _build/

jupyter-book build .

ghp-import -n -p -f _build/html
```

### For each new Exercise

`exercise_X_TEMPLATE.ipynb` is a template for the exercise notebook. 

`mark_exercise_X.py` is a marking template.

Use `mk_launch_links.py` to make Markdown text containing the links.

### Checking spelling

The book is built from `.ipynb` files, but `.Rmd` files are synced because they are
easier for spellchecking. Run this from the command line to spellcheck all notebooks:

```
codespell *.Rmd
```