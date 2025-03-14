from datetime import datetime

# Author and Title
AUTHOR = 'Guy Schnidrig'
SITENAME = 'Guy Schnidrig'
SITEURL = ""

SITETITLE = "Guy Schnidrig, PhD"
SITESUBTITLE = "Data Scientist"
SITEDESCRIPTION = "Personal Website of Guy Schnidrig"


# Use the Flex Theme
THEME = "themes/Flex"
BROWSER_COLOR = "#333"  # Change the browser tab color on mobile
PYGMENTS_STYLE = "monokai"
ROBOTS = "index, follow"

# Paths
PATH = "content"
OUTPUT_PATH = 'docs'
RELATIVE_URLS = True
DISABLE_URL_HASH = True
DEFAULT_PAGINATION = 5

# Time and Language
TIMEZONE = 'Europe/Rome'
I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Blogroll
SOCIAL = (("github", "https://github.com/GuySchnidrig"),
          ("linkedin", "https://www.linkedin.com/in/guy-schnidrig/"),
          ("rss", "/blog/feeds/all.atom.xml"),
          )


GITHUB_CORNER_URL = "https://github.com/GuySchnidrig"

# Menu
MENUITEMS = (
    ("About Me", "/pages/about.html"),
    ("Contact", "/pages/contact.html"),
)

# License
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}

COPYRIGHT_YEAR = datetime.now().year


DISQUS_SITENAME = "Guy-Schnidrig"
ADD_THIS_ID = "42"

# Darkmode
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True