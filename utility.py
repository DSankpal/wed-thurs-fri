"""Utility methods"""

import logging
import os
from google.cloud import _helpers


def project_id():
    """Returns the current google project"""
    x = _helpers._determine_default_project()
    return _helpers._determine_default_project()

def bucketobject_name():
    """Returns the bucket name as <project>_capitals"""
    return _helpers._determine_default_project() + '_capitals.json'

def on_cloud():
    """Returns whether the app is running on google"""
    return os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/')


def log_info(msg):
    """Simple wrapper to log everywhere"""

    if on_cloud():
        logging.info(msg)
    else:
        print msg
