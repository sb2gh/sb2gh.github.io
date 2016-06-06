#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'depuzzled'
SITENAME = u'depuzzled blog'
SITEURL = 'http://localhost:8000'

PATH = 'content'
THEME = 'themes/peuba'
STATIC_PATHS = ['theme/images']#, 'images']

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc(permalink=true)']
PLUGIN_PATHS = ['plugins', 'pelican-pluggins-master']
PLUGINS = [ 'sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img',
           'neighbors', 'latex', 'related_posts', 'assets', 'share_post',
           'multi_part']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
#PLUGIN_PATHS = ["pelican-pluggins-master", "/pelican-pluggins-master", "plugins"]
#PLUGINS = ["sitemap"]

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

DISQUS_SITENAME = "blogdepuzzled"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
