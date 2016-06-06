Title: Virtualenv and virtualenvwrapper
Subtitle: 
Date: 2016-05-15 20:00
Category: virtualenv
Tags: virtualenv, virtualenvwrapper
Summary: Creating a clean environment for python development
Slug: virtualenv
disqus_identifier: 2189d15-virtualenv
modified: 2016-05-15 22:00
keywords: virtualenv, virtualenvwrapper

[TOC]

## Virtualenv
Virtualenv allows the creation of different python projects with each different requirement. Some of these requirements can conflict between each other. Virtualenv solves these problems by allowing the user to create specific python environment for each project.  
Set up:

1. Download: `pip install virtualenv`
2. Log into project folder: `cd ~/proj`
3. Create virtualenv (python executable + pip): `virtualenv venv`
4. Start using virtual env: `source env/bin/activate`
5. `~/proj/env/bin/pip freeze > ~/proj/requirements.txt` (this will allow anyone to recreate the virtual env easily by running: pip install –r requirements.txt)

Notes:

* you can also specify the python interpreter: `virtualenv –p /usr/bin/bython2.7 venv`
* you should also exclude the virtual env folder from your source control by adding this folder to the ignore file (i.e., “.gitignore”)


<br>
## Virtualenvwrapper
virtualenvwrapper simplify the use of virtual environments.  All the virtual environments will be stored in the same folder.

Install virtualenvwrapper: `pip install virtualenvwrapper`
Create folder where all virtual environments will be stored: `export WORKON_HOME=~/VirtEnvs`
Reload: `source /usr/local/bin/virtualenvwrapper.sh`
Create a new environment: `mkvirtualenv venv-test`
Remove virtual env: `rmvirtualenv venv-test`
List all of the venvs: `lsvirtualenv`
Go to directory of current venv: `cdvirtualenv`
Show contents of site-packages directory: `lssitepackages`
If install from requirements to continue if a package fails: 
`cat requirements.txt | while read PACKAGE; do pip install "$PACKAGE"; done`


<br>
## References
<http://docs.python-guide.org/en/latest/dev/virtualenvs/>
<https://virtualenvwrapper.readthedocs.io/en/latest/>




<br>
<br>


