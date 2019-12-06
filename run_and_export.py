#!/usr/bin/env python

# This could be easier done in bash but I prefer to just do it in python

import glob,subprocess,os,shutil,shlex

os.chdir(os.path.dirname(__file__))
for nb in glob.glob('*.ipynb'):
    nb = os.path.splitext(nb)[0]
    
    cmd = f'jupyter-nbconvert --ExecutePreprocessor.timeout=-1 --to notebook --execute {nb}.ipynb --output {nb}.tmp.ipynb'
    subprocess.check_call(shlex.split(cmd))
    
    shutil.move(f'{nb}.tmp.ipynb',f'{nb}.ipynb')
    
    
    cmd = f'jupyter-nbconvert --to html --output {nb}.html {nb}.ipynb'
    subprocess.check_call(shlex.split(cmd))
