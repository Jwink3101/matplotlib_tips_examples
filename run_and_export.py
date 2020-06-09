#!/usr/bin/env python

# This could be easier done in bash but I prefer to just do it in python

import glob,subprocess,os,shutil,sys

os.chdir(os.path.dirname(__file__))

files = sys.argv[1:]
if not files:
    files = glob.glob('*.ipynb')

for nb in files:
    nb = os.path.splitext(nb)[0]
    
    cmd = ['jupyter-nbconvert',
           '--ExecutePreprocessor.timeout=-1',
           '--to','notebook',
           '--execute',
           f'{nb}.ipynb',
           '--output',f'{nb}.tmp.ipynb']
           
    s = subprocess.call(cmd)
    if s:
        raise subprocess.CalledProcessError()
        
    shutil.move(f'{nb}.tmp.ipynb',f'{nb}.ipynb')
    
    cmd = ['jupyter-nbconvert',
           '--to','html',
           '--output',f'{nb}.html',
           f'{nb}.ipynb']
    s = subprocess.call(cmd)
    if s:
        raise subprocess.CalledProcessError()
