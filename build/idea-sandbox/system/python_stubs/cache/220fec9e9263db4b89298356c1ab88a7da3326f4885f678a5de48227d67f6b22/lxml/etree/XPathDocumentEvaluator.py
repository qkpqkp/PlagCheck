# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .XPathElementEvaluator import XPathElementEvaluator

class XPathDocumentEvaluator(XPathElementEvaluator):
    """
    XPathDocumentEvaluator(self, etree, namespaces=None, extensions=None, regexp=True, smart_strings=True)
        Create an XPath evaluator for an ElementTree.
    
        Additional namespace declarations can be passed with the
        'namespace' keyword argument.  EXSLT regular expression support
        can be disabled with the 'regexp' boolean keyword (defaults to
        True).  Smart strings will be returned for string results unless
        you pass ``smart_strings=False``.
    """
    def __call__(self, _path, **_variables): # real signature unknown; restored from __doc__
        """
        __call__(self, _path, **_variables)
        
                Evaluate an XPath expression on the document.
        
                Variables may be provided as keyword arguments.  Note that namespaces
                are currently not supported for variables.
        """
        pass

    def __init__(self, etree, namespaces=None, extensions=None, regexp=True, smart_strings=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EEF8F60>'


