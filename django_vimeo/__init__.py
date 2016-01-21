"""
Django app for easy embeding Vimeo videos.
"""

VERSION = (0, 1, 5, 'dev')


def get_release():
    return '-'.join([get_version(), VERSION[-1]])


def get_version():
    """
    Returns only digit parts of version.
    """
    return '.'.join(str(i) for i in VERSION[:3])


__version__ = get_release()