#!/usr/bin/env bash

jupyter-nbconvert --ExecutePreprocessor.timeout=-1 --to notebook --execute matplotlib_tips_examples.ipynb --output matplotlib_tips_examples.1.ipynb
mv matplotlib_tips_examples.1.ipynb matplotlib_tips_examples.ipynb
jupyter-nbconvert --to html --output matplotlib_tips_examples.html matplotlib_tips_examples.ipynb
