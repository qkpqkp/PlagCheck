# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .LxmlSyntaxError import LxmlSyntaxError

from .XPathError import XPathError

class XPathSyntaxError(LxmlSyntaxError, XPathError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


