import urllib.parse
import re

# Patch re.sre_parse for lk21/exrex compatibility on Python 3.12+
if not hasattr(re, "sre_parse"):
    import re._parser
    re.sre_parse = re._parser


# Save the REAL original urlparse before patching
_original_urlparse = urllib.parse.urlparse


def safe_urlparse(url):
    try:
        return _original_urlparse(url)
    except Exception:
        return _original_urlparse("http://invalid")


# Patch urlparse safely
urllib.parse.urlparse = safe_urlparse


# Now import lk21 AFTER monkey patch
import lk21


# Apply pyrogram save_file patch
from . import pyrogram_patch
