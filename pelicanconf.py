#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marcwebbie'
SITENAME = u'Quilombist'
SITEURL = '//localhost:8000'
SITESUBTITLE = 'Technology and pan-africanism together'
TAGLINE = SITESUBTITLE

PATH = 'content'

TIMEZONE = 'Europe/Paris'

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
SOCIAL = (('twitter', 'https://twitter.com/marcwebbie'),
          ('github', '//github.com/marcwebbie'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

OUTPUT_PATH = "./quilombist.github.io"

TYPOGRIFY = True

STATIC_PATHS = ['images']

# Theme
THEME = "./themes/PureMod"
# THEME = "./local_themes/pelican-bootstrap3"
# THEME = "./local_themes/SoMa"
# THEME = "./local_themes/SoMa2"
# THEME = "./local_themes/Cahier"
# THEME = "./local_themes/Just-Read"
# THEME = "./local_themes/pure-single"
# THEME = "./local_themes/fresh-mod"
# THEME = "./local_themes/octopress"
# THEME = "./local_themes/simplegrey"
# THEME = "./local_themes/pure"
# THEME = "./local_themes/cahier"
# THEME = "./local_themes/foundation"


# Urls
# ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
# ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
# PAGE_URL = 'pages/{slug}/'
# PAGE_SAVE_AS = 'pages/{slug}/index.html'
