Title: Create Blog with Pelican hosted on github user page
Subtitle: 
Date: 2016-05-20 23:20
Category: Pelican
Tags: pelican, blog, jinja2, bootstrap, pelican-theme, font-awesome, github
Summary: Create a simple static blog with Pelican hosted on github user page
Slug: slg
disqus_identifier: key
modified: 2016-05-21 23:00
keywords: pelican, blog

## Create static blog with Pelican hosted on github user page
::python
mkvirtualenv venv-pel
source ~/.virtualenvs/venv-pel/bin/activate
pip install pelican, markdown, ghp-import


::python
pelican-quickstart

> Where do you want to create your new web site? [.] 
> What will be the title of this web site? blog depuzzled
> Who will be the author of this web site? depuzzled
> What will be the default language of this web site? [en] 
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) 
> What is your URL prefix? (see above example; no trailing slash) http://sb2gh.github.io
> Do you want to enable article pagination? (Y/n) 
> How many articles per page do you want? [10] 
> What is your time zone? [Europe/Paris] US/Eastern
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) 
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) 
> Do you want to upload your website using FTP? (y/N) 
> Do you want to upload your website using SSH? (y/N) 
> Do you want to upload your website using Dropbox? (y/N) 
> Do you want to upload your website using S3? (y/N) 
> Do you want to upload your website using Rackspace Cloud Files? (y/N) 
> Do you want to upload your website using GitHub Pages? (y/N) y 
> Is this your personal page (username.github.io)? (y/N) y
Done. Your new project is available at /Users/bm/webblog


::python
 make devserver
. develop_server.sh stop

::python
make github





