Title: Creating a Static Blog with Pelican and hosting it on github user pages
Subtitle: 
Date: 2016-05-22 20:00
Category: Pelican
Tags: pelican, blog, jinja2, bootstrap, pelican-theme, pelican-plugins, github
Summary: In this post we create a simple static blog with Pelican hosted on github user pages
Slug: pelican-blog
disqus_identifier: 2189d14-pelican-blog
modified: 2016-05-22 22:00
keywords: pelican, blog

[TOC]

[//]: # ( Create static blog with Pelican hosted on github user pages)
In this post we create a static blog using pelican and using the pelican theme 'Elegant' and host the blog on github user pages

<br>
## Environment set-up
We first create a virtualenv that will contains all the necessary packages necessary for python pelican
```
bm@Work ~/webbloggh -  $ mkvirtualenv venv-pel
bm@Work ~/webbloggh -  $ source ~/.virtualenvs/venv-pel/bin/activate
(venv-pel) bm@Work ~/webbloggh -  $ pip install pelican, markdown, ghp-import, beautifulSoup4, cssmin, Pillow, cssprefixer, cssutils, pretty, six, smartypants, typogrify, webassets
```

In order to have webassets working properly, we need to install lessc (note: if you won't use webassets, you should be able to skip this step). The only simple way I found to make it work was to install nodeenv.

```
(venv-pel) bm@Work ~/webbloggh -  $ pip install nodeenv
(venv-pel) bm@Work ~/webbloggh -  $ nodeenv --python-virtualenv
(venv-pel) bm@Work ~/webbloggh -  $ npm install less
```
<br>
## Create the blog with Pelican
Now that all the necessary packages are installed, we can launch pelican to set up the static blog
```
(venv-pel) bm@Work ~/webbloggh -  $ pelican-quickstart
```

We have to answer numerous questions to have pelican do the set-up.
```
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
```


Here is the tree structure (brew tree; tree -L 1)

```
├── Makefile
├── content
├── develop_server.sh
├── fabfile.py
├── less.js
├── node_modules
├── output
├── pelican.pid
├── pelicanconf.py
├── pelicanconf.pyc
├── plugins
├── publishconf.py
├── publishconf.pyc
└── themes
```
<br>
## Adding Theme and Plugins
We can choose the default theme of pelican or pick one that is available at <http://www.pelicanthemes.com>.  In this post, we are using the theme named 'Elegant'.  We need to download the theme that we want use and put it in a folder named 'themes' at the root of our blog.  
<br>
We are also going to add the different plugins that we want use such as the one for generating the table of content. We can get pelican plugins by cloning the following repo: <https://github.com/getpelican/pelican-plugins.git>.  We need to make sure that the plugins are in a folder named 'plugins' at the root of our blog.  
<br>
Once the theme and plugins are installed at the root of our blog, we need to edit the *pelicanconf.py* file to add the following information:

    #!Python
    THEME = 'themes/elegant'
    MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc(permalink=true)']
    PLUGIN_PATHS = ['plugins', 'pelican-pluggins-master']
    PLUGINS = [ 'sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img', 'neighbors', 'latex',  'related_posts', 'assets', 'share_post', 'multi_part']

<p></p>

We can now generate the output directory and check out blog at: localhost:8000. The command `make devserver` will generate the static blog in the output directory. The command `. develop_server.sh stop` will stop the server.
```
(venv-pel) bm@Work ~/webbloggh -  $ make devserver
(venv-pel) bm@Work ~/webbloggh -  $ . develop_server.sh stop
```

<br>
## Adding comments through DISQUS
To add comment capabilities to our blog, we can register with disqus.  Make sure you fill the website url - in this case: blog.depuzzled.com.  We call the website short name: blogdepuzzled.
To test locally, we need to make sure that 2 variables are properly set in *pelicanconf.py*. SITEURL must be set such as `SITEURL = 'http://localhost:8000'` and DISQUS_SITENAME such that `DISQUS_SITENAME = "blogdepuzzled"`.

<br>
## Hosting on github user pages
Github users can host their blog on github user pages.  In order to do this, we must create a new repository named: `username.github.io` where username is our github username.  On our local machine and at the root of our blog, we create a git repository (`git init`), all the files (`git add -A`) and push them to our github account by using the pelican command: `make github`.  
We can now look at the blog at *username.github.io*


<br>
## Using custom domain
We are using godaddy.com. We need to create a new CNAME in records.  Host will be set to `blog` and points to will be your github page `username.github.io`.  Next we need to create a file named `CNAME` at the root of our blog.  This file will contain one line: `www.blog.yourwebsitename.com`.

<br>
<br>


## Appendix
We used the pelican plugin (<https://github.com/talha131/pelican-elegant>; branch: *upgrade-bootstrap-agnostically*) for this blog.  We only perform very few modifications to the template:
	
+ *base.html*: include elegant.css at line 40
+ *elegant.css*: changed various fonts

<br>
## References
<http://simonsblog.co.uk/static-site-generator-pelican.html>
<https://github.com/noirbizarre/pelican-social>
<https://github.com/getpelican/pelican/wiki/Externally-hosted-plugins-and-tools>
<https://github.com/getpelican/pelican/wiki/Powered-by-Pelican>
<http://blog.getpelican.com/author/kyle-fuller.html>
<http://oncrashreboot.com/elegant-best-pelican-theme-features>
<http://querbalken.net/howto-setup-comments-with-disqus-in-pelican-en.html>
<https://fedoramagazine.org/make-github-pages-blog-with-pelican/>
<http://mathamy.com/migrating-to-github-pages-using-pelican.html>
<http://terriyu.info/blog/posts/2013/07/pelican-setup/>
<http://nafiulis.me/making-a-static-blog-with-pelican.html>
<http://vuongnguyen.com/creating-blog-python-virtualenv-pelican.html>


<br>
<br>










