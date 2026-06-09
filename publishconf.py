import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://guyschnidrig.github.io"
SITELOGO = SITEURL + "/images/favicon.svg"
RELATIVE_URLS = False
OUTPUT_PATH = "output"          # override the 'docs' from pelicanconf.py
DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ['images']
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
