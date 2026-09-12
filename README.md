# Introduction to Computer Programming

Textbook for the September 2026 Introduction to Computer Programming course at Global Academy, Siam University.

### Backup Exercise services if Binder fails

See `mk_launch_links.py` to generate Markdown links to other services.

### To re-build Github Pages

Too add new page(s), uncommnet in TOC, then:

```
rm -r _build/

jupyter-book build .

ghp-import -n -p -f _build/html
```

### To make a new Exercise Notebook (e.g. not a textbook page)

For marking script explanation go to the README at: https://github.com/pxr687/Intro_Comp_Programming_DEV

### A note on checking spelling

The book is built from `.ipynb` files, but `.Rmd` files are synced because they are
easier for spellchecking. Run this from the command line to spellcheck all notebooks:

```
codespell *.Rmd
```
